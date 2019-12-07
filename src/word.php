<?php // https://www.cs.rpi.edu/~goldsd/wordfreq.php

  session_start();

  ini_set( "allow_url_fopen", true );

  // used for bigram/trigram processing, i.e., when ngram > 1
  $skip = [ "the", "of", "to", "and", "in", "said", "for", "that", "was", "on",
            "he", "is", "with", "at", "by", "it", "from", "as", "be", "were",
            "an", "have", "his", "but", "has", "are", "not", "who", "they", "its",
            "had", "will", "would", "about", "been", "this", "their", "new", "or", "which",
            "we", "more", "after", "us", "percent", "up", "one", "people" ];

  if ( isset( $_GET['submitted'] ) && isset( $_GET['url'] ) )
  {
    $url = $_GET['url'];
    $displaystyle = 'inline';
    $ngram = 1;
    if ( isset( $_GET['ngram'] ) ) $ngram = $_GET['ngram'];

    $content = file_get_contents( $url );     // dangerous......!

    // remove special characters (e.g. &nbsp;)
    $content = preg_replace( '/&nbsp;/', '', $content );
    $content = preg_replace( '/&quot;/', '', $content );
    $content = preg_replace( '/&amp;/', '', $content );
    $content = preg_replace( '/&lt;/', '', $content );
    $content = preg_replace( '/&gt;/', '', $content );

    // remove <script>..</script>
    $content = preg_replace( '/<script.+?<\/script>/s', ' ', $content );

    // remove (crudely) all HTML tags <...>
    $content = preg_replace( '/<[^<>]+>/', ' ', $content );

    // isolate all "words" by simply grouping every set of a-z'
    $wlist = preg_split( '/[^a-z\']+/', strtolower( $content ), 0, PREG_SPLIT_NO_EMPTY );

    $wordlist = array();

    foreach ( $wlist as $word )
    {
      // remove leading and trailing ' characters
      $word = trim( $word, '\'' );

      // skip one-letter words
      if ( strlen( $word ) <= 1 ) continue;

      if ( substr_count( $word, '\'' ) > 1 )
      {
//print "Replaced \"$word\" with ";
        // This only isolates word with first ' character (e.g., "o'brien's==>o'brien"):
        $word = preg_replace( '/([a-z]+\'[a-z]+).*/', '$1', $word );
//print "\"$word\"<br />";
      }

      $wordlist[] = $word;
    }

//print_r( $wordlist );

    if ( !isset( $_SESSION['words'] ) )
    {
      $_SESSION['words'] = array();
    }

    for ( $i = 0 ; $i < count( $wordlist ) - ( $ngram - 1 ) ; $i++ )
    {
      if ( $ngram > 1 )
      {
        $words = array();
        $stop = false;

        for ( $j = 1 ; $j <= $ngram ; $j++ )
        {
          $words[$j] = $wordlist[$i+$j-1];
          if ( in_array( $words[$j], $skip ) ) { $stop = true; break; }
        }

        if ( $stop ) continue;

        $word = $words[1];

        for ( $j = 2 ; $j <= $ngram ; $j++ )
        {
          $word .= ' ' . $words[$j];
        }
      }
      else
      {
        $word = $wordlist[$i];
      }

      if ( strlen( $word ) <= 1 ) continue;

      if ( isset( $_SESSION['words'][$word] ) )
      {
        $_SESSION['words'][$word]++;
      }
      else
      {
        $_SESSION['words'][$word] = 1;
      }
    }

//    arsort( $_SESSION['words'] );

    array_multisort( array_values( $_SESSION['words'] ), SORT_DESC,
                     array_keys( $_SESSION['words'] ), SORT_ASC,
                     $_SESSION['words'] );

    $output = '';
    $_SESSION['totalwords'] = 0;
    $j = 1;

    foreach ( $_SESSION['words'] as $word => $numocc )
    {
      $output .= "#{$j}:\t{$numocc}\t{$word}\n";
      $_SESSION['totalwords'] += $numocc;
      $j++;
    }

    $_SESSION['urllist'] .= "[{$url}] ";
  }
  else
  {
    $url = '';
    $displaystyle = 'none';
    $output = '';
    $_SESSION['words'] = array();
    $_SESSION['urllist'] = '';
  }
?>

<html>
  <head>
    <title>Simple Word Frequency Counter</title>
  </head>
  <body>
    <form action="wordfreq.php" method="get">
      <input type="hidden" name="submitted" id="submitted" value="1" />
      <p>
        Enter URL:&nbsp;<input type="text" name="url" id="url" size="70" />
        ngrams:&nbsp;<input type="text" name="ngram" id="ngram" size="10" />
        <input type="submit" value="go get it" />
      </p>
    </form>

    <div id="results" style="display: <?php print $displaystyle; ?>;">
      <hr />
      <p>
        <a href="wordfreq.php" style="text-decoration: none;">&raquo; start over</a>
      </p>
      <p>
        Processed URLS <?php print $_SESSION['urllist']; ?>
<pre>
TOTAL WORDS: <?php print $_SESSION['totalwords']; ?>

UNIQUE WORDS: <?php print count( $_SESSION['words'] ); ?>

<?php print $output; ?>
</pre>
    </div>

  </body>
</html>

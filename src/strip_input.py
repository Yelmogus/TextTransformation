from bs4 import BeautifulSoup
'''
    stripInput:
    params: String doc
    return: String parsed_text
    errors:
        - If the string is invalid, throw InvalidStringException


    description: Given a string filename, stripInput will:
        1) Go through the string and remove all html tags/content (<title>, <h1>, <script> etc).
        2) Go through the string and remove all extra characters (eg. ain''t -> ain't)
        3) Go through the string and lowercase all words
        4) Remove all stop words () from the parsed text
        5) Return the text

    ex: INPUT: "filename.txt"
    ex: OUTPUT: "parsedtext.txt"
'''
stop_words = ["the","of","to","and","in","said","for","that","was","on","he","is","with","at",
              "by","it","from","as","be","were","an","have","his","but","has","are","not","who",
              "they","it’s","had","will","would","about","been","this","their","new","or","which",
              "we","more","after","us","percent","up","one","people","a","i"]

def stripInput(doc):
    # Use BeautifulSoup to take the given input and strip out all the html tags
    # and then lowercase everything
    soup = BeautifulSoup(doc)
    parsed_text = soup.get_text()
    parsed_text.lower()

    # Check out each stop word and, if its within the parsed_text, remove it
    for x in stop_words:
        parsed_text.replace(x, '')

    # Go through parsed_text and strip out all extra chracters
    # Also be sure to handle special cases when it comes to ' and -
    parsed_text = re.sub(r'[`1234567890-=~!@#$%^&*()_+]',"",parsed_text)

    parsed_text = re.sub(r'\'\'',"'",parsed_text)
    parsed_text = re.sub(r' \''," ",parsed_text)
    parsed_text = re.sub(r'\' '," ",parsed_text)

    parsed_text = re.sub(r'--',"-",parsed_text)
    parsed_text = re.sub(r' -'," ",parsed_text)
    parsed_text = re.sub(r'- '," ",parsed_text)

    return parsed_text

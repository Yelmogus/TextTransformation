""""
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
"""
from bs4 import BeautifulSoup
import re

stop_words = ["the", "of", "to", "and", "in", "said", "for", "that", "was", "on", "he", "is", "with", "at",
              "by", "it's", "it", "from", "as", "be", "were", "an", "have", "his", "but", "has", "are", "not", "who",
              "they", "had", "will", "would", "about", "been", "this", "their", "new", "or", "which",
              "we", "more", "after", "us", "percent", "up", "one", "people", "a", "i"]


def strip_input(doc, strip_stop_words=True):
    # Use BeautifulSoup to take the given input and strip out all the html tags
    # and then lowercase everything
    soup = BeautifulSoup(doc, "lxml")
    parsed_text = soup.get_text()
    parsed_text = parsed_text.lower()


    # Check out each stop word and, if its within the parsed_text, remove it
    #this regex checks for each stop word surrounded by word breaks (\b), excluding apostrophes.
    if strip_stop_words:
        rx = re.compile("|".join(r'(?<!\'\w)\b'+x+r'\b(?!\'\w)' for x in stop_words))
        parsed_text = rx.sub('', parsed_text)

    # Go through parsed_text and strip out all extra chracters
    # Also be sure to handle special cases when it comes to ' and -
    if parsed_text[0] == "\'" and parsed_text[0] == "-":
        s = list(parsed_text)
        s[0] = ""
        parsed_text = "".join(s)

    if parsed_text[-1] == "\'" and parsed_text[0] == "-":
        s = list(parsed_text)
        s[-1] = ""
        parsed_text = "".join(s)

    parsed_text = re.sub(r'[`\=\-\~\!\@\#\$\%\^\&\*\(\)\_\+]', "", parsed_text)

    parsed_text = re.sub(r'\'\'', "'", parsed_text)
    parsed_text = re.sub(r' \'|\' ', " ", parsed_text)

    parsed_text = re.sub(r'--', "-", parsed_text)
    parsed_text = re.sub(r' -|- ', " ", parsed_text)

    return parsed_text.strip()

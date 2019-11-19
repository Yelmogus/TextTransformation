'''
    stripInput:
    params: String file_name
    return: String parsed_text
    errors:
        - If the file name is invalid, throw InvalidFileException


    description: Given a string filename, stripInput will:
        1) Go through the file and remove all html tags/content (<title>, <h1>, <script> etc).
        2) Go through the file and remove all extra characters (eg. ain''t -> ain't)
        3) Go through the file and lowercase all words
        4) Place the parse file into a new file parsed_text and return it

    ex: INPUT: "filename.txt"
    ex: OUTPUT: "parsedtext.txt"
'''
def stripInput(filename):
    return None

from flask import Flask

app = Flask(__name__)


'''
    stripInput:
    params: String data
    return: String parsed_text
    errors:
        - If the file name is invalid, throw InvalidFileException


    description: Given a string filename, stripInput will:
        1) Go through the data and remove all html tags/content (<title>, <h1>, <script> etc).
        2) Go through the data and remove all extra characters (eg. ain''t -> ain't)
        3) Go through the data and lowercase all words
        4) Place the parse data into a new file parsed_text and return it

    ex: INPUT: data
    ex: OUTPUT: parsed_text
'''
def stripInput(data):
    return ""


'''
calculateNGrams
params: String data
        int n
errors:
    - If the data is empty, return an empty list
    - If n is not such that 1 <= n <= number of words in the data,
      return an empty list


description: Given a string data and and int n, calculateNGrams will:
    1.) Find all the n grams
    2.) Find out how many times those n grams appear in the data
    3.) Find out their relative locations in the data

ex: INPUT: "hello other search engine team hello other"; 2
ex: OUTPUT: [{"hello other", 2, [0, 5]} , {"other search", 1, [1]},
            {"search engine"}, 1, [2]}, {"engine team", 1, [3]}, {"team hello"},
            1, [4]}]
'''
def calculateNGrams(data, n):
    return [{"", 0, [0]}]

'''
locationNGrams
parms: String data
       String n_gram

description: Given a string data and a string n_gram, locationNGrams will:
    1.) Return a list of relative locations of where that n_gram is found
        in the data

ex: INPUT: "hello other search engine team hello other"; "hello other"
ex: OUTPUT: [0, 5]
'''
def locationNGrams(data, n_gram):
    return [0]

'''
    get_title:
    n = 40
    params: data -- html document (as a string)

    Obtains a document title, to appear as the main link for the
    page in the UI. Finds the first best, non-empty text tag, prioritizing <title>,
    <h1>, <h2>, <h3>, <h4>, <h5>, <h6>, then <p>, and returns a string
    of the first [n] characters. [n] is a constant that should be easily changeable.
    Provide an option for infinite [n], when n=-1.
    If no non-empty tags are found, returns an empty string.
'''
def get_title(data):
    return ""

"""
handleInputs
parms: None

Description: This is the driver function and makes and receives API calls.
    Given input from flask handleInput will:
        1.) Call stripInput with correct data
        2.) Call calculateNGrams with correct data
        3.) Call checkTitle with correct data
        4.) Compile all data from sub functions, format data in JSON file
            and return to API caller
"""
@app.route('/transform')
def handleInputs():
    return 0;

if __name__ == '__main__':
    app.run()

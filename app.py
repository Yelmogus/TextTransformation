from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json
from pattern.text.en import ngrams

app = Flask(__name__)


@app.route('/transform')
def handleInputs():
    return "Hello World"


if __name__ == '__main__':
    app.run()

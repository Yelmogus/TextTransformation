from flask import Flask
from flask_json import FlaskJSON, JsonError, json_response, as_json

app = Flask(__name__)


@app.route('/transform')
def handleInputs():
    return 0


if __name__ == '__main__':
    app.run()

from flask import Flask, request, json
from flask_json import FlaskJSON, as_json
from src import get_title, calculate_ngrams, strip_input
import json

app = Flask(__name__)
FlaskJSON(app)


@app.route('/transform', methods=['POST'])
@as_json
def handle_transformation():
    client_request_data = request.data.decode()
    data = json.loads(client_request_data)

    stripped_text = strip_input.stripInput(data["data"])
    if data["transformations"]["title"]:
        title = get_title.get_title(data["data"])
    else:
        title = ""

    response = {"stripped": stripped_text,
                "grams": calculate_ngrams.calculate_ngrams(stripped_text, data["transformation"]["grams"]),
                "title": title
                }
    return response


if __name__ == '__main__':
    app.run()

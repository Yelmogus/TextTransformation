from flask import Flask, request, json
from flask_json import FlaskJSON, JsonError, json_response, as_json
from src import get_title, handle_input, location_ngrams, ngrams, strip_input
import json
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

    stripped_text = strip_input.strip_input(data["data"])
    if data["transformations"]["title"]:
        title = get_title.get_title(data["data"])
    else:
        title = ""

    response = {"stripped": stripped_text,
                "grams": location_ngrams.locationNGrams(stripped_text),
                "title": title
                }
    return response


if __name__ == '__main__':
    app.run()

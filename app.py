from flask import Flask, request, json
from flask_json import FlaskJSON, as_json
from src import get_title, strip_input, calculate_ngrams, constants as c
import json

app = Flask(__name__)
FlaskJSON(app)


@app.route('/transform', methods=['POST'])
@as_json
def handle_transformation():
    client_request_data = request.data.decode()
    data = json.loads(client_request_data)

    stripped_text = strip_input.strip_input(data[c.DATA], strip_stop_words=data[c.TRANS][c.STRIPPED]).lower()
    title = get_title.get_title(data[c.DATA], title_req=data[c.TRANS][c.TITLE])

    response = {c.STRIPPED: stripped_text,
                c.GRAMS: calculate_ngrams.calculate_ngrams(stripped_text, data[c.TRANS][c.GRAMS]),
                c.TITLE: title.lower()
                }
    return response


if __name__ == '__main__':
    app.run()

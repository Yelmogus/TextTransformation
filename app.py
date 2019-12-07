from flask import Flask, request, json
from flask_json import FlaskJSON, as_json
from src import get_title, strip_input, calculate_ngrams, constants as const
import json

app = Flask(__name__)
FlaskJSON(app)


@app.route('/transform', methods=['POST'])
@as_json
def handle_transformation():
    client_request_data = request.data.decode()
    data = json.loads(client_request_data)

    stripped_text = strip_input.strip_input(data[const.DATA], strip_stop_words=data[const.TRANSFORMATIONS][const.STRIPPED])
    title = get_title.get_title(data[const.DATA], title_req=data[const.TRANSFORMATIONS][const.TITLE])

    response = {const.STRIPPED: stripped_text,
                const.GRAMS: calculate_ngrams.calculate_ngrams(stripped_text, data[const.TRANSFORMATIONS][const.GRAMS]),
                const.TITLE: title
                }
    return response


if __name__ == '__main__':
    app.run()

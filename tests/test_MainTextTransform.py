import pytest
import json
from app import app


@pytest.mark.parametrize("input_file, output_file", [
    ("in0.json", "out0.json"),
    ("in1.json", "out1.json"),
    ("in2.json", "out2.json"),
    ("in4.json", "out4.json"),
    ("in5.json", "out5.json")
])
def test_transform(input_file, output_file):
    tester = app.test_client()
    with open(input_file) as json_input_file:
        request_body = json.load(json_input_file)
        response = tester.post('/transform', content_type='html/text', json=request_body)
        with open(output_file) as json_output_file:
            assert response.get_json() == json.load(json_output_file)
            assert response.status == "200 OK"

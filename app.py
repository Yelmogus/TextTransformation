from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def main_routine():
    request.data
    return 'Hello Woas asd f  asdfdfrld!'

if __name__ == '__main__':
    app.run()

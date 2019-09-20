from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def responder():
    data = request.get_data()

    if data == 'What is your full name?':
        return 'George Peterson'

    return 'OK'


if __name__ == '__main__':
    app.run()


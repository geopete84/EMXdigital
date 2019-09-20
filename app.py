from flask import Flask
from flask import request

app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_body())


@app.route('/', methods=['GET'])
def responder():
    data = request.get_data()

    if data == 'What is your full name?':
        return 'George Peterson'

    return 'OK'


if __name__ == '__main__':
    app.run()


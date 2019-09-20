from flask import Flask
from flask import request
import logging
app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Form: %s', request.form)
    app.logger.debug('Json: %s', request.json)


@app.route('/', methods=['GET'])
def responder():
    data = request.get_data()

    if data == 'What is your full name?':
        return 'George Peterson'

    return 'OK'


if __name__ == '__main__':
    app.run()


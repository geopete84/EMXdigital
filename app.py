from flask import Flask
from flask import request
import logging
from pprint import pprint
app = Flask(__name__)

if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Args: %s', request.args)
    app.logger.debug('Form: %s', request.form)
    app.logger.debug('Data: %s', request.data)
    app.logger.debug('Json: %s', request.json)


@app.route('/', methods=['GET'])
def responder():
    args = request.args

    app.logger.debug(pprint(args))

    return 'OK'


if __name__ == '__main__':
    app.run()


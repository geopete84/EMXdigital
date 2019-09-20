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

    if args.get('Name'):
        return 'George Peterson'

    if args.get('Position'):
        return 'Senior Full Stack Python Engineer'

    if args.get('Ping'):
        return 'OK'

    if args.get('Puzzle'):
        # TODO: do the puzzle
        pass

    if args.get('Years'):
        return '9 years'

    if args.get('Degree'):
        return 'Masters of Science in Electrical and Computer Engineering from Southern Illinois University Carbondale'

    if args.get('Status'):
        return 'US Citizen'

    if args.get('Source'):
        return 'https://github.com/geopete84/EMXdigital'

    if args.get('Resume'):
        return 'https://docs.google.com/document/d/e/2PACX-1vTnZCilVuyER89N3c4PLPJHscAbaoRNkXISkNP4B_oDyaxQ9k4PHIw1LVmeF5dnJakdRcpez4UMcrfg/pub'

    if args.get('Phone'):
        return '8152364740'

    if args.get('Referrer'):
        return 'Glassdoor'

    if args.get('Email Address'):
        return 'geopete84@gmail.com'

    return 'working on it'


if __name__ == '__main__':
    app.run()


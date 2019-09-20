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
    app.logger.debug('Args: %s', request.args)
    app.logger.debug('Form: %s', request.form)
    app.logger.debug('Data: %s', request.data)
    app.logger.debug('Json: %s', request.json)


@app.route('/', methods=['GET'])
def responder():
    arguments = request.args.to_dict()
    title = arguments['q']
    if title == 'Name':
        return 'George Peterson'

    if title == 'Position':
        return 'Senior Full Stack Python Engineer'

    if title == 'Ping':
        return 'OK'

    if title == 'Puzzle':
        import re
        result = re.search('Please solve this puzzle:\n ABCD\nA(....)\nB(....)\nC(....)\nD(....)\n',
                           arguments['d'])

        matrix = [['x' for y in range(4)] for x in range(4)]
        for i in range(4):
            for j in range(4):
                if i == j:
                    matrix[i][j] = '='

        return ' ABCD\nA{}\nB{}\nC{}\nD{}'.format(''.join(matrix[0]),
                                                  ''.join(matrix[1]),
                                                  ''.join(matrix[2]),
                                                  ''.join(matrix[3]))


    if title == 'Years':
        return '9 years'

    if title == 'Degree':
        return 'Masters of Science in Electrical and Computer Engineering from Southern Illinois University Carbondale'

    if title == 'Status':
        return 'US Citizen'

    if title == 'Source':
        return 'https://github.com/geopete84/EMXdigital'

    if title == 'Resume':
        return 'https://docs.google.com/document/d/e/2PACX-1vTnZCilVuyER89N3c4PLPJHscAbaoRNkXISkNP4B_oDyaxQ9k4PHIw1LVmeF5dnJakdRcpez4UMcrfg/pub'

    if title == 'Phone':
        return '8152364740'

    if title == 'Referrer':
        return 'Glassdoor'

    if title == 'Email Address':
        return 'geopete84@gmail.com'

    return 'working on it'


if __name__ == '__main__':
    app.run()


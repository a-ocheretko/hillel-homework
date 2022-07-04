from flask import Flask, request, Response, render_template
from datetime import datetime
from random import choice
from werkzeug.exceptions import abort
from os import environ

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    browser = request.user_agent
    ip_address = request.remote_addr
    server_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render_template('whoami.html', browser=browser, ip_address=ip_address, server_time=server_time)


@app.route('/source_code')
def source_code():
    with open('app.py') as file:
        content = file.read()
        return Response(content, mimetype='text/plain')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/random')
def random():
    strng = ''
    letters = [chr(i) for i in list(range(65, 91)) + list(range(97, 123))]
    digs = '1234567890'
    specs = '!"№;%:?*()_+'
    length = request.values.get('length', '')
    digits = request.values.get('digits', '')
    specials = request.values.get('specials', '')
    try:
        if int(length) in range(1, 101) and int(digits) in (0, 1) and int(specials) in (0, 1):
            if int(digits) == 1:
                letters += digs
            if int(specials) == 1:
                letters += specs
            for i in range(int(length)):
                strng += choice(letters)
            return render_template('random_string.html', strng=strng)
    except ValueError:
        return abort(Response(render_template('random_string_error.html')))
    return abort(Response(render_template('random_string_error.html')))


if __name__ == '__main__':
    port = int(environ.get('PORT', 5000))
    app.run(app.run(debug=True, host='0.0.0.0', port=port))

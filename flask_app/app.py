from flask import Flask, request, Response
from datetime import datetime
from random import choice
from werkzeug.exceptions import abort

app = Flask(__name__)


@app.route('/whoami')
def whoami():
    browser = request.user_agent
    ip_address = request.remote_addr
    server_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return (f"<p>Client browser: {browser}</p>"
            f"<p>Client IP: {ip_address}</p>"
            f"<p>Server time: {server_time}</p>")


@app.route('/source_code')
def source_code():
    with open('app.py') as file:
        content = file.read()
        return Response(content, mimetype='text/plain')


@app.route('/')
def main():
    return (f'''<body>
                <h1>Hello!</h1>
                <p>To get a random string please enter string length (integer from 1 to 100) and if digits and specials 
                should be used (0 - False, 1 - True)</p>
                <form action="/random">
                    <label for="POST-name">Length:</label>
                    <input id="POST-name" type="text" name="length" value="20">
                    <label for="POST-name">Digits:</label>
                    <input id="POST-name" type="text" name="digits" value="0">
                    <label for="POST-name">Specials:</label>
                    <input id="POST-name" type="text" name="specials" value="0">
                    <input type="submit" value="Submit">
                </form>
                </body>''')


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
        if int(length) in range(1, 101) and int(digits) in range(0, 2) and int(specials) in range(0, 2):
            if int(digits) == 1:
                letters += digs
            if int(specials) == 1:
                letters += specs
            for i in range(int(length)):
                strng += choice(letters)
            return strng
    except ValueError:
        return abort(Response('''
        <body>
        <h1>Invalid parameters</h1>
        </body>'''))
    return abort(Response('''
    <body>
    <h1>Invalid parameters</h1>
    </body>'''))

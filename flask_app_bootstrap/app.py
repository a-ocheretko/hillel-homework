from flask import Flask, request, Response
from datetime import datetime
from random import choice
from werkzeug.exceptions import abort


app = Flask(__name__)

app.run(debug=True)


@app.route('/whoami')
def whoami():
    browser = request.user_agent
    ip_address = request.remote_addr
    server_time = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return f'''<!doctype html>
                            <html lang="en">                
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                                    rel="stylesheet" 
                                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                                    crossorigin="anonymous">
                                    <title>Random string generator</title>
                                </head>
                                <body class="d-flex flex-column min-vh-100">
                                <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                                    <symbol id="twitter" viewBox="0 0 16 16">
                                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                    </symbol>
                                </svg>
                                    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                                        <div class="container-fluid">
                                            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                                                <div class="navbar-nav">
                                                    <a class="nav-link active" aria-current="page" href="./">Home</a>
                                                    <a class="nav-link" href="./whoami">Who am I?</a>
                                                    <a class="nav-link" href="./source_code">Source code</a>
                                                </div>
                                            </div>
                                        </div>
                                    </nav>
                                    <br>
                                    <br>
                                    <br>
                                    <h2><center>Client browser</center></h2>
                                    <p><center>{browser}</center></p>
                                    <br>
                                    <br>
                                    <h2><center>Client IP</center></h2>
                                    <p><center>{ip_address}</center></p>
                                    <br>
                                    <br>
                                    <h2><center>Server time</center></h2>
                                    <p><center>{server_time}</center></p>
                                    <br>
                                    <br>
                                    <div class="wrapper flex-grow-1"></div>
                                    <div class="b-example-divider"></div>
                                        <div class="container">
                                          <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                                            <div class="col-md-4 d-flex align-items-center">
                                              <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                                                <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
                                              </a>
                                              <span class="text-muted">&copy; 2022 Andrii Ocheretko</span>
                                            </div>
                                            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                                                <li class="ms-3"><a class="text-muted" href="https://twitter.com/AndriiOcheretko"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
                                            </ul>
                                          </footer>
                                        </div>
                                </body>
                            </html>'''


@app.route('/source_code')
def source_code():
    with open('app.py') as file:
        content = file.read()
        return Response(content, mimetype='text/plain')


@app.route('/')
def home():
    return f'''<!doctype html>
                <html lang="en">                
                    <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                        rel="stylesheet" 
                        integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                        crossorigin="anonymous">
                        <title>Random string generator</title>
                    </head>
                    <body class="d-flex flex-column min-vh-100">
                    <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                        <symbol id="twitter" viewBox="0 0 16 16">
                        <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                        </symbol>
                    </svg>
                        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                            <div class="container-fluid">
                                <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                                    <div class="navbar-nav">
                                        <a class="nav-link active" aria-current="page" href="./">Home</a>
                                        <a class="nav-link" href="./whoami">Who am I?</a>
                                        <a class="nav-link" href="./source_code">Source code</a>
                                    </div>
                                </div>
                            </div>
                        </nav>
                        <br>
                        <br>
                        <h1><center>Hello!</center></h1>
                        <br>
                        <p><center>To generate a random string please enter string length (integer from 1 to 100) and if digits and 
                        specials should be used (0 - False, 1 - True)</center></p>
                        <br>
                        <form class="row g-3" action="/random">
                        <center>
                          <div class="col-auto">
                            <label for="POST-name">Length:</label>
                            <input id="POST-name" type="text" name="length" value="20">
                            <label for="POST-name">Digits:</label>
                            <input id="POST-name" type="text" name="digits" value="0">
                            <label for="POST-name">Specials:</label>
                            <input id="POST-name" type="text" name="specials" value="0">
                            <div class="col-auto">
                                <br>
                                <button type="submit" class="btn btn-primary mb-3">Submit</button>
                            </div>
                          </div>
                        </center>
                        </form>
                        <div class="wrapper flex-grow-1"></div>
                        <div class="b-example-divider"></div>
                            <div class="container">
                              <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                                <div class="col-md-4 d-flex align-items-center">
                                  <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                                    <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
                                  </a>
                                  <span class="text-muted">&copy; 2022 Andrii Ocheretko</span>
                                </div>
                                <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                                    <li class="ms-3"><a class="text-muted" href="https://twitter.com/AndriiOcheretko"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
                                </ul>
                              </footer>
                            </div>
                    </body>
                </html>'''


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
            return f'''<!doctype html>
                            <html lang="en">                
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                                    rel="stylesheet" 
                                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                                    crossorigin="anonymous">
                                    <title>Random string generator</title>
                                </head>
                                <body class="d-flex flex-column min-vh-100">
                                <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                                    <symbol id="twitter" viewBox="0 0 16 16">
                                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                    </symbol>
                                </svg>
                                    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                                        <div class="container-fluid">
                                            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                                                <div class="navbar-nav">
                                                    <a class="nav-link active" aria-current="page" href="./">Home</a>
                                                    <a class="nav-link" href="./whoami">Who am I?</a>
                                                    <a class="nav-link" href="./source_code">Source code</a>
                                                </div>
                                            </div>
                                        </div>
                                    </nav>
                                    <br>
                                    <br>
                                    <br>
                                    <h3><center>And this is a random string:</center></h3>
                                    <br>
                                    <br>
                                    <br>
                                    <center><b>{strng}</b></center>
                                    <div class="wrapper flex-grow-1"></div>
                                    <div class="b-example-divider"></div>
                                        <div class="container">
                                          <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                                            <div class="col-md-4 d-flex align-items-center">
                                              <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                                                <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
                                              </a>
                                              <span class="text-muted">&copy; 2022 Andrii Ocheretko</span>
                                            </div>
                                            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                                                <li class="ms-3"><a class="text-muted" href="https://twitter.com/AndriiOcheretko"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
                                            </ul>
                                          </footer>
                                        </div>
                                </body>
                            </html>'''
    except ValueError:
        return abort(Response(f'''<!doctype html>
                            <html lang="en">                
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                                    rel="stylesheet" 
                                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                                    crossorigin="anonymous">
                                    <title>Random string generator</title>
                                </head>
                                <body class="d-flex flex-column min-vh-100">
                                <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                                    <symbol id="twitter" viewBox="0 0 16 16">
                                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                    </symbol>
                                </svg>
                                    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                                        <div class="container-fluid">
                                            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                                                <div class="navbar-nav">
                                                    <a class="nav-link active" aria-current="page" href="./">Home</a>
                                                    <a class="nav-link" href="./whoami">Who am I?</a>
                                                    <a class="nav-link" href="./source_code">Source code</a>
                                                </div>
                                            </div>
                                        </div>
                                    </nav>
                                    <br>
                                    <br>
                                    <br>
                                    <h3><center>Oops, something went wrong...</center></h3>
                                    <br>
                                    <br>
                                    <p><center>String generator parameters you've entered are not valid</center></p>
                                    <br>
                                    <div class="wrapper flex-grow-1"></div>
                                    <div class="b-example-divider"></div>
                                        <div class="container">
                                          <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                                            <div class="col-md-4 d-flex align-items-center">
                                              <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                                                <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
                                              </a>
                                              <span class="text-muted">&copy; 2022 Andrii Ocheretko</span>
                                            </div>
                                            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                                                <li class="ms-3"><a class="text-muted" href="https://twitter.com/AndriiOcheretko"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
                                            </ul>
                                          </footer>
                                        </div>
                                </body>
                            </html>'''))
    return abort(Response(f'''<!doctype html>
                            <html lang="en">                
                                <head>
                                    <meta charset="utf-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1">
                                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" 
                                    rel="stylesheet" 
                                    integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" 
                                    crossorigin="anonymous">
                                    <title>Random string generator</title>
                                </head>
                                <body class="d-flex flex-column min-vh-100">
                                <svg xmlns="http://www.w3.org/2000/svg" style="display: none;">
                                    <symbol id="twitter" viewBox="0 0 16 16">
                                    <path d="M5.026 15c6.038 0 9.341-5.003 9.341-9.334 0-.14 0-.282-.006-.422A6.685 6.685 0 0 0 16 3.542a6.658 6.658 0 0 1-1.889.518 3.301 3.301 0 0 0 1.447-1.817 6.533 6.533 0 0 1-2.087.793A3.286 3.286 0 0 0 7.875 6.03a9.325 9.325 0 0 1-6.767-3.429 3.289 3.289 0 0 0 1.018 4.382A3.323 3.323 0 0 1 .64 6.575v.045a3.288 3.288 0 0 0 2.632 3.218 3.203 3.203 0 0 1-.865.115 3.23 3.23 0 0 1-.614-.057 3.283 3.283 0 0 0 3.067 2.277A6.588 6.588 0 0 1 .78 13.58a6.32 6.32 0 0 1-.78-.045A9.344 9.344 0 0 0 5.026 15z"/>
                                    </symbol>
                                </svg>
                                    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                                        <div class="container-fluid">
                                            <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
                                                <div class="navbar-nav">
                                                    <a class="nav-link active" aria-current="page" href="./">Home</a>
                                                    <a class="nav-link" href="./whoami">Who am I?</a>
                                                    <a class="nav-link" href="./source_code">Source code</a>
                                                </div>
                                            </div>
                                        </div>
                                    </nav>
                                    <br>
                                    <br>
                                    <br>
                                    <h3><center>Oops, something went wrong...</center></h3>
                                    <br>
                                    <br>
                                    <p><center>String generator parameters you've entered are not valid</center></p>
                                    <br>
                                    <div class="wrapper flex-grow-1"></div>
                                    <div class="b-example-divider"></div>
                                        <div class="container">
                                          <footer class="d-flex flex-wrap justify-content-between align-items-center py-3 my-4 border-top">
                                            <div class="col-md-4 d-flex align-items-center">
                                              <a href="/" class="mb-3 me-2 mb-md-0 text-muted text-decoration-none lh-1">
                                                <svg class="bi" width="30" height="24"><use xlink:href="#bootstrap"/></svg>
                                              </a>
                                              <span class="text-muted">&copy; 2022 Andrii Ocheretko</span>
                                            </div>
                                            <ul class="nav col-md-4 justify-content-end list-unstyled d-flex">
                                                <li class="ms-3"><a class="text-muted" href="https://twitter.com/AndriiOcheretko"><svg class="bi" width="24" height="24"><use xlink:href="#twitter"/></svg></a></li>
                                            </ul>
                                          </footer>
                                        </div>
                                </body>
                            </html>'''))

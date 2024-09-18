from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST' and request.headers.get('NotBad')  == 'true':
        return 'ReallyNotBad'
    else:
        return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)

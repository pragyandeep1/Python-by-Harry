# Explore the flask module and create a web server using flask and python

from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return 'Helo guts'
    if __name__ is '__main__':
        app.run(debug=True)
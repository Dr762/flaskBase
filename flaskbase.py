##basic flask example
##we use some bootstrap for html but I believe any js shit can be used

__author__ = "alex"
__date__ = "$Sep 8, 2015 11:23:32 AM$"

from flask import Flask
from flask import request
from flask import make_response
from flask import redirect
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

##flask app instance
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@app.route('/browser')
def browser():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


@app.route('/cookie')
def get_response():
    response = make_response('<h1>We have a cookie for you</h1>');
    response.set_cookie('answer', '42')
    return response


@app.route('/redirect')
def redir():
    return redirect('http://ru.wikipedia.org')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == "__main__":
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    app.run(debug=True)

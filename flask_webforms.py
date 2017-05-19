## we do an app with web forms
## I had to leave moment for compatibilitywith base demo
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_moment import Moment
from flask import session
from flask import url_for
from flask import redirect
from flask import flash


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fffe16hff'


@app.route('/', methods=['GET', 'POST'])
def web_form():
    form = NameForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like the name has been changed')
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('web_form'))
    return render_template('webform.html', form=form, name=session.get('name'))


if __name__ == "__main__":
    moment = Moment(app)
    bootstrap = Bootstrap(app)
    app.run(debug=True)

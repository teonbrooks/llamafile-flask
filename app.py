from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from client import Client


app = Flask(__name__)
app.secret_key = 'tO$&!|0wkamvVia0?n$NqIRVWOG'


class TextForm(FlaskForm):
    text = StringField('Enter some text', validators=[DataRequired()])
    submit = SubmitField('Submit')



client = Client()


@app.route('/', methods=['GET', 'POST'])
def index():
    form = TextForm()  
    text = None
    if form.validate_on_submit():  
        if client:
            prompt = form.text.data  
            client.submit_prompt(prompt)
            response =client.get_response()
            return render_template('main.html', form=form, response=response.choices[0].message.content, prompt=prompt)
        else:
            return "Error connecting to other server"
    return render_template('main.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)



from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField
from wtform.validators import InputField, NumberRange, SubmitField

class HealthDataForm(FlaskForm):
    date = DateField('Date', format='%Y-%m-%d')
    exercise = IntegerField('Exercise (minutes)', validators=[InputField(), NumberRange(min=0)])
    meditation = IntegerField('Meditation (minutes)', validators=[InputField(), NumberRange(min=0)])
    sleep = IntegerField('Sleep (minutes)', validators=[InputField(), NumberRange(min=0)])
    submit = SubmitField('Submit')
from flask_wtf import FlaskForm
from wtforms.fields import (
    BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
)
from wtforms.validators import DataRequired, ValidationError

from wtforms.widgets.html5 import DateInput, TimeInput

validators = [DataRequired()]


class AppointmentForm(FlaskForm):
    name = StringField('Name', validators)
    start_date = DateField('Start date', validators, widget=DateInput())
    start_time = TimeField('Start time', validators, widget=TimeInput())
    end_date = DateField('End date', validators, widget=DateInput())
    end_time = TimeField('End time', validators, widget=TimeInput())
    description = TextAreaField('Description', validators)
    private = BooleanField('Private?')
    submit = SubmitField('Create an appointment')

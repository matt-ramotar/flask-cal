from flask_wtf import FlaskForm
from wtforms.fields import BooleanField, DateField, StringField, SubmitField, TextAreaField, TimeField
from wtforms.validators import DataRequired, ValidationError
from wtforms.widgets.html5 import DateInput, TimeInput
from datetime import datetime

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

    def validate_end_date(form, field):
        start = datetime.combine(form.start_date.data, form.start_time.data)
        end = datetime.combine(form.end_date.data, form.end_time.data)
        if start >= end:
            raise ValidationError(
                'End date/time must come after start date/time')
        if form.start_date.data != form.end_date.data:
            raise ValidationError('End date must be the same as start date')

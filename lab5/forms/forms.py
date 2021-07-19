from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    username = DecimalField('Username', validators=[DataRequired()])
    first_name = DecimalField('First Name', validators=[DataRequired()])
    last_name = DecimalField('Last Name', validators=[DataRequired()])
    prog_lang = DecimalField('Programming Language', validators=[DataRequired()])
    experience_yr = DecimalField('Years of Experience', validators=[DataRequired()])
    age = DecimalField('Age', validators=[DataRequired()])
    hw1_hours = DecimalField('HW1 hours', validators=[DataRequired()])
    # proptype = StringField('proptype', validators=[DataRequired()])
    #Uncomment the next line for Grad student homework
    #model = ???
    submit = SubmitField('Add')
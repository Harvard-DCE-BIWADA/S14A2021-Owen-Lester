from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    beds = DecimalField('Beds', default=4, validators=[DataRequired()])
    baths = DecimalField('Baths', default=2.5, validators=[DataRequired()])
    sqft = DecimalField('Sq. feet', default=3005, validators=[DataRequired()])
    age = DecimalField('Age', default=15, validators=[DataRequired()])
    lotsize = DecimalField('Lot size', default=1793, validators=[DataRequired()])
    garage = DecimalField('Garage', default=1, validators=[DataRequired()])
    # proptype = StringField('proptype', validators=[DataRequired()])
    #Uncomment the next line for Grad student homework
    #model = ???
    submit = SubmitField('Predict')
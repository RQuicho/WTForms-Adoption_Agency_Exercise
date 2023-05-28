from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField
from wtforms.validators import InputRequired

class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank.")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank")])
    photo = StringField("Photo URL")
    age = IntegerField("Age")
    notes = StringField("Notes")


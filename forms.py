from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField, ValidationError, TextAreaField
from wtforms.validators import InputRequired, URL, Optional

def valid_species(form, field):
    """Checks if species input is within allowed species lsit"""
    if field.data not in ["Donkey", "Pig", "Kangaroo", "Rabbit", "Owl", "Tiger", "Bear"]:
        raise ValidationError('Species should be capitalized and must be valid species in 100-acre-woods')

def valid_age(form, field):
    """Checks if age is between 0 and 30"""
    if int(field.data) <= 0 or int(field.data) >= 30:
        raise ValidationError('Age must be between 0 and 30')


class AddPetForm(FlaskForm):
    """Form for adding pets"""

    name = StringField("Pet Name", validators=[InputRequired(message="Pet Name can't be blank.")])
    species = StringField("Species", validators=[InputRequired(message="Species can't be blank"), valid_species])
    photo_url = StringField("Photo URL", validators=[URL(message="Must be valid URL"), Optional()])
    age = IntegerField("Age", validators=[Optional(), valid_age])
    notes = TextAreaField("Notes", validators=[Optional()])

class EditPetForm(FlaskForm):
    """Form for edting pets"""
    photo_url = StringField("Photo URL", validators=[URL(message="Must be valid URL"), Optional()])
    notes = TextAreaField("Notes", validators=[Optional()])
    available = BooleanField("Available")

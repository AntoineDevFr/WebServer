# This file is part of PyFlaSQL.
# Original author: Raphael Viera (raphael.viera@emse.fr)
# Contribution : ISMIN student X (ismin.student@etu.emse.fr)
# License: check the LICENSE file.
"""
Create forms to be passed to the frontend
"""
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Email, InputRequired, Length, ValidationError, NumberRange
from flask_wtf.file import FileField, FileAllowed, FileRequired

class FileUploadForm(FlaskForm):
    image = FileField('Image', validators=[
        InputRequired(), 
        #FileAllowed(['jpg', 'jpeg', 'png', 'gif', 'php'], 'Only JPEG, PNG, and GIF images are allowed.')
        ])
    submit = SubmitField('Upload')
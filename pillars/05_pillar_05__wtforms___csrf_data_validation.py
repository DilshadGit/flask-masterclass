"""
Pillar 05: WTForms & CSRF Data Validation
File: app/forms.py
"""

from flask_wtf import FlaskForm\nfrom wtforms import StringField, PasswordField, SubmitField\nfrom wtforms.validators import DataRequired, Email, Length\n\nclass LoginForm(FlaskForm):\n    email = StringField('Email', validators=[DataRequired(), Email()])\n    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

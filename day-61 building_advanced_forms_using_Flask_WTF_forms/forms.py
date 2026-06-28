from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileSize
from wtforms import (
    StringField, EmailField, PasswordField,
    SelectField, BooleanField, TextAreaField, SubmitField
)
from wtforms.validators import (
    DataRequired, Email, Length, EqualTo,
    Regexp, ValidationError
)

BLOCKED_USERNAMES = ['admin', 'root', 'superuser']

class RegistrationForm(FlaskForm):

    # --- Basic Fields ---
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=25, message="Must be 3–25 characters"),
        Regexp(r'^\w+$', message="Only letters, numbers, and underscores")
    ])

    email = EmailField('Email Address', validators=[
        DataRequired(),
        Email(message="Enter a valid email")
    ])

    # --- Password Fields ---
    password = PasswordField('Password', validators=[
        DataRequired(),
        Length(min=8, message="At least 8 characters required")
    ])

    confirm_password = PasswordField('Confirm Password', validators=[
        DataRequired(),
        EqualTo('password', message="Passwords must match")
    ])

    # --- Select / Dropdown ---
    role = SelectField('Account Type', choices=[
        ('', '-- Select --'),
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('other', 'Other')
    ], validators=[DataRequired(message="Please select a role")])

    # --- Textarea ---
    bio = TextAreaField('Short Bio', validators=[
        Length(max=300, message="Max 300 characters")
    ])

    # --- File Upload ---
    avatar = FileField('Profile Picture', validators=[
        FileAllowed(['jpg', 'jpeg', 'png'], 'Images only (jpg, png)'),
        FileSize(max_size=2 * 1024 * 1024, message="Max file size is 2MB")
    ])

    # --- Checkbox ---
    agree = BooleanField('I agree to the Terms & Conditions', validators=[
        DataRequired(message="You must agree to continue")
    ])

    submit = SubmitField('Create Account')

    # ✅ Custom Validator — method name must be validate_<fieldname>
    def validate_username(self, username):
        if username.data.lower() in BLOCKED_USERNAMES:
            raise ValidationError(f'"{username.data}" is a reserved username.')
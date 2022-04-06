from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email , EqualTo


class Hypervisor(FlaskForm):
    hypervisorType = SelectField('HypervisorType', choices=["Proxmox", "VMware", "Hyper-V"])
    brand = SelectField('Server_Brand', choices=['HP', 'LENOVO', 'DELL'])
    model = SelectField()


class Servers(FlaskForm):
    serverName = StringField('Server_Name', validators=[DataRequired(), Length(min=2, max=20)])
    ipAddress = StringField('IP_AddrV4', validators=[DataRequired(), Length(min=15)])


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

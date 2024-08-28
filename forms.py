from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, NumberRange, Length, Email, EqualTo

class ProductForm(FlaskForm):
    category = StringField('Categoría', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    price = IntegerField('Precio', validators=[DataRequired(), NumberRange(min=0)])
    photo = StringField('Foto (URL)', validators=[DataRequired()])
    submit = SubmitField('Agregar Producto')

class RegistrationForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=20)])
    first_name = StringField('Nombre', validators=[DataRequired(), Length(min=3, max=20)])
    last_name = StringField('Apellido', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirma tu Contraseña', validators=[DataRequired(), EqualTo('password', message='Las contraseñas deben coincidir')])
    submit = SubmitField('Registrar')

class LoginForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    submit = SubmitField('Iniciar Sesión')
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class ProductForm(FlaskForm):
    category = StringField('Categoría', validators=[DataRequired()])
    name = StringField('Nombre', validators=[DataRequired()])
    description = TextAreaField('Descripción', validators=[DataRequired()])
    price = IntegerField('Precio', validators=[DataRequired(), NumberRange(min=0)])
    photo = StringField('Foto (URL)', validators=[DataRequired()])
    submit = SubmitField('Agregar Producto')

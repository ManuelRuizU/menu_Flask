from flask import render_template, redirect, url_for, flash
from forms import ProductForm, RegistrationForm, LoginForm
from services.services import save_product_to_json, load_products, save_user, authenticate_user 

def add_product():
    form = ProductForm()
    promociones, otras_categorias = load_products()
    if form.validate_on_submit():
        # Obtener datos del formulario
        category = form.category.data
        name = form.name.data
        description = form.description.data
        price = form.price.data
        photo = form.photo.data

        # Llamar al servicio para guardar el producto
        save_product_to_json(category, name, description, price, photo)

        return redirect(url_for('main.index'))

    return render_template('add_product.html', form=form, promociones=promociones, otras_categorias=otras_categorias)

def index():
    promociones, otras_categorias = load_products()
    return render_template('index.html', promociones=promociones, otras_categorias=otras_categorias)

def register_view():
    form = RegistrationForm()
    promociones, otras_categorias = load_products()
    if form.validate_on_submit():
        save_user(form.username.data, form.password.data)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('auth_bp.login_view'))
    return render_template('register.html', form=form, promociones=promociones, otras_categorias=otras_categorias)

def login_view():
    form = LoginForm()
    promociones, otras_categorias = load_products()
    if form.validate_on_submit():
        if authenticate_user(form.username.data, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Login unsuccessful. Please check your email and password.', 'danger')
    return render_template('login.html', form=form, promociones=promociones, otras_categorias=otras_categorias)

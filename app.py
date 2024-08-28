from flask import Flask, render_template, request, redirect, url_for
from forms import ProductForm
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Necesario para Flask-WTF


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    form = ProductForm()
    if form.validate_on_submit():
        category = form.category.data
        name = form.name.data
        description = form.description.data
        price = form.price.data
        photo = form.photo.data

        # Cargar datos existentes
        with open('static/json/productos.json', 'r') as file:
            data = json.load(file)

        # Agregar el nuevo producto al JSON
        if category not in data['promociones']:
            data['promociones'][category] = {}

        new_id = max([item['id'] for sublist in data['promociones'].values() for item in sublist.values()] + [0]) + 1
        data['promociones'][category][f"{new_id}_{name.replace(' ', '_')}"] = {
            'id': new_id,
            'nombre': name,
            'descripcion': description,
            'precio': price,
            'foto': photo
        }

        # Guardar datos actualizados
        with open('static/json/productos.json', 'w') as file:
            json.dump(data, file, indent=4)

        return redirect(url_for('index'))

    return render_template('add_product.html', form=form)


@app.route('/')
def index():
    # Ruta al archivo JSON
    json_path = os.path.join(app.root_path, 'static', 'json', 'productos.json')
    
    # Leer el archivo JSON
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filtrar categorías que comienzan con "Promociones"
    promociones = {key: value for key, value in data['promociones'].items() if key.lower().startswith('promociones')}
    
    # Filtrar otras categorías fuera de "Promociones"
    otras_categorias = {key: value for key, value in data['promociones'].items() if not key.lower().startswith('promociones')}
    
    # Añadir las categorías "Extras" y "Bebidas"
    if 'Extras' in data['promociones']:
        otras_categorias['Extras'] = data['promociones']['Extras']
    if 'Bebidas' in data['promociones']:
        otras_categorias['Bebidas'] = data['promociones']['Bebidas']

    return render_template('index.html', promociones=promociones, otras_categorias=otras_categorias)

if __name__ == '__main__':
    app.run(debug=True)

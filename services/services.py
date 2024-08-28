# /services/services.py
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

# Definir las rutas a los archivos JSON
PRODUCTS_FILE = os.path.join(os.getcwd(), 'data', 'productos.json')
USERS_FILE = os.path.join(os.getcwd(), 'data', 'user.json')


def load_products():
    # Leer el archivo JSON de productos
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Filtrar categorías que comienzan con "Promociones"
    promociones = {key: value for key, value in data['promociones'].items() if key.lower().startswith('promociones')}
    
    # Filtrar otras categorías fuera de "Promociones"
    otras_categorias = {key: value for key, value in data['promociones'].items() if not key.lower().startswith('promociones')}
    
    # Añadir las categorías "Extras" y "Bebidas" si existen
    if 'Extras' in data['promociones']:
        otras_categorias['Extras'] = data['promociones']['Extras']
    if 'Bebidas' in data['promociones']:
        otras_categorias['Bebidas'] = data['promociones']['Bebidas']

    return promociones, otras_categorias


def save_product_to_json(category, name, description, price, photo):
    # Cargar datos existentes del archivo JSON de productos
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Agregar el nuevo producto al JSON
    if category not in data['promociones']:
        data['promociones'][category] = {}

    # Generar un nuevo ID para el producto
    new_id = max([item['id'] for sublist in data['promociones'].values() for item in sublist.values()] + [0]) + 1
    data['promociones'][category][f"{new_id}_{name.replace(' ', '_')}"] = {
        'id': new_id,
        'nombre': name,
        'descripcion': description,
        'precio': price,
        'foto': photo
    }

    # Guardar los datos actualizados en el archivo JSON de productos
    with open(PRODUCTS_FILE, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)


def save_user(email, password):
    # Generar un hash de la contraseña
    hashed_password = generate_password_hash(password)
    user_data = {'email': email, 'password': hashed_password}

    try:
        # Intentar cargar los usuarios existentes desde el archivo JSON de usuarios
        with open(USERS_FILE, 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, inicializar una lista vacía de usuarios
        users = []

    # Agregar el nuevo usuario a la lista
    users.append(user_data)

    # Guardar los usuarios actualizados en el archivo JSON de usuarios
    with open(USERS_FILE, 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=4)


def authenticate_user(email, password):
    try:
        # Cargar los usuarios desde el archivo JSON de usuarios
        with open(USERS_FILE, 'r', encoding='utf-8') as file:
            users = json.load(file)
    except FileNotFoundError:
        # Si el archivo no existe, devolver False (no autenticado)
        return False

    # Verificar si el usuario proporcionado existe y la contraseña coincide
    for user in users:
        if user['email'] == email and check_password_hash(user['password'], password):
            return True

    return False

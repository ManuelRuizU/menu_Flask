# app.py
from flask import Flask
from routes.urls import main, auth_bp
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Asegúrate de usar una clave secreta segura

# Habilitar la protección CSRF
csrf = CSRFProtect(app)

app.register_blueprint(main)
app.register_blueprint(auth_bp)

if __name__ == '__main__':
    app.run(debug=True)


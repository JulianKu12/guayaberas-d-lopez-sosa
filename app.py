from flask import Flask, render_template
import os

# Configuración inicial de la aplicación Flask
app = Flask(__name__)

# --- AQUÍ VA EL CÓDIGO DE CONEXIÓN MODERNO ---

# 2. Configuración dinámica (Detecta si es Railway o tu PC)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('postgresql://postgres:RAkPXKAEitHxwPOrEgVGEpkeJVJKQQGE@postgres.railway.internal:5432/railway', 'sqlite:///catalogo.db')

# 3. Parche de compatibilidad para PostgreSQL
uri = app.config['SQLALCHEMY_DATABASE_URI']
if uri and uri.startswith("postgres://"):
    app.config['SQLALCHEMY_DATABASE_URI'] = uri.replace("postgres://", "postgresql://", 1)

# --- FIN DEL BLOQUE DE CONEXIÓN ---

@app.context_processor
def inject_brand():
    return {'brand_name': 'Guayaberas D´ López Sosa'}

# Catálogo Curado de 21 Modelos de Alta Gama
PRODUCTOS = [
    {
        "id": 1,
        "nombre": "Modelo Bambú 01",
        "sku": "mod-bambu_01",
        "precio": 460.0,
        "material": "Lino Murano",
        "color": "Blanco",
        "imagen": "modelo_bambu_01.jpg"
    },
    {
        "id": 2,
        "nombre": "Modelo Esteban",
        "sku": "mod-esteban",
        "precio": 480.0,
        "material": "Lino Look",
        "color": "Hueso",
        "imagen": "modelo_esteban.jpg"
    },
    {
        "id": 3,
        "nombre": "Modelo Presidencial Enrique",
        "sku": "mod-presidencial-enrique",
        "precio": 490.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_presidencial_enrique.jpg"
    },
    {
        "id": 4,
        "nombre": "Modelo Palmas",
        "sku": "mod-palmas",
        "precio": 570.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_palmas.jpg"
    },
    {
        "id": 5,
        "nombre": "Modelo Calabaza 01",
        "sku": "mod-calabaza-01",
        "precio": 540.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_calabaza_01.jpg"
    },
    {
        "id": 6,
        "nombre": "Modelo César",
        "sku": "mod-cesar",
        "precio": 530.0,
        "material": "Lino Look",
        "color": "Blanco Jaspeado",
        "imagen": "modelo_cesar.jpg"
    },
    {
        "id": 7,
        "nombre": "Modelo Colibrí 01",
        "sku": "mod-colibri-01",
        "precio": 530.0,
        "material": "Lino Look",
        "color": "Fucsia",
        "imagen": "modelo_colibri_01.jpg"
    },
    {
        "id": 8,
        "nombre": "Modelo Elegante",
        "sku": "mod-elegante",
        "precio": 540.0,
        "material": "Lino Lino Amalfi",
        "color": "Verde Menta",
        "imagen": "modelo_elegante.jpg"
    },
    {
        "id": 9,
        "nombre": "Modelo Esencial",
        "sku": "mod-esencial",
        "precio": 540.0,
        "material": "Lino Amalfi",
        "color": "Negro",
        "imagen": "modelo_esencial.jpg"
    },
    {
        "id": 10,
        "nombre": "Modelo Edgar",
        "sku": "mod-edgar",
        "precio": 590.0,
        "material": "Lino Amalfi",
        "color": "Negro",
        "imagen": "modelo_edgar.jpg"
    },
    {
        "id": 11,
        "nombre": "Modelo Sol 02",
        "sku": "mod-sol-02",
        "precio": 570.0,
        "material": "Lino Amalfi",
        "color": "Azul Marino",
        "imagen": "modelo_sol_02.jpg"
    },
    {
        "id": 12,
        "nombre": "Modelo Cuyo",
        "sku": "mod-cuyo",
        "precio": 540.0,
        "material": "Lino Amalfi",
        "color": "Azul Marino",
        "imagen": "modelo_cuyo.jpg"
    },
    {
        "id": 13,
        "nombre": "Modelo Panal 06",
        "sku": "mod_panal_06",
        "precio": 600.0,
        "material": "Lino Amalfi",
        "color": "Azul Cielo",
        "imagen": "modelo_panal_06.jpg"
    },
    {
        "id": 14,
        "nombre": "Modelo Domingo",
        "sku": "mod_domingo",
        "precio": 560.0,
        "material": "Lino Look",
        "color": "Fucsia",
        "imagen": "modelo_domingo.jpg"
    },
    {
        "id": 15,
        "nombre": "Modelo Presidencial Felipe 01",
        "sku": "mod_presidencial_felipe_01",
        "precio": 540.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_presidencial_felipe_01.jpg"
    },
    {
        "id": 16,
        "nombre": "Modelo Presidencial Cruz",
        "sku": "mod_presidencial_cruz",
        "precio": 540.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_presidencial_cruz.jpg"
    },
    {
        "id": 17,
        "nombre": "Modelo Bryan 01",
        "sku": "mod_bryan_01",
        "precio": 585.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_bryan_01.jpg"
    },
    {
        "id": 18,
        "nombre": "Modelo Arcoíris",
        "sku": "mod_arcoiris",
        "precio": 480.0,
        "material": "Lino Look",
        "color": "Hueso",
        "imagen": "modelo_arcoiris.jpg"
    },
    {
        "id": 19,
        "nombre": "Modelo Alfredo",
        "sku": "mod_alfredo",
        "precio": 560.0,
        "material": "Lino Look",
        "color": "Gris Bajo",
        "imagen": "modelo_alfredo.jpg"
    },
    {
        "id": 20,
        "nombre": "Modelo Edgar 06",
        "sku": "mod_edgar_06",
        "precio": 535.0,
        "material": "Lino Amalfi",
        "color": "Azul Cielo",
        "imagen": "modelo_edgar_06.jpg"
    },
    {
        "id": 21,
        "nombre": "Modelo Uriel 01",
        "sku": "mod_uriel_01",
        "precio": 570.0,
        "material": "Lino Amalfi",
        "color": "Blanco",
        "imagen": "modelo_uriel_01.jpg"
    }
]

@app.route('/')
def home():
    return render_template('pages/index.html', productos=PRODUCTOS)

@app.route('/producto/<int:id>')
def producto(id):
    producto_encontrado = next((p for p in PRODUCTOS if p['id'] == id), None)
    if producto_encontrado:
        return render_template('pages/detalle.html', producto=producto_encontrado)
    return render_template('pages/404.html'), 404

@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404

if __name__ == '__main__':
    # Esto solo se activa cuando lo corres tú localmente
    app.run(debug=False, port=8080)

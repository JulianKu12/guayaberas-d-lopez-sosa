# Plan de Actualización: Catálogo de Lujo (7 Modelos PNG)

Este plan describe la transición a un catálogo curado de 7 guayaberas de alta gama con imágenes PNG.

## Cambios en el Código

### 1. Actualizar `app.py`
Se reemplazará la consulta a la base de datos por una lista de diccionarios que representen los 7 modelos de lujo.
- Nombres: Lino Presidencial, Yucateca de Gala, Seda de Izamal, Algodón Maya Real, Lino del Golfo, Gala Peninsular, Elegancia Meridiana.
- Imágenes: `guayabera_1.png` a `guayabera_7.png`.

### 2. Actualizar `templates/pages/index.html`
Se modificará el bucle de productos para que sea compatible con la nueva estructura de datos.
- Bucle: `{% for producto in productos %}`.
- Ruta de imagen: `{{ url_for('static', filename='assets/img/' + producto.imagen) }}`.

### 3. Refinar `static/css/main.css`
Se mejorará la presentación visual de las tarjetas de producto.
- Grid: `grid-template-columns: repeat(auto-fit, minmax(320px, 1fr))`.
- Imágenes: `aspect-ratio: 4/5`, `object-fit: cover`, `border: 2px solid #3E2723`, `border-radius: 4px`.

## Pasos de Verificación
1. Iniciar la aplicación Flask.
2. Navegar a la página de inicio.
3. Validar la carga de las 7 imágenes PNG.
4. Verificar el diseño responsivo del catálogo.

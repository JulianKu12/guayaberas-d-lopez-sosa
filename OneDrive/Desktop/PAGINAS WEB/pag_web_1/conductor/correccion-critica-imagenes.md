# Plan de Corrección Crítica: Carga de Imágenes PNG y Estructura de Datos

Este plan describe las correcciones de ingeniería para solucionar los errores de carga de imágenes en el catálogo de 7 modelos de lujo.

## Cambios en el Código

### 1. Actualizar `app.py`
Limpieza de la clave `imagen` en la lista de productos estáticos para que solo contenga el nombre del archivo.

### 2. Corrección en `templates/pages/index.html` y `detalle.html`
Se utilizará la sintaxis exacta de `url_for` que requiere Flask para buscar en la carpeta correcta:
- `src="{{ url_for('static', filename='assets/img/' + producto.imagen) }}"`

Se incluirá un manejador de error para depuración en consola:
- `onerror="console.log('Error cargando: ' + this.src)"`

### 3. CSS de Respaldo en `static/css/main.css`
Se añadirán propiedades a las imágenes para que, en caso de fallo, el diseño no se rompa:
- `min-height: 300px;`
- `background-color: #E5E5E5;`

## Pasos de Verificación
1. Verificar que el servidor Flask inicia correctamente.
2. Comprobar la carga de imágenes en el Home y en la página de Detalle.
3. Inspeccionar la consola del navegador para descartar rutas erróneas.

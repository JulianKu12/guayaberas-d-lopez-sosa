/**
 * Lógica principal del Frontend para Guayaberas Élite.
 * Maneja el cursor personalizado, efectos de lupa, preloader y envío a WhatsApp.
 */

document.addEventListener('DOMContentLoaded', () => {
    // Referencias a elementos clave del DOM
    const introScreen = document.getElementById('intro-screen');
    const mainContent = document.getElementById('main-content');
    const customCursor = document.getElementById('custom-cursor');
    
    /* --- LÓGICA DEL CURSOR PERSONALIZADO Y EFECTO LUPA --- */
    if (customCursor) {
        let isZooming = false;
        let currentImg = null;

        // Movimiento del cursor personalizado siguiendo el ratón
        document.addEventListener('mousemove', (e) => {
            const x = e.clientX;
            const y = e.clientY;

            // Uso de requestAnimationFrame para un movimiento suave y optimizado
            requestAnimationFrame(() => {
                customCursor.style.left = `${x}px`;
                customCursor.style.top = `${y}px`;

                // Si el ratón está sobre una imagen (modo lupa)
                if (isZooming && currentImg) {
                    const rect = currentImg.getBoundingClientRect();
                    
                    // Cálculo de la posición relativa del ratón dentro de la imagen (porcentaje)
                    const relX = ((x - rect.left) / rect.width) * 100;
                    const relY = ((y - rect.top) / rect.height) * 100;

                    // Ajuste de la posición del fondo para crear el efecto de "zoom" en el cursor
                    customCursor.style.backgroundPosition = `${relX}% ${relY}%`;
                }
            });
        });

        // Selección de todas las imágenes que deben tener efecto de lupa
        const zoomContainers = document.querySelectorAll('.product-image-wrapper img, .main-image img, .sec-img-wrapper img');
        
        zoomContainers.forEach(img => {
            // Al entrar en la imagen, activamos el modo lupa
            img.addEventListener('mouseenter', (e) => {
                isZooming = true;
                currentImg = e.target;
                customCursor.classList.add('hover-product');
                
                // Cargamos la misma imagen en el cursor para el efecto de aumento
                customCursor.style.backgroundImage = `url(${currentImg.src})`;
                // Escalamiento del fondo para simular un zoom de 2.5x
                customCursor.style.backgroundSize = `${currentImg.offsetWidth * 2.5}px auto`;
            });

            // Al salir de la imagen, desactivamos el modo lupa
            img.addEventListener('mouseleave', () => {
                isZooming = false;
                currentImg = null;
                customCursor.classList.remove('hover-product');
                customCursor.style.backgroundImage = 'none';
            });
        });

        // Efectos visuales del cursor al pasar sobre elementos interactivos (botones/enlaces)
        const links = document.querySelectorAll('a, button, .btn, .size-btn, .thumb-item');
        links.forEach(link => {
            link.addEventListener('mouseenter', () => customCursor.classList.add('hover-link'));
            link.addEventListener('mouseleave', () => customCursor.classList.remove('hover-link'));
        });
    }

    /* --- TRANSICIÓN DEL PRELOADER (PANTALLA DE CARGA) --- */
    const startLuxuryTransition = () => {
        // Desvanecimiento de la pantalla de carga
        if (introScreen) introScreen.classList.add('fade-out');
        // Visualización del contenido principal con un ligero retraso
        if (mainContent) {
            mainContent.style.display = 'block';
            setTimeout(() => mainContent.classList.add('show'), 100);
        }
        // Restauración del scroll del cuerpo
        document.body.style.overflow = 'auto';
    };

    // La transición comienza después de 3.5 segundos para mostrar la marca
    setTimeout(startLuxuryTransition, 3500);

    /* --- INICIALIZACIÓN DE SCROLL SUAVE (LENIS) --- */
    const initLenis = () => {
        if (typeof Lenis !== 'undefined') {
            const lenis = new Lenis({
                duration: 1.2,
                easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            });
            // Bucle de animación para el scroll suave
            function raf(time) {
                lenis.raf(time);
                requestAnimationFrame(raf);
            }
            requestAnimationFrame(raf);
        }
    };

    // Se inicializa después de que el preloader ha desaparecido
    setTimeout(initLenis, 4700);
});

/**
 * Función para recopilar datos de personalización y enviarlos por WhatsApp.
 * Se ejecuta al hacer clic en el botón de consulta.
 */
function enviarWhatsApp() {
    const configurador = document.querySelector('.configurador-sastreria');
    const nombreProducto = configurador.getAttribute('data-producto');
    
    // Captura de valores seleccionados en los menús desplegables
    const tela = document.getElementById('select-tela').value;
    const cuello = document.getElementById('select-cuello').value;
    const manga = document.getElementById('select-manga').value;
    const color = document.getElementById('color_personalizado').value || 'No especificado';
    const talla = document.getElementById('select-talla').value;

    // Construcción del mensaje personalizado
    const mensaje = `Hola! Me interesa personalizar el modelo ${nombreProducto} con Tela: ${tela}, Cuello: ${cuello}, Manga: ${manga}, Color: ${color} y Talla: ${talla}. ¿Tienen disponibilidad?`;
    
    // Codificación de la URL para WhatsApp con el mensaje
    const url = `https://wa.me/529994599995?text=${encodeURIComponent(mensaje)}`;

    // Apertura de la conversación en una nueva pestaña
    window.open(url, '_blank');
}

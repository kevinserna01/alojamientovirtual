# Carta de Cumpleaños Interactiva con FastHTML

Esta es una carta de cumpleaños interactiva y visualmente atractiva creada con [FastHTML](https://fastht.ml/).

## Características

- 🎂 Diseño atractivo y festivo con gradientes y animaciones
- 🎊 Efectos visuales como confeti y animaciones de corazón
- 💌 Mensajes personalizados al hacer clic en los botones
- 🌸 Flores animadas y elementos decorativos
- 🌈 Diseño responsivo para verse bien en cualquier dispositivo

## Personalización

Puedes personalizar varios aspectos de la carta modificando el archivo `main.py`:

- **Texto principal**: Modifica el texto dentro de las etiquetas `P(...)` para personalizar el mensaje
- **Estilos**: Cambia los colores del gradiente de fondo y otros estilos en la variable `estilos`
- **Mensajes interactivos**: Cambia los mensajes que aparecen al hacer clic en los botones, modificando el parámetro en la función `mostrarMensaje(...)`
- **Imágenes**: Puedes agregar imágenes personalizadas si lo deseas

## Cómo ejecutar

Sigue estos pasos para ejecutar la carta de cumpleaños:

1. Asegúrate de tener instalado Python 3.7 o superior
2. Instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

3. Inicia el servidor de desarrollo:

```bash
python main.py
```

4. Abre tu navegador web y visita: http://0.0.0.0:5001

## Cómo compartir tu carta

Para compartir tu carta con esa persona especial, puedes:

1. Desplegarla con Vercel siguiendo las instrucciones del proyecto original:

```bash
npm install -g vercel
vercel --prod
```

2. O simplemente mostrar la aplicación localmente si están juntos durante la sorpresa

## Personalización avanzada

Si quieres hacer cambios más avanzados:

- **Agregar música**: Puedes agregar un elemento de audio HTML para reproducir música de fondo
- **Más animaciones**: Explora bibliotecas como [animate.css](https://animate.style/) para agregar más efectos
- **Agregar imágenes**: Crea una carpeta `public` y coloca allí imágenes que puedas mostrar en tu carta

## Notas

Este proyecto está basado en el boilerplate de FastHTML, un framework web de Python moderno y eficiente. Para más información sobre FastHTML, visita su [documentación oficial](https://docs.fastht.ml/).

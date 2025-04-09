from fasthtml.common import *
import os
from starlette.responses import FileResponse

app, rt = fast_app(hdrs=(picolink))

def serve_static(path):
    file_path = os.path.join(os.path.dirname(__file__), path)
    if os.path.exists(file_path):
        return FileResponse(file_path)
    return "File not found", 404

@rt("/static/<path:path>")
def static(path):
    return serve_static(f"public/static/{path}")

@rt("/")
def get():
    message = """Sí si, lo sé…
Tal vez para ti, tu cumpleaños no sea algo tan especial.
Pero para mí, sí lo es.

Hoy no quisiera dejar pasar la oportunidad de desearte un feliz cumpleaños.

Espero que este nuevo año de vida venga lleno de alegrías, sueños cumplidos y momentos inolvidables.

Que todos tus deseos se hagan realidad y que siempre conserves esa chispa tan especial que te caracteriza.

Con cariño,"""
    
    return (
        Head(
            Title("Feliz Cumpleaños"),
            Meta(name="description", content="Una carta de cumpleaños especial"),
            Style("""
                :root {
                  --primary-color: #ff85a2;
                  --secondary-color: #ffd5e5;
                  --accent-color: #ffb3c6;
                  --text-color: #4a4a4a;
                  --envelope-color: #fff0f5;
                  --envelope-shadow: #ffc0cb;
                  --paper-color: #fff;
                  --paper-shadow: rgba(0, 0, 0, 0.1);
                }
                
                body {
                  margin: 0;
                  padding: 0;
                  min-height: 100vh;
                  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                  color: var(--text-color);
                  overflow: hidden;
                }
                
                .animated-bg {
                  position: fixed;
                  top: 0;
                  left: 0;
                  width: 100%;
                  height: 100%;
                  background: linear-gradient(-45deg, #ffd5e5, #ffb3c6, #ff85a2, #ffb3c6);
                  background-size: 400% 400%;
                  animation: gradient 15s ease infinite;
                  z-index: -1;
                }
                
                .stars {
                  position: fixed;
                  top: 0;
                  left: 0;
                  width: 100%;
                  height: 100%;
                  z-index: -1;
                  overflow: hidden;
                }
                
                .star {
                  position: absolute;
                  background-color: white;
                  border-radius: 50%;
                  opacity: 0;
                  animation: twinkle 5s infinite;
                }
                
                .container {
                  display: flex;
                  flex-direction: column;
                  justify-content: center;
                  align-items: center;
                  min-height: 100vh;
                  padding: 1rem;
                  position: relative;
                  overflow: visible;
                }
                
                .envelope-container {
                  perspective: 1000px;
                  margin-bottom: 1rem;
                  position: fixed;
                  top: 45%;
                  left: 50%;
                  transform: translate(-50%, -50%);
                  z-index: 1;
                }
                
                .envelope {
                  position: relative;
                  width: 300px;
                  height: 200px;
                  background-color: var(--envelope-color);
                  border-radius: 5px;
                  box-shadow: 0 10px 25px var(--envelope-shadow);
                  cursor: pointer;
                  transform-style: preserve-3d;
                  transition: all 1s ease;
                }
                
                .envelope.open {
                  transform: rotateX(180deg) translateY(-100px);
                }
                
                .envelope-front {
                  position: absolute;
                  width: 100%;
                  height: 100%;
                  backface-visibility: hidden;
                  display: flex;
                  justify-content: center;
                  align-items: center;
                  border-radius: 5px;
                  overflow: hidden;
                }
                
                .envelope-back {
                  position: absolute;
                  width: 100%;
                  height: 100%;
                  backface-visibility: hidden;
                  transform: rotateX(180deg);
                  border-radius: 5px;
                  background-color: var(--envelope-color);
                  display: flex;
                  justify-content: center;
                  align-items: center;
                }
                
                .flap {
                  position: absolute;
                  top: 0;
                  width: 100%;
                  height: 100px;
                  background-color: var(--accent-color);
                  clip-path: polygon(0 0, 50% 50%, 100% 0);
                  z-index: 2;
                  transition: transform 0.5s ease;
                  transform-origin: top;
                }
                
                .envelope:hover .flap {
                  transform: rotateX(180deg);
                }
                
                .letter {
                  position: fixed;
                  top: 50%;
                  left: 50%;
                  transform: translate(-50%, 100vh);
                  opacity: 0;
                  transition: all 1s ease;
                  z-index: 3;
                  background-color: var(--paper-color);
                  padding: 1.5rem;
                  border-radius: 15px;
                  box-shadow: 0 10px 25px var(--paper-shadow);
                  max-width: 90vw;
                  width: 100%;
                  max-width: 600px;
                  max-height: 85vh;
                  overflow-y: auto;
                  display: flex;
                  flex-direction: column;
                  align-items: center;
                  background-image: 
                    linear-gradient(90deg, transparent 79px, #abced4 79px, #abced4 81px, transparent 81px),
                    linear-gradient(#eee .1em, transparent .1em);
                  background-size: 100% 1.5em;
                }
                
                .letter.show {
                  transform: translate(-50%, -50%);
                  opacity: 1;
                }
                
                .letter::-webkit-scrollbar {
                  width: 8px;
                }
                
                .letter::-webkit-scrollbar-track {
                  background: var(--paper-color);
                  border-radius: 4px;
                }
                
                .letter::-webkit-scrollbar-thumb {
                  background: var(--primary-color);
                  border-radius: 4px;
                }
                
                .message-container {
                  width: 100%;
                  padding: 0 0.5rem;
                }
                
                .message {
                  font-size: 1.2rem;
                  line-height: 1.6;
                  text-align: left;
                  margin-bottom: 1rem;
                  white-space: pre-wrap;
                  color: var(--text-color);
                  opacity: 0;
                  transform: translateY(20px);
                  transition: all 0.5s ease;
                  width: 100%;
                  padding: 0 0.5rem;
                  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                }
                
                .message.visible {
                  opacity: 1;
                  transform: translateY(0);
                }
                
                .signature {
                  text-align: right;
                  font-size: 1.3rem;
                  font-style: italic;
                  color: var(--primary-color);
                  margin-top: 0.5rem;
                  align-self: flex-end;
                  padding-right: 1rem;
                }
                
                .button {
                  display: inline-block;
                  padding: 0.75rem 1.5rem;
                  background-color: var(--primary-color);
                  color: white;
                  border: none;
                  border-radius: 50px;
                  font-size: 1rem;
                  cursor: pointer;
                  transition: all 0.3s ease;
                  text-decoration: none;
                  margin: 1rem 0;
                  align-self: center;
                }
                
                .button:hover {
                  background-color: var(--accent-color);
                  transform: translateY(-3px);
                  box-shadow: 0 5px 15px rgba(255, 133, 162, 0.4);
                }
                
                /* Animations */
                @keyframes gradient {
                  0% {
                    background-position: 0% 50%;
                  }
                  50% {
                    background-position: 100% 50%;
                  }
                  100% {
                    background-position: 0% 50%;
                  }
                }
                
                @keyframes twinkle {
                  0% { opacity: 0; }
                  50% { opacity: 0.8; }
                  100% { opacity: 0; }
                }
                
                @media (max-width: 768px) {
                  .envelope {
                    width: 250px;
                    height: 160px;
                  }
                  
                  .letter {
                    padding: 1rem;
                    max-height: 80vh;
                    max-width: 95vw;
                  }
                  
                  .message {
                    font-size: 1rem;
                    line-height: 1.4;
                    padding: 0;
                  }

                  .signature {
                    font-size: 1.1rem;
                    padding-right: 0.5rem;
                  }

                  .button {
                    padding: 0.5rem 1rem;
                    font-size: 0.9rem;
                    margin: 0.5rem 0;
                  }
                }

                @media (max-height: 600px) {
                  .envelope-container {
                    top: 40%;
                  }

                  .letter {
                    max-height: 90vh;
                    padding: 1rem;
                  }

                  .message {
                    font-size: 0.9rem;
                    line-height: 1.3;
                    margin-bottom: 0.5rem;
                  }

                  .signature {
                    margin-top: 0.25rem;
                  }

                  .button {
                    margin: 0.25rem 0;
                  }
                }

                /* Modal Styles */
                .modal {
                    display: none;
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    background-color: rgba(0, 0, 0, 0.8);
                    z-index: 1000;
                    opacity: 0;
                    transition: opacity 0.3s ease;
                }

                .modal.show {
                    display: flex;
                    opacity: 1;
                    justify-content: center;
                    align-items: center;
                }

                .modal-content {
                    background-color: var(--paper-color);
                    padding: 1rem;
                    border-radius: 15px;
                    position: relative;
                    max-width: 90vw;
                    max-height: 90vh;
                    transform: scale(0.7);
                    transition: transform 0.3s ease;
                    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
                }

                .modal.show .modal-content {
                    transform: scale(1);
                }

                .modal-close {
                    position: absolute;
                    top: -15px;
                    right: -15px;
                    width: 30px;
                    height: 30px;
                    background-color: var(--primary-color);
                    border: none;
                    border-radius: 50%;
                    color: white;
                    font-size: 1.2rem;
                    cursor: pointer;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
                }

                .modal-image {
                    max-width: 100%;
                    max-height: 80vh;
                    border-radius: 10px;
                }
            """),
        ),
        Body(
            Div(cls="animated-bg"),
            Div(cls="stars"),
            Div(
                id="youtube-player",
                style="""
                    position: fixed;
                    bottom: -1000px;
                    right: -1000px;
                    z-index: -1;
                    opacity: 0;
                    pointer-events: none;
                """
            ),
            Div(
                "🎵",
                id="btn-musica",
                style="""
                    position: fixed;
                    bottom: 20px;
                    right: 20px;
                    background: rgba(255,255,255,0.7);
                    padding: 10px;
                    border-radius: 50%;
                    cursor: pointer;
                    z-index: 100;
                """
            ),
            Div(
                Div(
                    Button("×", cls="modal-close"),
                    Img(src="../public/static/imagen_especial.png", cls="modal-image", alt="Imagen Especial"),
                    cls="modal-content"
                ),
                id="special-modal",
                cls="modal"
            ),
            Div(
                Div(
                    Div(
                        Div(
                            P("Click para abrir", style="color: white; text-align: center;"),
                            cls="envelope-front"
                        ),
                        Div(cls="flap"),
                        Div(cls="envelope-back"),
                        cls="envelope"
                    ),
                    cls="envelope-container"
                ),
                Div(
                    Div(
                        P(message, cls="message"),
                        cls="message-container"
                    ),
                    P("¿hamburguesa o pizza?", cls="signature"),
                    A("❤️ Gracias por ser especial", href="#", cls="button"),
                    cls="letter"
                ),
                cls="container"
            ),
            Script("""
                document.addEventListener('DOMContentLoaded', function() {
                  // Create stars
                  const starsContainer = document.querySelector('.stars');
                  const starCount = 100;
                  
                  for (let i = 0; i < starCount; i++) {
                    const star = document.createElement('div');
                    star.classList.add('star');
                    
                    // Random positions and sizes
                    const size = Math.random() * 3 + 1;
                    star.style.width = size + 'px';
                    star.style.height = size + 'px';
                    star.style.left = Math.random() * 100 + '%';
                    star.style.top = Math.random() * 100 + '%';
                    
                    // Random animation delay
                    star.style.animationDelay = Math.random() * 5 + 's';
                    
                    starsContainer.appendChild(star);
                  }
                  
                  // Envelope interaction
                  const envelope = document.querySelector('.envelope');
                  const letter = document.querySelector('.letter');
                  const messageElement = document.querySelector('.message');
                  
                  envelope.addEventListener('click', function() {
                    this.classList.toggle('open');
                    
                    // If envelope is open, show the letter
                    if (this.classList.contains('open')) {
                      setTimeout(() => {
                        letter.classList.add('show');
                        setTimeout(() => {
                          messageElement.classList.add('visible');
                        }, 500);
                      }, 800);
                    } else {
                      messageElement.classList.remove('visible');
                      letter.classList.remove('show');
                    }
                  });
                  
                  // Modal functionality
                  const modal = document.getElementById('special-modal');
                  const specialButton = document.querySelector('.button');
                  const closeButton = document.querySelector('.modal-close');
                  
                  specialButton.addEventListener('click', function(e) {
                    e.preventDefault();
                    modal.classList.add('show');
                  });
                  
                  closeButton.addEventListener('click', function() {
                    modal.classList.remove('show');
                  });
                  
                  modal.addEventListener('click', function(e) {
                    if (e.target === modal) {
                      modal.classList.remove('show');
                    }
                  });
                  
                  // Cerrar modal con la tecla Escape
                  document.addEventListener('keydown', function(e) {
                    if (e.key === 'Escape' && modal.classList.contains('show')) {
                      modal.classList.remove('show');
                    }
                  });
                  
                  // Música de fondo
                  const musicBtn = document.getElementById('btn-musica');
                  const youtubePlayer = document.getElementById('youtube-player');
                  let playerReady = false;
                  let playerActive = false;
                  
                  // Cargar la API de YouTube
                  function loadYouTubeAPI() {
                    if (!window.YT) {
                      const tag = document.createElement('script');
                      tag.src = 'https://www.youtube.com/iframe_api';
                      const firstScriptTag = document.getElementsByTagName('script')[0];
                      firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
                    }
                  }
                  
                  loadYouTubeAPI();
                  
                  // Función que se llama cuando la API está lista
                  window.onYouTubeIframeAPIReady = function() {
                    playerReady = true;
                    const player = new YT.Player('youtube-player', {
                      height: '1',
                      width: '1',
                      videoId: '2ucJrszbGCs',
                      playerVars: {
                        'playsinline': 1,
                        'controls': 0,
                        'autoplay': 0,
                        'mute': 0,
                        'disablekb': 1,
                        'fs': 0,
                        'modestbranding': 1,
                        'rel': 0
                      },
                      events: {
                        'onReady': onPlayerReady
                      }
                    });
                    
                    function onPlayerReady(event) {
                      // El reproductor está listo pero no comienza automáticamente
                    }
                  };
                  
                  function toggleMusica() {
                    if (playerReady) {
                      if (!playerActive) {
                        // Reproducir
                        const player = window.YT.get('youtube-player');
                        if (player) {
                          player.playVideo();
                        }
                        musicBtn.textContent = '🔊';
                        playerActive = true;
                      } else {
                        // Pausar
                        const player = window.YT.get('youtube-player');
                        if (player) {
                          player.pauseVideo();
                        }
                        musicBtn.textContent = '🎵';
                        playerActive = false;
                      }
                    }
                  }
                  
                  // Agregar el evento al botón de música
                  if (musicBtn) {
                    musicBtn.addEventListener('click', toggleMusica);
                  }
                });
            """),
        ),
    )

serve()

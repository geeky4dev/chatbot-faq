import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexión desde el frontend (CORS habilitado)

RESPUESTAS_FAQ_ORIGINAL = {
    "hola": "¡Hola! ¿En qué puedo ayudarte?",
    "qué es tu empresa": "Somos una empresa de ejemplo que usa IA.",
    "adiós": "¡Hasta luego!",
    "cómo estás": "Estoy bien, gracias por preguntar.",
    "cuál es tu propósito": "Mi propósito es ayudarte respondiendo preguntas frecuentes.",
    "qué tecnologías usas": "Uso tecnologías como Flask para el backend y React para el frontend.",
    "qué es Flask": "Flask es un framework web de Python utilizado para construir aplicaciones web."
}
RESPUESTAS_FAQ = {k.lower(): v for k, v in RESPUESTAS_FAQ_ORIGINAL.items()}

@app.route("/")
def index():
    return "Backend API está funcionando"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("message", "").strip().lower()  # La clave debe ser 'message' porque así envía el frontend
    print(f"Mensaje recibido (normalizado): '{mensaje}'")
    respuesta = RESPUESTAS_FAQ.get(mensaje, "Lo siento, no entendí tu pregunta.")
    return jsonify({"respuesta": respuesta})

# Ruta GET para probar que /chat está activa
@app.route("/chat", methods=["GET"])
def chat_get():
    return "Ruta /chat activa para GET", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # Puerto asignado por Render o 5001 local

    print("Rutas disponibles en Flask:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> métodos: {list(rule.methods)}")

    app.run(host="0.0.0.0", port=port)
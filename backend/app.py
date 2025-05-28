import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexión desde el frontend

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
    mensaje = data.get("mensaje", "").strip().lower()  # ✅ Clave corregida para que coincida con el frontend
    print(f"Mensaje recibido (normalizado): '{mensaje}'")
    respuesta = RESPUESTAS_FAQ.get(mensaje, "Lo siento, no entendí tu pregunta.")
    return jsonify({"respuesta": respuesta})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # Usa el puerto asignado por Render
    app.run(host="0.0.0.0", port=port)
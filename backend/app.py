import os
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Permite conexión desde el frontend (CORS habilitado)

RESPUESTAS_FAQ_ORIGINAL = {
    "hello": "Hello! How can I assist you today? I'm here to answer your questions.",
    "what does your company do?": "We are a sample company specializing in AI-based solutions to improve our users' experience.",
    "goodbye": "Goodbye! I hope I was helpful. Feel free to come back if you have more questions.",
    "how are you?": "I'm doing great, thank you for asking. How can I assist you today?",
    "what is your purpose?": "My purpose is to help you by providing clear and quick answers to frequently asked questions about our company and services.",
    "what technologies do you use?": "To provide you with an efficient experience, we use modern technologies: Flask as the backend framework to handle the logic and React on the frontend for an interactive and user-friendly interface.",
    "what is flask?": "Flask is a lightweight and flexible Python web framework that allows for easy and fast web application development. It's popular for creating APIs and web services.",
    "where are you located?": "Our main office is located in Montevideo, Uruguay, but we serve clients worldwide.",
    "how can I contact you?": "You can contact us by email at contact@company.com or call us at +598 1234 5678.",
    "what are your business hours?": "Our business hours are Monday to Friday, from 9:00 AM to 6:00 PM (GMT-3).",
    "do you offer technical support?": "Yes, we have a technical support team available to help you with any issues or inquiries.",
    "what services do you offer?": "We offer software development, AI consulting, and customized solutions tailored to your company’s needs.",
    "how can I hire your services?": "You can request a quote through our website or contact us directly to discuss your requirements.",
    "do you have any free plans?": "Currently, we do not offer free plans, but we provide demos and pilot trials to evaluate our solutions.",
    "do you accept credit card payments?": "Yes, we accept credit and debit card payments, as well as bank transfers.",
    "how long does a project take?": "The timeline varies depending on complexity, but typically an initial project takes between 4 and 8 weeks.",
    "what guarantees do you offer?": "We provide quality guarantees and post-sale support to ensure you are satisfied with our services.",
    "do you have discounts or promotions?": "From time to time, we launch special promotions. We recommend subscribing to our newsletter to stay informed.",
    "how do you protect my data?": "The privacy and security of your data are our top priorities. We comply with international data protection regulations.",
    "do you work with international companies?": "Yes, we have experience working with clients from different countries and adapting to their needs.",
    "what sets your company apart?": "We stand out by offering innovative solutions, personalized attention, and a team of experts in technology and AI."
}

RESPUESTAS_FAQ = {k.lower(): v for k, v in RESPUESTAS_FAQ_ORIGINAL.items()}

@app.route("/")
def index():
    return "Backend API is running"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    mensaje = data.get("message", "").strip().lower()  # La clave debe ser 'message' porque así envía el frontend
    print(f"Received message (normalized): '{mensaje}'")
    respuesta = RESPUESTAS_FAQ.get(mensaje, "Sorry, I didn't understand your question.")
    return jsonify({"respuesta": respuesta})

# Ruta GET para probar que /chat está activa
@app.route("/chat", methods=["GET"])
def chat_get():
    return "Route /chat is active for GET", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))  # Puerto asignado por Render o 5001 local

    print("Available Flask routes:")
    for rule in app.url_map.iter_rules():
        print(f"{rule} -> methods: {list(rule.methods)}")

    app.run(host="0.0.0.0", port=port)
import { useState } from 'react'

function App() {
  const [mensaje, setMensaje] = useState("")
  const [respuesta, setRespuesta] = useState("")
  const [showExamples, setShowExamples] = useState(true)

  const backendUrl = import.meta.env.VITE_BACKEND_URL

  const ejemplos = [
    "hello",
    "what does your company do?",
    "where are you located?",
    "what technologies do you use?",
    "what are your business hours?",
    "do you offer technical support?",
    "how can i hire your services?",
    "how long does a project take?",
    "goodbye",
  ]

  const enviarMensaje = async () => {
    if (!mensaje.trim()) return // evita enviar mensajes vacíos

    setShowExamples(false) // ocultar ejemplos cuando el usuario escribe algo

    try {
      const res = await fetch(`${backendUrl}/chat`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: mensaje })
      })

      if (!res.ok) throw new Error("Error al contactar al backend")

      const data = await res.json()
      setRespuesta(data.respuesta)
    } catch (error) {
      console.error(error)
      setRespuesta("Ocurrió un error al procesar tu mensaje.")
    }
  }

  return (
    <div style={{ padding: "2rem" }}>
      <h1>Chatbot FAQ</h1>

      {showExamples && (
        <div style={{ marginBottom: "1rem", backgroundColor: "#f0f0f0", padding: "1rem", borderRadius: "8px" }}>
          <p><strong>Examples of queries you can make:</strong></p>
          <ul>
            {ejemplos.map((ej, i) => (
              <li key={i} style={{ cursor: "pointer", color: "blue" }}
                  onClick={() => { setMensaje(ej); setShowExamples(false); setRespuesta("") }}>
                {ej}
              </li>
            ))}
          </ul>
          <p>Type your question bellow and press Submit.</p>
        </div>
      )}

      <input
        type="text"
        value={mensaje}
        onChange={(e) => setMensaje(e.target.value)}
        placeholder="Write your query here, e.g.: What does your company do?"
        style={{ width: "100%", padding: "0.5rem", marginBottom: "0.5rem" }}
      />
      <button onClick={enviarMensaje}>Submit</button>

      {respuesta && (
        <p style={{ marginTop: "1rem" }}>
          <strong>Respuesta:</strong> {respuesta}
        </p>
      )}
    </div>
  )
}

export default App
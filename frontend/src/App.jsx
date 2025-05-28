import { useState } from 'react'

function App() {
  const [mensaje, setMensaje] = useState("")
  const [respuesta, setRespuesta] = useState("")

  const backendUrl = import.meta.env.VITE_BACKEND_URL

  const enviarMensaje = async () => {
    try {
      const res = await fetch(`${backendUrl}/chat`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ mensaje })
      })

      if (!res.ok) {
        throw new Error("Error al contactar al backend")
      }

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
      <input
        type="text"
        value={mensaje}
        onChange={(e) => setMensaje(e.target.value)}
        placeholder="Escribe tu pregunta"
      />
      <button onClick={enviarMensaje}>Enviar</button>
      <p><strong>Respuesta:</strong> {respuesta}</p>
    </div>
  )
}

export default App



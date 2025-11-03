import React, { useState } from "react";
import "./Mensajes.css";

function Mensajes() {
  const [conversaciones] = useState([
    { id: 1, paciente: "Juan Restrepo", ultimo: "Doctor, ¿puedo tomar el medicamento en ayunas?" },
    { id: 2, paciente: "María López", ultimo: "Gracias por la receta, me siento mejor." },
    { id: 3, paciente: "Carlos Pérez", ultimo: "¿Podemos reprogramar la cita?" },
  ]);

  const [chatActivo, setChatActivo] = useState(null);
  const [mensajes, setMensajes] = useState([]);
  const [nuevoMensaje, setNuevoMensaje] = useState("");

  const abrirChat = (paciente) => {
    setChatActivo(paciente);
    // Simulación de mensajes cargados
    setMensajes([
      { remitente: "paciente", texto: "Hola doctor, tengo una duda." },
      { remitente: "doctor", texto: "Claro, dime." },
    ]);
  };

  const enviarMensaje = (e) => {
    e.preventDefault();
    if (!nuevoMensaje.trim()) return;

    const mensaje = { remitente: "doctor", texto: nuevoMensaje };
    setMensajes([...mensajes, mensaje]);
    setNuevoMensaje("");
  };

  return (
    <div className="mensajes-container">
      <h2>💬 Mensajes</h2>
      <p>Comunícate con tus pacientes en tiempo real.</p>

      <div className="mensajes-layout">
        {/* Lista de conversaciones */}
        <aside className="conversaciones-lista">
          <h3>Conversaciones</h3>
          <ul>
            {conversaciones.map((c) => (
              <li
                key={c.id}
                className={chatActivo === c.paciente ? "activo" : ""}
                onClick={() => abrirChat(c.paciente)}
              >
                <strong>{c.paciente}</strong>
                <p>{c.ultimo}</p>
              </li>
            ))}
          </ul>
        </aside>

        {/* Chat activo */}
        <section className="chat-area">
          {chatActivo ? (
            <>
              <div className="chat-header">
                <h3>Chat con {chatActivo}</h3>
              </div>
              <div className="chat-mensajes">
                {mensajes.map((m, index) => (
                  <div
                    key={index}
                    className={`mensaje ${m.remitente === "doctor" ? "doctor" : "paciente"}`}
                  >
                    <p>{m.texto}</p>
                  </div>
                ))}
              </div>
              <form className="chat-input" onSubmit={enviarMensaje}>
                <input
                  type="text"
                  placeholder="Escribe un mensaje..."
                  value={nuevoMensaje}
                  onChange={(e) => setNuevoMensaje(e.target.value)}
                />
                <button type="submit">Enviar</button>
              </form>
            </>
          ) : (
            <div className="chat-placeholder">
              <p>Selecciona una conversación para comenzar</p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default Mensajes;

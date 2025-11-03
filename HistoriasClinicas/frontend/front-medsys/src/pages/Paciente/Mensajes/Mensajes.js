import React, { useState } from "react";
import "./Mensajes.css";

function MensajesPaciente() {
  const [conversaciones] = useState([
    { id: 1, profesional: "Dr. Juan Pérez", ultimo: "Recuerda tomar el medicamento en la mañana." },
    { id: 2, profesional: "Dra. María López", ultimo: "El resultado de tu examen ya está disponible." },
  ]);

  const [chatActivo, setChatActivo] = useState(null);
  const [mensajes, setMensajes] = useState([]);
  const [nuevoMensaje, setNuevoMensaje] = useState("");

  const abrirChat = (profesional) => {
    setChatActivo(profesional);
    // Simulación de mensajes cargados
    setMensajes([
      { remitente: "profesional", texto: "Hola, ¿cómo sigues?" },
      { remitente: "paciente", texto: "Me siento mejor, gracias doctor." },
    ]);
  };

  const enviarMensaje = (e) => {
    e.preventDefault();
    if (!nuevoMensaje.trim()) return;

    const mensaje = { remitente: "paciente", texto: nuevoMensaje };
    setMensajes([...mensajes, mensaje]);
    setNuevoMensaje("");
  };

  return (
    <div className="mensajes-container">
      <h2>💬 Mensajes</h2>
      <p>Comunícate con tus profesionales de salud.</p>

      <div className="mensajes-layout">
        {/* Lista de conversaciones */}
        <aside className="conversaciones-lista">
          <h3>Conversaciones</h3>
          <ul>
            {conversaciones.map((c) => (
              <li
                key={c.id}
                className={chatActivo === c.profesional ? "activo" : ""}
                onClick={() => abrirChat(c.profesional)}
              >
                <strong>{c.profesional}</strong>
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
                    className={`mensaje ${m.remitente}`}
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

export default MensajesPaciente;

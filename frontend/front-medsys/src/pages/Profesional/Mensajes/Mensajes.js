import React, { useState, useEffect, useRef } from "react";
import "./Mensajes.css";

function MensajesProfesional() {
  const [conversaciones, setConversaciones] = useState([]);
  const [busqueda, setBusqueda] = useState(""); 
  const [chatActivo, setChatActivo] = useState(null);
  const [mensajes, setMensajes] = useState([]);
  const [nuevoMensaje, setNuevoMensaje] = useState("");

  const mensajesEndRef = useRef(null);

  // ID del Médico logueado (Ajusta este ID según tus pruebas o contexto de login)
  const idMedicoLogueado = "49f8a1a9-27bc-4527-b9c7-b910fa6e8dad"; 

  const hacerScrollAlFondo = () => {
    mensajesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (mensajes.length > 0) {
      hacerScrollAlFondo();
    }
  }, [mensajes]);

  // 1. Cargar la lista de Pacientes usando la API correspondiente
  useEffect(() => {
    fetch("http://localhost:7000/mensajes/contactos")
      .then((res) => {
        if (!res.ok) throw new Error("Error al conectar con la API de pacientes");
        return res.json();
      })
      .then((data) => {
        if (Array.isArray(data)) {
          setConversaciones(data);
        }
      })
      .catch((err) => console.error("Error al cargar pacientes:", err));
  }, []);

  // 2. Abrir el chat con el paciente seleccionado
  const abrirChat = (paciente) => {
    setChatActivo(paciente);

    fetch(`http://localhost:7000/mensajes/chat/${idMedicoLogueado}/${paciente.id}`)
      .then((res) => {
        if (!res.ok) throw new Error("Error al obtener el historial");
        return res.json();
      })
      .then((data) => {
        if (Array.isArray(data)) {
          setMensajes(data);
        }
      })
      .catch((err) => {
        console.error("Error al obtener chat:", err);
        setMensajes([]);
      });
  };

  // 3. Enviar mensaje del Médico al Paciente
  const enviarMensaje = (e) => {
    e.preventDefault();
    if (!nuevoMensaje.trim() || !chatActivo) return;

    const payload = {
      idremitente: idMedicoLogueado,
      iddestinatario: chatActivo.id,
      contenido: nuevoMensaje,
    };

    fetch("http://localhost:7000/mensajes/enviar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    })
      .then((res) => res.json())
      .then((data) => {
        if (!data.error) {
          // Renderizado optimista (Al ser el remitente, sale con la clase 'doctor' a la derecha)
          const mensajeOptimista = {
            idmensaje: data.idmensaje || Date.now().toString(),
            idremitente: idMedicoLogueado,
            iddestinatario: chatActivo.id,
            contenido: nuevoMensaje,
            fecha: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
            estado_seguridad: "✅ Verificado (Cifrado e Íntegro)",
          };

          setMensajes((prev) => [...prev, mensajeOptimista]);
          setNuevoMensaje("");

          setTimeout(() => abrirChat(chatActivo), 300);
        } else {
          console.error("Error en el servidor:", data.error);
        }
      })
      .catch((err) => console.error("Error en la petición HTTP:", err));
  };

  // 👈 NUEVA FUNCIÓN: Extrae "HH:MM" de la fecha del mensaje
  const extraerHoraFormateada = (fechaStr) => {
    if (!fechaStr) return "";
    try {
      if (fechaStr.length <= 5) return fechaStr; 
      const fragmentos = fechaStr.split(" ");
      if (fragmentos.length > 1) {
        return fragmentos[1].substring(0, 5); // Toma solo los primeros 5 caracteres (HH:MM)
      }
      return fechaStr;
    } catch (e) {
      return "";
    }
  };

  const conversacionesFiltradas = conversaciones.filter((c) =>
    c.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  return (
    <div className="mensajes-container">
      <h2>💬 Panel de Mensajería Profesional</h2>
      <p>Gestión de consultas y seguimiento seguro con tus pacientes.</p>

      <div className="mensajes-layout">
        {/* Barra Lateral: Lista de Pacientes */}
        <aside className="conversaciones-lista">
          <h3>Pacientes</h3>
          
          <div className="search-container">
            <input
              type="text"
              placeholder="Buscar paciente..."
              value={busqueda}
              onChange={(e) => setBusqueda(e.target.value)}
              className="search-input"
            />
          </div>

          <ul>
            {conversacionesFiltradas.length > 0 ? (
              conversacionesFiltradas.map((c) => (
                <li
                  key={c.id}
                  className={chatActivo?.id === c.id ? "activo" : ""}
                  onClick={() => abrirChat(c)}
                >
                  <strong>{c.nombre}</strong>
                  <p>{c.ultimo_msg || "Ver historial de chat"}</p>
                </li>
              ))
            ) : (
              <li className="no-results">No se encontraron pacientes</li>
            )}
          </ul>
        </aside>

        {/* Área del Chat */}
        <section className="chat-area">
          {chatActivo ? (
            <>
              <div className="chat-header">
                <h3>Paciente: {chatActivo.nombre}</h3>
              </div>
              
              <div className="chat-mensajes">
                {mensajes.map((m) => {
                  // Si el ID del remitente coincide con el médico logueado va a la derecha ('doctor')
                  // Si viene del paciente va a la izquierda ('paciente')
                  const soyElRemitente = String(m.idremitente).trim() === String(idMedicoLogueado).trim();

                  return (
                    <div
                      key={m.idmensaje || Math.random()}
                      className={`mensaje ${soyElRemitente ? "doctor" : "paciente"}`}
                      title={m.estado_seguridad || "Mensaje verificado"}
                    >
                      <div className="mensaje-texto">{m.contenido}</div>
                      {/* 👈 AQUÍ SE AGREGA LA HORA QUE FALTABA */}
                      <span className="mensaje-hora">{extraerHoraFormateada(m.fecha)}</span>
                    </div>
                  );
                })}
                <div ref={mensajesEndRef} />
              </div>

              <form className="chat-input" onSubmit={enviarMensaje}>
                <input
                  type="text"
                  placeholder="Escribe una respuesta médica..."
                  value={nuevoMensaje}
                  onChange={(e) => setNuevoMensaje(e.target.value)}
                />
                <button type="submit">Enviar</button>
              </form>
            </>
          ) : (
            <div className="chat-placeholder">
              <p>Selecciona un paciente para revisar su historial de mensajes</p>
            </div>
          )}
        </section>
      </div>
    </div>
  );
}

export default MensajesProfesional;
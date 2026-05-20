import React, { useState, useEffect, useRef } from "react";
import "./Mensajes.css";

function MensajesPaciente() {
  const [conversaciones, setConversaciones] = useState([]);
  const [busqueda, setBusqueda] = useState(""); // 👈 Estado para controlar el texto de búsqueda
  const [chatActivo, setChatActivo] = useState(null);
  const [mensajes, setMensajes] = useState([]);
  const [nuevoMensaje, setNuevoMensaje] = useState("");

  const mensajesEndRef = useRef(null);

  // ID hardcodeado del paciente actual logueado para las pruebas de MedSys
  const idPacienteLogueado = "69151a86-6b0b-457c-8f4c-7594d6ef4423";

  const hacerScrollAlFondo = () => {
    mensajesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    if (mensajes.length > 0) {
      hacerScrollAlFondo();
    }
  }, [mensajes]);

  // 1. Cargar la lista de profesionales de salud desde la API
  useEffect(() => {
    fetch("http://localhost:7000/mensajes/medicos-disponibles")
      .then((res) => {
        if (!res.ok) throw new Error("Error al conectar con la API de médicos");
        return res.json();
      })
      .then((data) => {
        if (Array.isArray(data)) {
          setConversaciones(data);
        }
      })
      .catch((err) => console.error("Error al cargar médicos:", err));
  }, []);

  // 2. Abrir el chat y traer el historial bidireccional desencriptado
  const abrirChat = (medico) => {
    setChatActivo(medico);

    fetch(`http://localhost:7000/mensajes/chat/${medico.id}/${idPacienteLogueado}`)
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

  // 3. Enviar mensaje cifrado con integridad HMAC
  const enviarMensaje = (e) => {
    e.preventDefault();
    if (!nuevoMensaje.trim() || !chatActivo) return;

    const payload = {
      idremitente: idPacienteLogueado,
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
          const mensajeOptimista = {
            idmensaje: data.idmensaje || Date.now().toString(),
            idremitente: idPacienteLogueado,
            iddestinatario: chatActivo.id,
            contenido: nuevoMensaje,
            fecha: new Date().toLocaleTimeString([], { hour: "2-digit", minute: "2-digit" }),
            estado_seguridad: "✅ Verificado (Cifrado e Íntegro)",
          };

          setMensajes((prev) => [...prev, mensajeOptimista]);
          setNuevoMensaje("");

          setTimeout(() => abrirChat(chatActivo), 300);
        } else {
          console.error("Error en servidor:", data.error);
        }
      })
      .catch((err) => console.error("Error en la petición HTTP:", err));
  };

  const extraerHoraFormateada = (fechaStr) => {
    if (!fechaStr) return "";
    try {
      if (fechaStr.length <= 5) return fechaStr; 
      const fragmentos = fechaStr.split(" ");
      if (fragmentos.length > 1) {
        return fragmentos[1].substring(0, 5);
      }
      return fechaStr;
    } catch (e) {
      return "";
    }
  };

  // 👈 Filtrado reactivo: Se ejecuta automáticamente cada vez que cambia "busqueda" o "conversaciones"
  const conversacionesFiltradas = conversaciones.filter((c) =>
    c.nombre.toLowerCase().includes(busqueda.toLowerCase())
  );

  return (
    <div className="mensajes-container">
      <h2>💬 Mensajes</h2>
      <p>Comunícate con tus profesionales de salud de forma segura.</p>

      <div className="mensajes-layout">
        {/* Barra Lateral: Lista de Médicos Disponibles */}
        <aside className="conversaciones-lista">
          <h3>Conversaciones</h3>
          
          {/* 👈 NUEVA BARRA DE BÚSQUEDA */}
          <div className="search-container">
            <input
              type="text"
              placeholder="Buscar profesional..."
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
                  <p>{c.ultimo_msg || "Haz clic para abrir el chat"}</p>
                </li>
              ))
            ) : (
              <li className="no-results">No se encontraron profesionales</li>
            )}
          </ul>
        </aside>

        {/* Contenedor del Chat Activo */}
        <section className="chat-area">
          {chatActivo ? (
            <>
              <div className="chat-header">
                <h3>Chat con {chatActivo.nombre}</h3>
              </div>
              
              <div className="chat-mensajes">
                {mensajes.map((m) => {
                  const soyElRemitente = String(m.idremitente).trim() === String(idPacienteLogueado).trim();

                  return (
                    <div
                      key={m.idmensaje || Math.random()}
                      className={`mensaje ${soyElRemitente ? "doctor" : "paciente"}`}
                      title={m.estado_seguridad || "Mensaje verificado"}
                    >
                      <div className="mensaje-texto">{m.contenido}</div>
                      <span className="mensaje-hora">{extraerHoraFormateada(m.fecha)}</span>
                    </div>
                  );
                })}
                <div ref={mensajesEndRef} />
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
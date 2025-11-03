import React, { useState } from "react";
import "./Configuracion.css";

function Configuracion() {
  const [nombre, setNombre] = useState("Dr. Juan Pérez");
  const [especialidad, setEspecialidad] = useState("Medicina General");
  const [email, setEmail] = useState("juanperez@correo.com");
  const [telefono, setTelefono] = useState("3001234567");
  const [horario, setHorario] = useState("Lunes a Viernes, 8:00 AM - 5:00 PM");
  const [notificaciones, setNotificaciones] = useState(true);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log("Datos actualizados:", {
      nombre,
      especialidad,
      email,
      telefono,
      horario,
      notificaciones,
    });
    alert("Configuración guardada correctamente ✅");
  };

  return (
    <div className="config-container">
      <h2>⚙️ Configuración del Profesional</h2>
      <p>Ajusta tu perfil, horarios y preferencias.</p>

      <form className="config-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Nombre completo</label>
          <input
            type="text"
            value={nombre}
            onChange={(e) => setNombre(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Especialidad</label>
          <input
            type="text"
            value={especialidad}
            onChange={(e) => setEspecialidad(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Correo electrónico</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Teléfono</label>
          <input
            type="tel"
            value={telefono}
            onChange={(e) => setTelefono(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label>Horario de atención</label>
          <input
            type="text"
            value={horario}
            onChange={(e) => setHorario(e.target.value)}
          />
        </div>

        <div className="form-group checkbox">
          <label>
            <input
              type="checkbox"
              checked={notificaciones}
              onChange={() => setNotificaciones(!notificaciones)}
            />
            Recibir notificaciones de nuevas citas
          </label>
        </div>

        <button type="submit" className="btn-save">Guardar cambios</button>
      </form>
    </div>
  );
}

export default Configuracion;

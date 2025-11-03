import React, { useState } from "react";
import "./Citas.css";

function CitasPaciente() {
  const [citas, setCitas] = useState([
    { id: 1, fecha: "05/11/2025", hora: "10:00 AM", profesional: "Dr. Juan Pérez", estado: "Confirmada" },
    { id: 2, fecha: "10/11/2025", hora: "02:00 PM", profesional: "Dra. María López", estado: "Pendiente" },
    { id: 3, fecha: "20/10/2025", hora: "09:00 AM", profesional: "Dr. Carlos Gómez", estado: "Completada" },
  ]);

  // Lista de profesionales disponibles en el consultorio
  const profesionales = ["Dr. Juan Pérez", "Dra. María López", "Dr. Carlos Gómez"];

  const [nuevaCita, setNuevaCita] = useState({
    fecha: "",
    hora: "",
    profesional: "",
  });

  const handleChange = (e) => {
    setNuevaCita({ ...nuevaCita, [e.target.name]: e.target.value });
  };

  const handleAgendar = (e) => {
    e.preventDefault();
    if (!nuevaCita.fecha || !nuevaCita.hora || !nuevaCita.profesional) return;

    let profesionalAsignado = nuevaCita.profesional;

    // Si elige "aleatorio", asignamos un profesional al azar
    if (profesionalAsignado === "aleatorio") {
      const randomIndex = Math.floor(Math.random() * profesionales.length);
      profesionalAsignado = profesionales[randomIndex];
    }

    const nueva = {
      id: citas.length + 1,
      fecha: nuevaCita.fecha,
      hora: nuevaCita.hora,
      profesional: profesionalAsignado,
      estado: "Pendiente",
    };

    setCitas([...citas, nueva]);
    setNuevaCita({ fecha: "", hora: "", profesional: "" });
    alert(`✅ Cita solicitada con ${profesionalAsignado}`);
  };

  return (
    <div className="citas-paciente-container">
      <h2>📅 Mis Citas</h2>
      <p>Consulta tus citas médicas, agenda nuevas y revisa el estado de cada una.</p>

      {/* Resumen */}
      <div className="citas-summary">
        <div className="summary-card">
          <h3>{citas.filter(c => c.estado === "Pendiente").length}</h3>
          <p>Pendientes</p>
        </div>
        <div className="summary-card">
          <h3>{citas.filter(c => c.estado === "Confirmada").length}</h3>
          <p>Confirmadas</p>
        </div>
        <div className="summary-card">
          <h3>{citas.filter(c => c.estado === "Completada").length}</h3>
          <p>Completadas</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="citas-table-container">
        <table className="citas-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Profesional</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {citas.map((c) => (
              <tr key={c.id}>
                <td>{c.fecha}</td>
                <td>{c.hora}</td>
                <td>{c.profesional}</td>
                <td>
                  <span className={`status ${c.estado.toLowerCase()}`}>
                    {c.estado}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Formulario */}
      <div className="citas-form-container">
        <h3>➕ Agendar nueva cita</h3>
        <form className="citas-form" onSubmit={handleAgendar}>
          <div className="form-group">
            <label>Fecha</label>
            <input
              type="date"
              name="fecha"
              value={nuevaCita.fecha}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Hora</label>
            <input
              type="time"
              name="hora"
              value={nuevaCita.hora}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Profesional</label>
            <select
              name="profesional"
              value={nuevaCita.profesional}
              onChange={handleChange}
              required
            >
              <option value="">Seleccione...</option>
              <option value="aleatorio">Asignar Aleatoriamente</option>
              {profesionales.map((p, i) => (
                <option key={i} value={p}>{p}</option>
              ))}
            </select>
          </div>
          <button type="submit" className="btn-agendar">Agendar Cita</button>
        </form>
      </div>
    </div>
  );
}

export default CitasPaciente;

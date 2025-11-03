import React, { useState } from "react";
import "./Historial.css";

function HistorialPaciente() {
  const [consultas] = useState([
    {
      id: 1,
      fecha: "20/10/2025",
      profesional: "Dr. Juan Pérez",
      especialidad: "Medicina General",
      diagnostico: "Hipertensión",
      tratamiento: "Enalapril 10mg cada 12h",
      notas: "Se recomienda control de presión arterial semanal."
    },
    {
      id: 2,
      fecha: "05/09/2025",
      profesional: "Dra. María López",
      especialidad: "Dermatología",
      diagnostico: "Dermatitis atópica",
      tratamiento: "Crema hidratante + antihistamínico",
      notas: "Evitar exposición prolongada al sol."
    },
    {
      id: 3,
      fecha: "15/07/2025",
      profesional: "Dr. Carlos Gómez",
      especialidad: "Psicología",
      diagnostico: "Ansiedad leve",
      tratamiento: "Terapia cognitivo-conductual",
      notas: "Asistir a sesiones semanales."
    }
  ]);

  const [seleccionada, setSeleccionada] = useState(null);

  return (
    <div className="historial-container">
      <h2>🧾 Historial Médico</h2>
      <p>Consulta tus antecedentes clínicos y detalles de cada cita.</p>

      {/* Resumen */}
      <div className="historial-summary">
        <div className="summary-card">
          <h3>{consultas.length}</h3>
          <p>Consultas registradas</p>
        </div>
        <div className="summary-card">
          <h3>{new Set(consultas.map(c => c.especialidad)).size}</h3>
          <p>Especialidades atendidas</p>
        </div>
        <div className="summary-card">
          <h3>{new Set(consultas.map(c => c.diagnostico)).size}</h3>
          <p>Diagnósticos distintos</p>
        </div>
      </div>

      {/* Tabla de consultas */}
      <div className="historial-table-container">
        <table className="historial-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Profesional</th>
              <th>Especialidad</th>
              <th>Diagnóstico</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {consultas.map((c) => (
              <tr key={c.id}>
                <td>{c.fecha}</td>
                <td>{c.profesional}</td>
                <td>{c.especialidad}</td>
                <td>{c.diagnostico}</td>
                <td>
                  <button
                    className="btn-detalle"
                    onClick={() => setSeleccionada(c)}
                  >
                    Ver Detalle
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detalle de consulta */}
      {seleccionada && (
        <div className="detalle-consulta">
          <h3>📋 Detalle de la consulta</h3>
          <p><strong>Fecha:</strong> {seleccionada.fecha}</p>
          <p><strong>Profesional:</strong> {seleccionada.profesional}</p>
          <p><strong>Especialidad:</strong> {seleccionada.especialidad}</p>
          <p><strong>Diagnóstico:</strong> {seleccionada.diagnostico}</p>
          <p><strong>Tratamiento:</strong> {seleccionada.tratamiento}</p>
          <p><strong>Notas:</strong> {seleccionada.notas}</p>
          <button className="btn-cerrar" onClick={() => setSeleccionada(null)}>
            Cerrar
          </button>
        </div>
      )}
    </div>
  );
}

export default HistorialPaciente;

import React, { useState } from "react";
import "./Resultados.css";

function ResultadosPaciente() {
  const [resultados] = useState([
    {
      id: 1,
      fecha: "01/11/2025",
      profesional: "Dr. Juan Pérez",
      tipo: "Examen de sangre",
      archivo: "examen-sangre.pdf",
      estado: "Disponible",
    },
    {
      id: 2,
      fecha: "20/10/2025",
      profesional: "Dra. María López",
      tipo: "Radiografía de tórax",
      archivo: "radiografia-torax.jpg",
      estado: "Disponible",
    },
    {
      id: 3,
      fecha: "05/09/2025",
      profesional: "Dr. Carlos Gómez",
      tipo: "Informe psicológico",
      archivo: "informe-psicologia.pdf",
      estado: "Archivado",
    },
  ]);

  return (
    <div className="resultados-container">
      <h2>📂 Resultados Médicos</h2>
      <p>Consulta y descarga los resultados de tus exámenes y documentos clínicos.</p>

      {/* Resumen */}
      <div className="resultados-summary">
        <div className="summary-card">
          <h3>{resultados.filter(r => r.estado === "Disponible").length}</h3>
          <p>Disponibles</p>
        </div>
        <div className="summary-card">
          <h3>{resultados.filter(r => r.estado === "Archivado").length}</h3>
          <p>Archivados</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="resultados-table-container">
        <table className="resultados-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Profesional</th>
              <th>Tipo</th>
              <th>Archivo</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {resultados.map((r) => (
              <tr key={r.id}>
                <td>{r.fecha}</td>
                <td>{r.profesional}</td>
                <td>{r.tipo}</td>
                <td>{r.archivo}</td>
                <td>
                  <span className={`status ${r.estado.toLowerCase()}`}>
                    {r.estado}
                  </span>
                </td>
                <td>
                  <button className="btn-view">Ver</button>
                  <button className="btn-download">Descargar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Nota */}
      <div className="resultados-nota">
        <p>ℹ️ Los resultados disponibles pueden ser descargados en formato PDF o imagen. Consulta a tu médico para su interpretación.</p>
      </div>
    </div>
  );
}

export default ResultadosPaciente;

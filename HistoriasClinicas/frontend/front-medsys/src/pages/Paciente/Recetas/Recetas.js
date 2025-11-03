import React, { useState } from "react";
import "./Recetas.css";

function RecetasPaciente() {
  const [recetas] = useState([
    {
      id: 1,
      fecha: "01/11/2025",
      profesional: "Dr. Juan Pérez",
      medicamento: "Enalapril 10mg",
      dosis: "1 tableta cada 12h",
      estado: "Activa",
    },
    {
      id: 2,
      fecha: "15/10/2025",
      profesional: "Dra. María López",
      medicamento: "Crema hidratante",
      dosis: "Aplicar 2 veces al día",
      estado: "Activa",
    },
    {
      id: 3,
      fecha: "01/09/2025",
      profesional: "Dr. Carlos Gómez",
      medicamento: "Paracetamol 500mg",
      dosis: "1 tableta cada 8h por 5 días",
      estado: "Finalizada",
    },
  ]);

  return (
    <div className="recetas-container">
      <h2>💊 Mis Recetas</h2>
      <p>Consulta tus medicamentos actuales y el historial de tratamientos.</p>

      {/* Resumen */}
      <div className="recetas-summary">
        <div className="summary-card">
          <h3>{recetas.filter(r => r.estado === "Activa").length}</h3>
          <p>Recetas Activas</p>
        </div>
        <div className="summary-card">
          <h3>{recetas.filter(r => r.estado === "Finalizada").length}</h3>
          <p>Recetas Finalizadas</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="recetas-table-container">
        <table className="recetas-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Profesional</th>
              <th>Medicamento</th>
              <th>Dosis</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {recetas.map((r) => (
              <tr key={r.id}>
                <td>{r.fecha}</td>
                <td>{r.profesional}</td>
                <td>{r.medicamento}</td>
                <td>{r.dosis}</td>
                <td>
                  <span className={`status ${r.estado.toLowerCase()}`}>
                    {r.estado}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Nota */}
      <div className="recetas-nota">
        <p>⚠️ Recuerda seguir las indicaciones de tu médico y no suspender el tratamiento sin consultar.</p>
      </div>
    </div>
  );
}

export default RecetasPaciente;

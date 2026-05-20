import React, { useState, useEffect } from "react";
import "./Recetas.css";

function RecetasPaciente() {
  const paciente = JSON.parse(localStorage.getItem("paciente"));
  const [recetas, setRecetas] = useState([]);
  const [seleccionada, setSeleccionada] = useState(null);

  useEffect(() => {
    const fetchRecetas = async () => {
      if (!paciente || !paciente.documento) return;

      try {
        const res = await fetch(`http://127.0.0.1:7000/recetamedica/paciente/${paciente.documento}`);
        if (!res.ok) throw new Error("Error al obtener recetas médicas");
        const data = await res.json();
        setRecetas(data);
      } catch (err) {
        console.error("Error cargando recetas:", err);
      }
    };

    fetchRecetas();
  }, [paciente]);

  return (
    <div className="recetas-container">
      <h2>💊 Mis Recetas Médicas</h2>
      <p>Consulta tus medicamentos actuales y el historial de tratamientos.</p>

      {/* Resumen */}
      <div className="recetas-summary">
        <div className="summary-card">
          <h3>{recetas.filter(r => r.activo).length}</h3>
          <p>Recetas Activas</p>
        </div>
        <div className="summary-card">
          <h3>{recetas.filter(r => !r.activo).length}</h3>
          <p>Recetas Finalizadas</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="recetas-table-container">
        <table className="recetas-table">
          <thead>
            <tr>
              <th>Medicamento</th>
              <th>Dosis</th>
              <th>Profesional</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {recetas.map((r) => (
              <tr key={r.idreceta}>
                <td>{r.medicamento}</td>
                <td>{r.dosis}</td>
                <td>{r.nombre_profesional}</td>
                <td>
                  <span className={`status ${r.activo ? "activa" : "finalizada"}`}>
                    {r.activo ? "Activa" : "Finalizada"}
                  </span>
                </td>
                <td>
                  <button className="btn-detalle" onClick={() => setSeleccionada(r)}>
                    Ver Detalle
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detalle de receta */}
      {seleccionada && (
        <div className="detalle-receta">
          <h3>📋 Detalle de la receta</h3>
          <p><strong>Medicamento:</strong> {seleccionada.medicamento}</p>
          <p><strong>Dosis:</strong> {seleccionada.dosis}</p>
          <p><strong>Indicaciones:</strong> {seleccionada.indicaciones}</p>
          <p><strong>Profesional:</strong> {seleccionada.nombre_profesional}</p>
          <p><strong>Estado:</strong> {seleccionada.activo ? "Activa" : "Finalizada"}</p>
          <button className="btn-cerrar" onClick={() => setSeleccionada(null)}>
            Cerrar
          </button>
        </div>
      )}

      {/* Nota */}
      <div className="recetas-nota">
        <p>⚠️ Recuerda seguir las indicaciones de tu médico y no suspender el tratamiento sin consultar.</p>
      </div>
    </div>
  );
}

export default RecetasPaciente;

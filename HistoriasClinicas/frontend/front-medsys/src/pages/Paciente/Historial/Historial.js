import React, { useState, useEffect } from "react";
import "./Historial.css";

function HistoriaClinicaPaciente() {
  const paciente = JSON.parse(localStorage.getItem("paciente"));
  const [consultas, setConsultas] = useState([]);
  const [seleccionada, setSeleccionada] = useState(null);

  useEffect(() => {
    const fetchHistorias = async () => {
      if (!paciente || !paciente.documento) return;

      try {
        const res = await fetch(`http://127.0.0.1:7000/historiaclinica/paciente/${paciente.documento}`);
        if (!res.ok) throw new Error("Error al obtener historias clínicas");
        const data = await res.json();
        setConsultas(data);
      } catch (err) {
        console.error("Error cargando historias clínicas:", err);
      }
    };

    fetchHistorias();
  }, [paciente]);

  return (
    <div className="historial-container">
      <h2>🧾 Historia Clínica</h2>
      <p>Consulta tu historia clínica y detalles de cada registro.</p>

      {/* Resumen */}
      <div className="historial-summary">
        <div className="summary-card">
          <h3>{consultas.length}</h3>
          <p>Registros en tu historia clínica</p>
        </div>
        <div className="summary-card">
          <h3>{new Set(consultas.map(c => c.cargo)).size}</h3>
          <p>Cargos atendidos</p>
        </div>
      </div>

      {/* Tabla de historias clínicas */}
      <div className="historial-table-container">
        <table className="historial-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Profesional</th>
              <th>Cargo</th>
              <th>Antecedentes</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {consultas.map((c) => (
              <tr key={c.idhistoria}>
                <td>{c.fecha}</td>
                <td>{c.nombre_profesional}</td>
                <td>{c.cargo}</td>
                <td>{c.antecedentes}</td>
                <td>
                  <button className="btn-detalle" onClick={() => setSeleccionada(c)}>
                    Ver Detalle
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detalle de historia clínica */}
      {seleccionada && (
        <div className="detalle-consulta">
          <h3>📋 Detalle de la historia clínica</h3>
          <p><strong>Fecha:</strong> {seleccionada.fecha}</p>
          <p><strong>Profesional:</strong> {seleccionada.nombre_profesional}</p>
          <p><strong>Cargo:</strong> {seleccionada.cargo}</p>
          <p><strong>Antecedentes:</strong> {seleccionada.antecedentes}</p>
          <p><strong>Observaciones:</strong> {seleccionada.observaciones}</p>
          <button className="btn-cerrar" onClick={() => setSeleccionada(null)}>
            Cerrar
          </button>
        </div>
      )}
    </div>
  );
}

export default HistoriaClinicaPaciente;

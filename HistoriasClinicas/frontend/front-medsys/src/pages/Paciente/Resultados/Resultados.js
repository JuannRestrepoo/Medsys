import React, { useState, useEffect } from "react";
import "./Resultados.css";

function ResultadosPaciente() {
  const paciente = JSON.parse(localStorage.getItem("paciente"));
  const [resultados, setResultados] = useState([]);
  const [seleccionado, setSeleccionado] = useState(null);

  useEffect(() => {
    const fetchResultados = async () => {
      if (!paciente || !paciente.documento) return;

      try {
        const res = await fetch(`http://127.0.0.1:7000/resultados/paciente/${paciente.documento}`);
        if (!res.ok) throw new Error("Error al obtener resultados médicos");
        const data = await res.json();
        setResultados(data);
      } catch (err) {
        console.error("Error cargando resultados:", err);
      }
    };

    fetchResultados();
  }, [paciente]);

  return (
    <div className="resultados-container">
      <h2>📂 Resultados Médicos</h2>
      <p>Consulta y descarga los resultados de tus exámenes y documentos clínicos.</p>

      {/* Resumen */}
      <div className="resultados-summary">
        <div className="summary-card">
          <h3>{resultados.filter(r => r.activo).length}</h3>
          <p>Disponibles</p>
        </div>
        <div className="summary-card">
          <h3>{resultados.filter(r => !r.activo).length}</h3>
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
              <th>Título</th>
              <th>Archivo</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {resultados.map((r) => (
              <tr key={r.idresultado}>
                <td>{new Date(r.fecha).toLocaleDateString()}</td>
                <td>{r.nombre_profesional}</td>
                <td>{r.titulo}</td>
                <td>{r.archivo}</td>
                <td>
                  <span className={`status ${r.activo ? "disponible" : "archivado"}`}>
                    {r.activo ? "Disponible" : "Archivado"}
                  </span>
                </td>
                <td>
                  <button className="btn-view" onClick={() => setSeleccionado(r)}>Ver Detalles</button>
                  <button
                    className="btn-download"
                    onClick={() => window.open(`http://127.0.0.1:7000/uploads/${r.archivo}`, "_blank")}
                  >
                    Descargar
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Detalle */}
      {seleccionado && (
        <div className="detalle-resultado">
          <h3>📋 Detalle del resultado</h3>
          <p><strong>Título:</strong> {seleccionado.titulo}</p>
          <p><strong>Descripción:</strong> {seleccionado.descripcion}</p>
          <p><strong>Profesional:</strong> {seleccionado.nombre_profesional}</p>
          <p><strong>Archivo:</strong> {seleccionado.archivo}</p>
          <p><strong>Estado:</strong> {seleccionado.activo ? "Disponible" : "Archivado"}</p>
          <button className="btn-cerrar" onClick={() => setSeleccionado(null)}>Cerrar</button>
        </div>
      )}

      {/* Nota */}
      <div className="resultados-nota">
        <p>ℹ️ Los resultados disponibles pueden ser descargados en formato PDF o imagen. Consulta a tu médico para su interpretación.</p>
      </div>
    </div>
  );
}

export default ResultadosPaciente;

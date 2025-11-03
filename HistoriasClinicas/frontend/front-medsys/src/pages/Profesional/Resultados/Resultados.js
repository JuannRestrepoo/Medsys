import React, { useState } from "react";
import "./Resultados.css";

function Resultados() {
  const [resultados, setResultados] = useState([
    { id: 1, paciente: "Juan Restrepo", tipo: "Examen de sangre", fecha: "01/11/2025", archivo: "examen-sangre.pdf" },
    { id: 2, paciente: "María López", tipo: "Radiografía", fecha: "28/10/2025", archivo: "radiografia.jpg" },
  ]);

  const [nuevoPaciente, setNuevoPaciente] = useState("");
  const [nuevoTipo, setNuevoTipo] = useState("");
  const [nuevoArchivo, setNuevoArchivo] = useState(null);

  const handleSubirResultado = (e) => {
    e.preventDefault();
    if (!nuevoPaciente || !nuevoTipo || !nuevoArchivo) return;

    const nuevo = {
      id: resultados.length + 1,
      paciente: nuevoPaciente,
      tipo: nuevoTipo,
      fecha: new Date().toLocaleDateString(),
      archivo: nuevoArchivo.name,
    };

    setResultados([...resultados, nuevo]);
    setNuevoPaciente("");
    setNuevoTipo("");
    setNuevoArchivo(null);
  };

  return (
    <div className="resultados-container">
      <h2>📂 Resultados y Documentos</h2>
      <p>Sube y consulta los resultados médicos de tus pacientes.</p>

      {/* Formulario para subir resultado */}
      <form className="resultado-form" onSubmit={handleSubirResultado}>
        <div className="form-group">
          <label>Paciente</label>
          <input
            type="text"
            value={nuevoPaciente}
            onChange={(e) => setNuevoPaciente(e.target.value)}
            placeholder="Nombre del paciente"
          />
        </div>
        <div className="form-group">
          <label>Tipo de resultado</label>
          <input
            type="text"
            value={nuevoTipo}
            onChange={(e) => setNuevoTipo(e.target.value)}
            placeholder="Ej: Resonancia, Examen de sangre..."
          />
        </div>
        <div className="form-group">
          <label>Archivo</label>
          <input
            type="file"
            onChange={(e) => setNuevoArchivo(e.target.files[0])}
          />
        </div>
        <button type="submit" className="btn-upload">📤 Subir Resultado</button>
      </form>

      {/* Tabla de resultados */}
      <div className="resultados-table-container">
        <table className="resultados-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Tipo</th>
              <th>Fecha</th>
              <th>Archivo</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {resultados.map((r) => (
              <tr key={r.id}>
                <td>{r.paciente}</td>
                <td>{r.tipo}</td>
                <td>{r.fecha}</td>
                <td>{r.archivo}</td>
                <td>
                  <button className="btn-view">Ver</button>
                  <button className="btn-delete">Eliminar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Resultados;

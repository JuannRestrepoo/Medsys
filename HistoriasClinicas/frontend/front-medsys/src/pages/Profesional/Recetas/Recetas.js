import React, { useState } from "react";
import "./Recetas.css";

function Recetas() {
  const [recetas, setRecetas] = useState([
    { id: 1, paciente: "Juan Restrepo", medicamento: "Ibuprofeno 400mg", fecha: "01/11/2025", estado: "Activa" },
    { id: 2, paciente: "María López", medicamento: "Amoxicilina 500mg", fecha: "28/10/2025", estado: "Finalizada" },
  ]);

  const [nuevoPaciente, setNuevoPaciente] = useState("");
  const [nuevoMedicamento, setNuevoMedicamento] = useState("");

  const handleAgregarReceta = (e) => {
    e.preventDefault();
    if (!nuevoPaciente || !nuevoMedicamento) return;

    const nueva = {
      id: recetas.length + 1,
      paciente: nuevoPaciente,
      medicamento: nuevoMedicamento,
      fecha: new Date().toLocaleDateString(),
      estado: "Activa",
    };

    setRecetas([...recetas, nueva]);
    setNuevoPaciente("");
    setNuevoMedicamento("");
  };

  return (
    <div className="recetas-container">
      <h2>💊 Recetas y Tratamientos</h2>
      <p>Gestiona las recetas médicas de tus pacientes.</p>

      {/* Formulario para nueva receta */}
      <form className="receta-form" onSubmit={handleAgregarReceta}>
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
          <label>Medicamento / Tratamiento</label>
          <input
            type="text"
            value={nuevoMedicamento}
            onChange={(e) => setNuevoMedicamento(e.target.value)}
            placeholder="Ej: Paracetamol 500mg cada 8h"
          />
        </div>
        <button type="submit" className="btn-add">➕ Agregar Receta</button>
      </form>

      {/* Tabla de recetas */}
      <div className="recetas-table-container">
        <table className="recetas-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Medicamento</th>
              <th>Fecha</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {recetas.map((r) => (
              <tr key={r.id}>
                <td>{r.paciente}</td>
                <td>{r.medicamento}</td>
                <td>{r.fecha}</td>
                <td>
                  <span className={`status ${r.estado.toLowerCase()}`}>
                    {r.estado}
                  </span>
                </td>
                <td>
                  <button className="btn-view">Ver</button>
                  <button className="btn-end">Finalizar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Recetas;

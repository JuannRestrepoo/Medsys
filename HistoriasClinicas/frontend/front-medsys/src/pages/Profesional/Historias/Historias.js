import React, { useState } from "react";
import "./Historias.css";

function Historias() {
  // Datos de ejemplo (luego vendrán del backend)
  const [pacientes] = useState([
    { id: 1, nombre: "Juan Restrepo", edad: 28, ultimaConsulta: "10/10/2025" },
    { id: 2, nombre: "María López", edad: 34, ultimaConsulta: "05/09/2025" },
    { id: 3, nombre: "Carlos Pérez", edad: 42, ultimaConsulta: "22/08/2025" },
  ]);

  const handleVerHistoria = (id) => {
    console.log("Ver historia clínica del paciente con ID:", id);
    alert(`Abrir historia clínica del paciente con ID: ${id}`);
  };

  return (
    <div className="historias-container">
      <h2>🧾 Historias Clínicas</h2>
      <p>Consulta y gestiona la información médica de tus pacientes.</p>

      <div className="historias-table-container">
        <table className="historias-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Edad</th>
              <th>Última consulta</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {pacientes.map((p) => (
              <tr key={p.id}>
                <td>{p.nombre}</td>
                <td>{p.edad} años</td>
                <td>{p.ultimaConsulta}</td>
                <td>
                  <button
                    className="btn-view"
                    onClick={() => handleVerHistoria(p.id)}
                  >
                    Ver Historia
                  </button>
                  <button className="btn-edit">Editar</button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Historias;

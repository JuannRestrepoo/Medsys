import React, { useState } from "react";
import "./Pagos.css";

function Pagos() {
  const [facturas, setFacturas] = useState([
    { id: 1, paciente: "Juan Restrepo", servicio: "Consulta general", fecha: "01/11/2025", monto: 80000, estado: "Pendiente" },
    { id: 2, paciente: "María López", servicio: "Control dermatológico", fecha: "28/10/2025", monto: 120000, estado: "Pagado" },
    { id: 3, paciente: "Carlos Pérez", servicio: "Terapia psicológica", fecha: "25/10/2025", monto: 100000, estado: "Pendiente" },
  ]);

  const marcarComoPagado = (id) => {
    setFacturas(
      facturas.map((f) =>
        f.id === id ? { ...f, estado: "Pagado" } : f
      )
    );
  };

  return (
    <div className="pagos-container">
      <h2>💳 Pagos y Facturación</h2>
      <p>Consulta y gestiona las facturas de tus pacientes.</p>

      <div className="pagos-table-container">
        <table className="pagos-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Servicio</th>
              <th>Fecha</th>
              <th>Monto</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {facturas.map((f) => (
              <tr key={f.id}>
                <td>{f.paciente}</td>
                <td>{f.servicio}</td>
                <td>{f.fecha}</td>
                <td>${f.monto.toLocaleString()}</td>
                <td>
                  <span className={`status ${f.estado.toLowerCase()}`}>
                    {f.estado}
                  </span>
                </td>
                <td>
                  {f.estado === "Pendiente" ? (
                    <button
                      className="btn-pay"
                      onClick={() => marcarComoPagado(f.id)}
                    >
                      Marcar como Pagado
                    </button>
                  ) : (
                    <button className="btn-view">Ver Recibo</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Pagos;

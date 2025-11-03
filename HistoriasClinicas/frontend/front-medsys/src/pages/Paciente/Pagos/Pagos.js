import React, { useState } from "react";
import "./Pagos.css";

function PagosPaciente() {
  const [facturas] = useState([
    {
      id: 1,
      fecha: "01/11/2025",
      servicio: "Consulta general",
      monto: 80000,
      estado: "Pendiente",
    },
    {
      id: 2,
      fecha: "15/10/2025",
      servicio: "Control dermatológico",
      monto: 120000,
      estado: "Pagado",
    },
    {
      id: 3,
      fecha: "05/09/2025",
      servicio: "Terapia psicológica",
      monto: 100000,
      estado: "Pendiente",
    },
  ]);

  return (
    <div className="pagos-container">
      <h2>💳 Pagos</h2>
      <p>Consulta tus facturas médicas y el estado de tus pagos.</p>

      {/* Resumen */}
      <div className="pagos-summary">
        <div className="summary-card">
          <h3>{facturas.filter(f => f.estado === "Pendiente").length}</h3>
          <p>Facturas Pendientes</p>
        </div>
        <div className="summary-card">
          <h3>{facturas.filter(f => f.estado === "Pagado").length}</h3>
          <p>Facturas Pagadas</p>
        </div>
        <div className="summary-card">
          <h3>
            $
            {facturas
              .filter(f => f.estado === "Pendiente")
              .reduce((acc, f) => acc + f.monto, 0)
              .toLocaleString()}
          </h3>
          <p>Total Pendiente</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="pagos-table-container">
        <table className="pagos-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Servicio</th>
              <th>Monto</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {facturas.map((f) => (
              <tr key={f.id}>
                <td>{f.fecha}</td>
                <td>{f.servicio}</td>
                <td>${f.monto.toLocaleString()}</td>
                <td>
                  <span className={`status ${f.estado.toLowerCase()}`}>
                    {f.estado}
                  </span>
                </td>
                <td>
                  {f.estado === "Pendiente" ? (
                    <button className="btn-pay">Pagar</button>
                  ) : (
                    <button className="btn-view">Ver Recibo</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Nota */}
      <div className="pagos-nota">
        <p>ℹ️ Puedes realizar tus pagos en línea o en el centro médico. Una vez confirmado, el estado cambiará a "Pagado".</p>
      </div>
    </div>
  );
}

export default PagosPaciente;

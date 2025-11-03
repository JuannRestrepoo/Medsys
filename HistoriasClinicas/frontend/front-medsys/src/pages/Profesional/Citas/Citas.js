import React from "react";
import "./Citas.css";

function Citas() {
  return (
    <div className="citas-container">
      <h2>📅 Agenda de Citas</h2>
      <p>Aquí puedes gestionar tus citas con los pacientes.</p>

      {/* Resumen rápido */}
      <div className="citas-summary">
        <div className="summary-card">
          <h3>5</h3>
          <p>Citas de hoy</p>
        </div>
        <div className="summary-card">
          <h3>2</h3>
          <p>Solicitudes pendientes</p>
        </div>
        <div className="summary-card">
          <h3>12</h3>
          <p>Citas confirmadas esta semana</p>
        </div>
      </div>

      {/* Tabla de citas */}
      <div className="citas-table-container">
        <table className="citas-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Servicio</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Estado</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Juan Restrepo</td>
              <td>Consulta general</td>
              <td>10/11/2025</td>
              <td>10:00 AM</td>
              <td><span className="status pending">Pendiente</span></td>
              <td>
                <button className="btn-accept">Aceptar</button>
                <button className="btn-reject">Rechazar</button>
              </td>
            </tr>
            <tr>
              <td>María López</td>
              <td>Control dermatológico</td>
              <td>10/11/2025</td>
              <td>11:30 AM</td>
              <td><span className="status confirmed">Confirmada</span></td>
              <td>
                <button className="btn-view">Ver</button>
              </td>
            </tr>
            <tr>
              <td>Carlos Pérez</td>
              <td>Terapia psicológica</td>
              <td>11/11/2025</td>
              <td>09:00 AM</td>
              <td><span className="status cancelled">Cancelada</span></td>
              <td>
                <button className="btn-view">Ver</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Citas;

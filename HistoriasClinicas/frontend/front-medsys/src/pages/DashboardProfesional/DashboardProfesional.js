import React from "react";
import "./DashboardProfesional.css";

function DashboardProfesional() {
  return (
    <div className="dashboard-container">
      {/* Overview */}
      <section className="summary-cards">
        <div className="card">📅 8 citas hoy</div>
        <div className="card">👥 25 pacientes activos</div>
        <div className="card">💊 2 recetas pendientes</div>
        <div className="card">⚠️ 3 alertas médicas</div>
      </section>

      {/* Quick tasks */}
      <section className="quick-tasks">
        <h3>Tareas rápidas</h3>
        <ul>
          <li>✍️ Firmar 1 informe pendiente</li>
          <li>📂 Revisar resultados de laboratorio</li>
          <li>📅 Confirmar citas de mañana</li>
        </ul>
      </section>

      {/* Fila 1: Pacientes, Historias, Agenda */}
      <div className="cards-row three">
        <section className="dashboard-section">
          <h3>Pacientes</h3>
          <table className="patients-table">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Documento</th>
                <th>Diagnóstico</th>
                <th>Estado</th>
                <th>Acciones</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>Ana Gómez</td>
                <td>12345678</td>
                <td>Hipertensión</td>
                <td><span className="status green">Estable</span></td>
                <td><button>Ver Historia</button></td>
              </tr>
              <tr>
                <td>Carlos Pérez</td>
                <td>87654321</td>
                <td>Diabetes</td>
                <td><span className="status red">Urgente</span></td>
                <td><button>Ver Historia</button></td>
              </tr>
            </tbody>
          </table>
        </section>

        <section className="dashboard-section">
          <h3>Historias Clínicas</h3>
          <ul className="history-list">
            <li><strong>Ana Gómez</strong> – Última consulta: 20/10/2025</li>
            <li><strong>Carlos Pérez</strong> – Última consulta: 18/10/2025</li>
          </ul>
        </section>

        <section className="dashboard-section">
          <h3>Agenda Médica</h3>
          <div className="calendar-placeholder">📅 Calendario semanal/mensual</div>
        </section>
      </div>

      {/* Fila 2: Recetas, Mensajes, Reportes */}
      <div className="cards-row three">
        <section className="dashboard-section">
          <h3>Recetas</h3>
          <ul className="prescriptions-list">
            <li><strong>Ana Gómez</strong> – Enalapril 10mg</li>
            <li><strong>Carlos Pérez</strong> – Metformina 850mg</li>
          </ul>
        </section>

        <section className="dashboard-section">
          <h3>Mensajes</h3>
          <ul className="messages-list">
            <li>📩 Nueva cita asignada a Carlos Pérez</li>
            <li>📩 Resultado de laboratorio disponible</li>
          </ul>
        </section>

        <section className="dashboard-section">
          <h3>Reportes</h3>
          <ul className="reports-list">
            <li>Pacientes atendidos en octubre: 120</li>
            <li>Diagnósticos más frecuentes: Hipertensión, Diabetes</li>
            <li><button>📊 Exportar PDF</button></li>
          </ul>
        </section>
      </div>

      {/* Fila 3: Configuración */}
      <div className="cards-row one">
        <section className="dashboard-section">
          <h3>Configuración</h3>
          <button className="btn-secondary">Editar Perfil</button>
          <button className="btn-secondary">Cambiar Contraseña</button>
          <button className="btn-secondary">Disponibilidad</button>
        </section>
      </div>
    </div>
  );
}

export default DashboardProfesional;

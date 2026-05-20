import React, { useState, useEffect } from "react";
import "./DashboardProfesional.css";

function DashboardProfesional() {
  const profesional = JSON.parse(localStorage.getItem("profesional")) || {};
  const [citasHoy, setCitasHoy] = useState(0);
  const [pacientesActivos, setPacientesActivos] = useState(0);
  const [recetasPendientes, setRecetasPendientes] = useState(0);
  const [alertasMedicas, setAlertasMedicas] = useState(0);
  const [pacientesRecientes, setPacientesRecientes] = useState([]);
  const [historias, setHistorias] = useState([]);
  const [agenda, setAgenda] = useState([]);
  const [reportes, setReportes] = useState({ atendidos: 0, frecuentes: [] });

  useEffect(() => {
    const fetchData = async () => {
      try {
        const id = profesional.idprofesional;

        // Citas de hoy
        const resCitasHoy = await fetch(`http://127.0.0.1:7000/dashboard/citas/hoy/${id}`);
        const dataCitasHoy = await resCitasHoy.json();
        setCitasHoy(dataCitasHoy.length);

        // Pacientes activos
        const resPacientes = await fetch(`http://127.0.0.1:7000/dashboard/pacientes/${id}`);
        const dataPacientes = await resPacientes.json();
        setPacientesActivos(dataPacientes.length);

        // Pacientes recientes
        const resPacientesRecientes = await fetch(`http://127.0.0.1:7000/dashboard/pacientes/recientes/${id}`);
        const dataPacientesRecientes = await resPacientesRecientes.json();
        setPacientesRecientes(dataPacientesRecientes);

        // Recetas pendientes
        const resRecetas = await fetch(`http://127.0.0.1:7000/dashboard/recetas/pendientes/${id}`);
        const dataRecetas = await resRecetas.json();
        setRecetasPendientes(dataRecetas.length);

        // Alertas médicas (pacientes nuevos última semana)
        const resAlertas = await fetch(`http://127.0.0.1:7000/dashboard/pacientes/nuevos/${id}`);
        const dataAlertas = await resAlertas.json();
        setAlertasMedicas(dataAlertas.length);

        // Historias clínicas
        const resHistorias = await fetch(`http://127.0.0.1:7000/dashboard/historias/${id}`);
        const dataHistorias = await resHistorias.json();
        setHistorias(dataHistorias);

        // Agenda semanal
        const resAgenda = await fetch(`http://127.0.0.1:7000/dashboard/citas/semana/${id}`);
        const dataAgenda = await resAgenda.json();
        setAgenda(dataAgenda);

        // Reportes
        const resReportes = await fetch(`http://127.0.0.1:7000/dashboard/reportes/${id}`);
        const dataReportes = await resReportes.json();
        setReportes(dataReportes);

      } catch (err) {
        console.error("Error cargando dashboard:", err);
      }
    };

    if (profesional.idprofesional) {
      fetchData();
    }
  }, [profesional.idprofesional]);

  return (
    <div className="dashboard-container">
      {/* Resumen general */}
      <section className="summary-cards">
        <div className="card">
          <div className="card-icon">📅</div>
          <div className="card-text">{citasHoy} citas hoy</div>
        </div>
        <div className="card">
          <div className="card-icon">👥</div>
          <div className="card-text">{pacientesActivos} pacientes activos</div>
        </div>
        <div className="card">
          <div className="card-icon">💊</div>
          <div className="card-text">{recetasPendientes} recetas pendientes</div>
        </div>
        <div className="card">
          <div className="card-icon">⚠️</div>
          <div className="card-text">{alertasMedicas} pacientes nuevos esta semana</div>
        </div>
      </section>

      {/* Pacientes recientes */}
      <div className="cards-row three">
        <section className="dashboard-section">
          <h3>Pacientes recientes</h3>
          <table className="patients-table">
            <thead>
              <tr>
                <th>Nombre</th>
                <th>Documento</th>
              </tr>
            </thead>
            <tbody>
              {pacientesRecientes.map((p) => (
                <tr key={p.idpaciente}>
                  <td>{p.nombre}</td>
                  <td>{p.documento}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </section>

        {/* Historias clínicas */}
        <section className="dashboard-section">
          <h3>Historias Clínicas</h3>
          <ul className="history-list">
            {historias.map((h) => (
              <li key={h.idhistoria}>
                <strong>{h.paciente}</strong> – {new Date(h.fecha).toLocaleDateString()}
              </li>
            ))}
          </ul>
        </section>

        {/* Agenda médica */}
        <section className="dashboard-section">
          <h3>Agenda Médica</h3>
          <ul className="agenda-list">
            {agenda.map((cita) => {
              const fechaCompleta = cita.Fecha && cita.Hora 
                ? new Date(`${cita.Fecha}T${cita.Hora}`)
                : null;

              return (
                <li key={cita.IdCita}>
                  {fechaCompleta 
                    ? fechaCompleta.toLocaleString("es-CO", {
                        day: "2-digit",
                        month: "2-digit",
                        year: "numeric",
                        hour: "2-digit",
                        minute: "2-digit",
                        hour12: true
                      })
                    :"Sin fecha"}
                  {cita.paciente ? ` – ${cita.paciente}` : ""}
                </li>
              );
            })}
          </ul>
        </section>
      </div>

      {/* Recetas y Reportes */}
      <div className="cards-row two">
        <section className="dashboard-section">
          <h3>Recetas</h3>
          <ul className="prescriptions-list">
            {recetasPendientes === 0 ? (
              <li>No hay recetas pendientes</li>
            ) : (
              <li>{recetasPendientes} recetas pendientes</li>
            )}
          </ul>
        </section>

        <section className="dashboard-section">
          <h3>Reportes</h3>
          <ul className="reports-list">
            <li>Pacientes atendidos: {reportes.atendidos}</li>
            <li>
              {reportes.frecuentes.length > 0
                ? `Diagnósticos más frecuentes: ${reportes.frecuentes.join(", ")}`
                : "No hay diagnósticos registrados aún"}
            </li>
            <li><button>📊 Exportar PDF</button></li>
          </ul>
        </section>
      </div>

      {/* Configuración */}
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

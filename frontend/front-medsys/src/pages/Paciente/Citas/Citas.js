import React, { useState, useEffect } from "react";
import "./Citas.css";

function CitasPaciente() {
  const paciente = JSON.parse(localStorage.getItem("paciente"));
  console.log("Paciente desde localStorage:", paciente);

  const [citas, setCitas] = useState([]);
  const [citaActual, setCitaActual] = useState(null);
  const [loading, setLoading] = useState(false);

  // 🔹 Cargar todas las citas del paciente
  useEffect(() => {
    const fetchCitasPaciente = async () => {
      if (!paciente || !paciente.documento) {
        console.warn("Paciente no válido o sin documento.");
        return;
      }

      try {
        const res = await fetch(`http://127.0.0.1:7000/citamedica/paciente/${paciente.documento}`);
        const raw = await res.text();
        console.log("Respuesta cruda del backend:", raw);

        if (!res.ok) throw new Error("Error al obtener citas del paciente");

        const data = JSON.parse(raw);
        console.log("Citas recibidas:", data);
        setCitas(data);
      } catch (err) {
        console.error("Error cargando citas del paciente:", err);
      }
    };

    fetchCitasPaciente();
  }, [paciente]);

  // 🔹 Seleccionar la cita pendiente más próxima
  useEffect(() => {
    if (!citas || citas.length === 0) {
      console.warn("No hay citas cargadas.");
      return;
    }

    const hoy = new Date();
    const pendientesFuturas = citas
      .filter(c => c.estado?.toLowerCase() === "pendiente")
      .filter(c => {
        const fechaCita = new Date(c.fecha);
        console.log(`Evaluando cita: ${c.idcita} → ${c.fecha} → ${fechaCita}`);
        return fechaCita >= hoy;
      })
      .sort((a, b) => new Date(a.fecha) - new Date(b.fecha));

    console.log("Citas pendientes futuras:", pendientesFuturas);

    if (pendientesFuturas.length > 0) {
      setCitaActual(pendientesFuturas[0]);
    } else {
      setCitaActual(null);
    }
  }, [citas]);

  if (loading) return <p>Cargando citas...</p>;

  const citasPasadas = citas.filter(c => c.estado === "Completada" || c.estado === "Confirmada");

  return (
    <div className="citas-paciente-container">
      <h2>📅 Módulo de Citas</h2>

      {/* Cita actual */}
      <div className="cita-actual">
        <h3>📌 Próxima Cita</h3>
        {citaActual ? (
          <div className="cita-detalle">
            <p><strong>Fecha:</strong> {citaActual.fecha}</p>
            <p><strong>Hora:</strong> {citaActual.hora}</p>
            <p><strong>Profesional:</strong> {citaActual.nombre_profesional || citaActual.idprofesional}</p>
            <p><strong>Estado:</strong> {citaActual.estado}</p>
            <p><strong>Dirección:</strong> {citaActual.direccion_centro}</p>
            <p><strong>Ciudad:</strong> {citaActual.ciudad_centro}</p>

            {/* Botón para cancelar cita */}
            <button className="btn-cancelar" onClick={() => alert("Funcionalidad pendiente")}>
               Cancelar cita
            </button>
          </div>
        ) : (
          <p>No tienes citas futuras pendientes.</p>
        )}
      </div>

      {/* Historial de citas */}
      <div className="citas-pasadas">
        <h3>📖 Historial de Citas</h3>
        {citasPasadas.length === 0 ? (
          <p>No tienes citas pasadas.</p>
        ) : (
          <table className="citas-table">
            <thead>
              <tr>
                <th>Fecha</th>
                <th>Hora</th>
                <th>Profesional</th>
                <th>Estado</th>
              </tr>
            </thead>
            <tbody>
              {citasPasadas.map((c) => (
                <tr key={c.idcita}>
                  <td>{c.fecha}</td>
                  <td>{c.hora}</td>
                  <td>{c.nombre_profesional || c.idprofesional}</td>
                  <td>
                    <span className={`status ${c.estado?.toLowerCase()}`}>
                      {c.estado}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}

export default CitasPaciente;

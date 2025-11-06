import React, { useState, useEffect } from "react";
import "./Citas.css";

function Citas() {
  const profesional = JSON.parse(localStorage.getItem("profesional"));

  const [nuevaCita, setNuevaCita] = useState({
    documento: "",
    fecha: "",
    hora: "",
    motivo: "",
  });

  const [citas, setCitas] = useState([]); // 👈 estado para las citas

  // 🔎 función para cargar citas pendientes
  const fetchCitas = async () => {
    try {
      const res = await fetch("http://127.0.0.1:7000/citamedica/pendientes");
      if (!res.ok) throw new Error("Error al obtener citas");
      const data = await res.json();
      setCitas(data); // 👈 guardamos las citas en el estado
    } catch (err) {
      console.error("Error cargando citas:", err);
    }
  };

  // cargar citas al montar el componente
  useEffect(() => {
    fetchCitas();
  }, []);

  const handleChange = (e) => {
    setNuevaCita({ ...nuevaCita, [e.target.name]: e.target.value });
  };

  const handleAgendar = async (e) => {
    e.preventDefault();

    try {
      // 1. Buscar paciente por documento
      const resPaciente = await fetch(
        `http://127.0.0.1:7000/paciente/documento/${nuevaCita.documento}`
      );
      if (!resPaciente.ok) throw new Error("Paciente no encontrado");
      const paciente = await resPaciente.json();

      // 2. Construir payload de la cita
      const citaPayload = {
        idcita: crypto.randomUUID(),
        idpaciente: paciente.IdPaciente,
        idprofesional: profesional.idprofesional, // 👈 en minúscula
        fecha: nuevaCita.fecha,
        hora: nuevaCita.hora,
        motivo: nuevaCita.motivo || "Consulta general",
        estado: "Pendiente",
        activo: true,
      };

      console.log("Payload enviado:", citaPayload);

      // 3. Enviar al backend
      const res = await fetch("http://127.0.0.1:7000/citamedica/ingresarcitamedica", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(citaPayload),
      });

      const data = await res.json();
      console.log("Respuesta backend:", data);

      if (!res.ok || data.error) {
        throw new Error(data.error || JSON.stringify(data.detail));
      }

      alert("✅ Cita agendada con éxito");

      // 4. Resetear formulario
      setNuevaCita({ documento: "", fecha: "", hora: "", motivo: "" });

      // 5. Refrescar listado de citas desde el backend
      await fetchCitas();
    } catch (err) {
      console.error(err);
      alert("❌ No se pudo agendar la cita: " + err.message);
    }
  };

  return (
    <div className="citas-container">
      <h2>📅 Agenda de Citas</h2>
      <p>Aquí puedes gestionar tus citas con los pacientes.</p>

      {/* Tabla de citas dinámica */}
      <div className="citas-table-container">
        <h3>📖 Listado de Citas Pendientes</h3>
        <table className="citas-table">
          <thead>
            <tr>
              <th>Nombre</th>
              <th>Documento</th>
              <th>Teléfono</th>
              <th>Correo</th>
              <th>Fecha</th>
              <th>Hora</th>
              <th>Motivo</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {citas.length > 0 ? (
              citas.map((cita) => (
                <tr key={cita.IdCita || cita.idcita}>
                  <td>{cita.NombrePaciente || "—"}</td>
                  <td>{cita.Documento || "—"}</td>
                  <td>{cita.Telefono || "—"}</td>
                  <td>{cita.Correo || "—"}</td>
                  <td>{cita.Fecha}</td>
                  <td>{cita.Hora}</td>
                  <td>{cita.Motivo}</td>
                  <td>
                    <span className={`status ${cita.Estado ? cita.Estado.toLowerCase() : ""}`}>
                      {cita.Estado || "—"}
                    </span>
                  </td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="8">No hay citas pendientes</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>

      {/* Formulario para agendar nueva cita */}
      <div className="citas-form-container">
        <h3>➕ Agendar nueva cita</h3>
        <form className="citas-form" onSubmit={handleAgendar}>
          <div className="form-group">
            <label>Documento del Paciente</label>
            <input
              type="text"
              name="documento"
              value={nuevaCita.documento}
              onChange={handleChange}
              placeholder="Número de documento"
              required
            />
          </div>
          <div className="form-group">
            <label>Fecha</label>
            <input
              type="date"
              name="fecha"
              value={nuevaCita.fecha}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Hora</label>
            <input
              type="time"
              name="hora"
              value={nuevaCita.hora}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group" style={{ flex: "1 1 100%" }}>
            <label>Motivo</label>
            <input
              type="text"
              name="motivo"
              value={nuevaCita.motivo}
              onChange={handleChange}
              placeholder="Motivo de la consulta"
            />
          </div>
          <button type="submit" className="btn-agendar">Agendar Cita</button>
        </form>
      </div>
    </div>
  );
}

export default Citas;

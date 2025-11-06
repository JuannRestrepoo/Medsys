import React, { useState, useEffect } from "react";
import "./Historias.css";

function Historias() {
  const profesional = JSON.parse(localStorage.getItem("profesional"));

  const [nuevaHistoria, setNuevaHistoria] = useState({
    documento: "",
    fecha_creacion: "",
    antecedentes: "",
    observaciones: "",
  });

  const [historias, setHistorias] = useState([]);

  // 🔎 función para cargar historias clínicas recientes
  const fetchHistorias = async () => {
    try {
      const res = await fetch(
        `http://127.0.0.1:7000/historiaclinica/recientes/${profesional.idprofesional}`
      );
      if (!res.ok) throw new Error("Error al obtener historias clínicas");
      const data = await res.json();
      setHistorias(data);
    } catch (err) {
      console.error("Error cargando historias:", err);
    }
  };

  useEffect(() => {
    if (profesional?.idprofesional) {
      fetchHistorias();
    }
  }, [profesional?.idprofesional]);

  const handleChange = (e) => {
    setNuevaHistoria({ ...nuevaHistoria, [e.target.name]: e.target.value });
  };

  const handleAgregar = async (e) => {
    e.preventDefault();

    try {
      // 1. Buscar paciente por documento
      const resPaciente = await fetch(
        `http://127.0.0.1:7000/paciente/documento/${nuevaHistoria.documento}`
      );
      if (!resPaciente.ok) throw new Error("Paciente no encontrado");
      const paciente = await resPaciente.json();

      // 2. Construir payload de la historia clínica
      const historiaPayload = {
        idhistoria: crypto.randomUUID(),
        idpaciente: paciente.IdPaciente,
        idprofesional: profesional.idprofesional,
        fecha_creacion: nuevaHistoria.fecha_creacion,
        antecedentes: nuevaHistoria.antecedentes,
        observaciones: nuevaHistoria.observaciones,
        activo: true,
      };

      // 3. Enviar al backend
      const res = await fetch(
        "http://127.0.0.1:7000/historiaclinica/ingresarhistoriaclinica",
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(historiaPayload),
        }
      );

      const data = await res.json();
      if (!res.ok || data.error) {
        throw new Error(data.error || JSON.stringify(data.detail));
      }

      alert("✅ Historia clínica registrada con éxito");

      // 4. Resetear formulario
      setNuevaHistoria({
        documento: "",
        fecha_creacion: "",
        antecedentes: "",
        observaciones: "",
      });

      // 5. Refrescar listado
      await fetchHistorias();
    } catch (err) {
      console.error(err);
      alert("❌ No se pudo registrar la historia clínica: " + err.message);
    }
  };

  return (
    <div className="historias-container">
      <h2>🩺 Historias Clínicas</h2>
      <p>Aquí puedes registrar y consultar las historias clínicas de tus pacientes.</p>

      {/* Formulario para nueva historia */}
      <div className="historias-form-container">
        <h3>➕ Registrar nueva historia clínica</h3>
        <form className="historias-form" onSubmit={handleAgregar}>
          <div className="form-group">
            <label>Documento del Paciente</label>
            <input
              type="text"
              name="documento"
              value={nuevaHistoria.documento}
              onChange={handleChange}
              placeholder="Número de documento"
              required
            />
          </div>
          <div className="form-group">
            <label>Fecha</label>
            <input
              type="date"
              name="fecha_creacion"
              value={nuevaHistoria.fecha_creacion}
              onChange={handleChange}
              required
            />
          </div>
          <div className="form-group">
            <label>Antecedentes</label>
            <textarea
              name="antecedentes"
              value={nuevaHistoria.antecedentes}
              onChange={handleChange}
              placeholder="Antecedentes del paciente"
              required
            />
          </div>
          <div className="form-group">
            <label>Observaciones</label>
            <textarea
              name="observaciones"
              value={nuevaHistoria.observaciones}
              onChange={handleChange}
              placeholder="Observaciones del profesional"
              required
            />
          </div>
          <button type="submit" className="btn-agregar">Registrar Historia</button>
        </form>
      </div>

      {/* Tabla de historias recientes */}
      <div className="historias-table-container">
        <h3>📖 Historias Clínicas Recientes</h3>
        <table className="historias-table">
          <thead>
            <tr>
              <th>Paciente</th>
              <th>Documento</th>
              <th>Fecha</th>
              <th>Antecedentes</th>
              <th>Observaciones</th>
            </tr>
          </thead>
          <tbody>
            {historias.length > 0 ? (
              historias.map((historia) => (
                <tr key={historia.idhistoria}>
                  <td>{historia.paciente}</td>
                  <td>{historia.documento}</td>
                  <td>{historia.fecha}</td>
                  <td>{historia.antecedentes}</td>
                  <td>{historia.observaciones}</td>
                </tr>
              ))
            ) : (
              <tr>
                <td colSpan="5">No hay historias clínicas registradas</td>
              </tr>
            )}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Historias;

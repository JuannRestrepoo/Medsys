import React, { useState } from "react";
import "./Recetas.css";

function Recetas() {
  const profesional = JSON.parse(localStorage.getItem("profesional"));

  const [form, setForm] = useState({
    documento: "",
    medicamento: "",
    dosis: "",
    indicaciones: "",
  });

  const [mensaje, setMensaje] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegistrarReceta = async (e) => {
    e.preventDefault();

    try {
      // 1. Buscar paciente por documento
      const resPaciente = await fetch(
        `http://127.0.0.1:7000/paciente/documento/${form.documento}`
      );
      if (!resPaciente.ok) throw new Error("Paciente no encontrado");
      const paciente = await resPaciente.json();

      // 2. Construir payload de la receta
      const recetaPayload = {
        idreceta: crypto.randomUUID(),
        idpaciente: paciente.IdPaciente,
        idprofesional: profesional.idprofesional,
        medicamento: form.medicamento,
        dosis: form.dosis,
        indicaciones: form.indicaciones,
        activo: true,
      };

      console.log("Payload enviado:", recetaPayload);

      // 3. Enviar al backend
      const res = await fetch("http://127.0.0.1:7000/recetamedica/recetamedicapost", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(recetaPayload),
      });

      const data = await res.json();
      console.log("Respuesta backend:", data);

      if (!res.ok || data.error) {
        throw new Error(data.error || JSON.stringify(data.detail));
      }

      setMensaje("✅ Receta registrada con éxito");
      setError("");

      // 4. Resetear formulario
      setForm({ documento: "", medicamento: "", dosis: "", indicaciones: "" });
    } catch (err) {
      console.error(err);
      setError("❌ No se pudo registrar la receta: " + err.message);
      setMensaje("");
    }
  };

  return (
    <div className="recetas-container">
      <h2>💊 Registro de Recetas Médicas</h2>
      <p>El profesional puede registrar recetas médicas vinculadas a un paciente.</p>

      {/* Formulario para nueva receta */}
      <form className="receta-form" onSubmit={handleRegistrarReceta}>
        <div className="form-group">
          <label>Documento del Paciente</label>
          <input
            type="text"
            name="documento"
            value={form.documento}
            onChange={handleChange}
            placeholder="Número de documento"
            required
          />
        </div>
        <div className="form-group">
          <label>Medicamento</label>
          <input
            type="text"
            name="medicamento"
            value={form.medicamento}
            onChange={handleChange}
            placeholder="Ej: Ibuprofeno 400mg"
            required
          />
        </div>
        <div className="form-group">
          <label>Dosis</label>
          <input
            type="text"
            name="dosis"
            value={form.dosis}
            onChange={handleChange}
            placeholder="Ej: 1 tableta cada 8h"
            required
          />
        </div>
        <div className="form-group">
          <label>Indicaciones</label>
          <textarea
            name="indicaciones"
            value={form.indicaciones}
            onChange={handleChange}
            placeholder="Indicaciones para el paciente"
            required
          />
        </div>
        <button type="submit" className="btn-add">➕ Registrar Receta</button>
      </form>

      {/* Mensajes */}
      {mensaje && <p className="mensaje-exito">{mensaje}</p>}
      {error && <p className="mensaje-error">{error}</p>}
    </div>
  );
}

export default Recetas;

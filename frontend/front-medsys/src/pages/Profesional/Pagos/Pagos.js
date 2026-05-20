import React, { useState } from "react";
import "./Pagos.css";

function Pagos() {
  const profesional = JSON.parse(localStorage.getItem("profesional")) || {};
  const centro = JSON.parse(localStorage.getItem("centro")) || {};

  const [form, setForm] = useState({
    documento: "",
    servicio: "",
    fecha: "",
    monto: "",
  });
  const [mensaje, setMensaje] = useState("");
  const [error, setError] = useState("");

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  // 👉 Registrar cobro y generar factura inmediatamente
  const handleRegistrarCobro = async (e) => {
    e.preventDefault();
    try {
      // 1. Buscar paciente
      const resPaciente = await fetch(
        `http://127.0.0.1:7000/paciente/documento/${form.documento}`
      );
      if (!resPaciente.ok) throw new Error("Paciente no encontrado");
      const paciente = await resPaciente.json();

      // 2. Payload para registrar cobro
        const payload = {
          idpaciente: paciente.IdPaciente,
          idprofesional: profesional.idprofesional,
          idcentro: centro.idcentro,   // 👈 nuevo
          productoservicio: form.servicio,
          total: parseFloat(form.monto),
          activo: true,
          fecha: form.fecha || new Date().toISOString().split("T")[0],
        };
      console.log("Payload cobro:", payload);

      // 3. Registrar cobro
      const res = await fetch("http://127.0.0.1:7000/cobro/registrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(payload),
      });

      const data = await res.json();
      if (!res.ok || data.error) throw new Error(data.error);

      // 4. Generar factura automáticamente con el idcobro
      await handleGenerarFactura(data.idcobro);

      setMensaje("✅ Cobro y factura registrados correctamente");
      setError("");
      setForm({ documento: "", servicio: "", fecha: "", monto: "" });
    } catch (err) {
      setError("❌ Error al registrar cobro: " + err.message);
      setMensaje("");
    }
  };

  // 👉 Generar factura por idcobro
  const handleGenerarFactura = async (idcobro) => {
    try {
      const res = await fetch(
        `http://127.0.0.1:7000/cobro/${idcobro}/generar-factura`,
        { method: "POST" }
      );

      if (!res.ok) throw new Error("Error al generar factura");

      // Descargar/abrir archivo
      const blob = await res.blob();
      const url = window.URL.createObjectURL(blob);
      window.open(url, "_blank");
    } catch (err) {
      setError("❌ Error al generar factura: " + err.message);
    }
  };

  return (
    <div className="pagos-container">
      <h2>💳 Registro de Cobros</h2>
      <form className="pagos-form" onSubmit={handleRegistrarCobro}>
        <div className="form-group">
          <label>Documento del Paciente</label>
          <input
            type="text"
            name="documento"
            value={form.documento}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Servicio</label>
          <input
            type="text"
            name="servicio"
            value={form.servicio}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Fecha</label>
          <input
            type="date"
            name="fecha"
            value={form.fecha}
            onChange={handleChange}
          />
        </div>
        <div className="form-group">
          <label>Monto</label>
          <input
            type="number"
            name="monto"
            value={form.monto}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit" className="btn-registrar">
          📥 Registrar Cobro + Generar Factura
        </button>
      </form>

      {mensaje && <p className="mensaje-exito">{mensaje}</p>}
      {error && <p className="mensaje-error">{error}</p>}
    </div>
  );
}

export default Pagos;

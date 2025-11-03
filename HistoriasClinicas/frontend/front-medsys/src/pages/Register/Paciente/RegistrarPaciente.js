import React, { useState, useEffect } from "react";
import "./RegistrarPaciente.css";

function RegistrarPaciente() {
  const [ciudades, setCiudades] = useState([]);
  const [tiposDocumento, setTiposDocumento] = useState([]);

  const [form, setForm] = useState({
    nombre: "",
    documento: "",
    edad: "",
    genero: "",
    telefono: "",
    correo: "",
    direccion: "",
    idciudad: "",
    idtipodocumento: "",
    grupo_sanguineo: "",
    alergias: "",
    antecedentes: ""
  });

  // Cargar ciudades desde el backend
  useEffect(() => {
    fetch("http://127.0.0.1:7000/ciudad/consultarciudad")
      .then((res) => res.json())
      .then((data) => setCiudades(data))
      .catch((err) => console.error("Error cargando ciudades:", err));
  }, []);

  // Cargar tipos de documento desde el backend
  useEffect(() => {
    fetch("http://127.0.0.1:7000/tipodocumento/consultar")
      .then((res) => res.json())
      .then((data) => setTiposDocumento(data))
      .catch((err) => console.error("Error cargando tipos de documento:", err));
  }, []);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:7000/paciente/registrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(form)
      });

      const data = await response.json();

      if (data.mensaje) {
        alert("✅ Paciente registrado correctamente");
        setForm({
          nombre: "",
          documento: "",
          edad: "",
          genero: "",
          telefono: "",
          correo: "",
          direccion: "",
          idciudad: "",
          idtipodocumento: "",
          grupo_sanguineo: "",
          alergias: "",
          antecedentes: ""
        });
      } else {
        alert("❌ Error: " + data.error);
      }
    } catch (err) {
      alert("❌ No se pudo conectar con el servidor");
    }
  };

  return (
    <div className="registrar-container">
      <h2>🧍 Registrar Paciente</h2>
      <p>Completa la información para registrar un nuevo paciente.</p>

      <form className="registrar-form" onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Nombre completo</label>
          <input
            type="text"
            name="nombre"
            value={form.nombre}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Tipo de Documento</label>
          <select
            name="idtipodocumento"
            value={form.idtipodocumento}
            onChange={handleChange}
            required
          >
            <option value="">Seleccione tipo...</option>
            {tiposDocumento.map((td) => (
              <option key={td.IdTipoDocumento} value={td.IdTipoDocumento}>
                {td.Nombre}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Número de Documento</label>
          <input
            type="text"
            name="documento"
            value={form.documento}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Edad</label>
          <input
            type="number"
            name="edad"
            value={form.edad}
            onChange={handleChange}
            required
          />
        </div>
        <div className="form-group">
          <label>Fecha de Nacimiento</label>
          <input
            type="date"
            name="fecha_nacimiento"
            value={form.fecha_nacimiento}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Género</label>
          <select name="genero" value={form.genero} onChange={handleChange} required>
            <option value="">Seleccione...</option>
            <option value="Femenino">Femenino</option>
            <option value="Masculino">Masculino</option>
            <option value="Otro">Otro</option>
          </select>
        </div>

        <div className="form-group">
          <label>Teléfono</label>
          <input
            type="text"
            name="telefono"
            value={form.telefono}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Correo electrónico</label>
          <input
            type="email"
            name="correo"
            value={form.correo}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Dirección</label>
          <input
            type="text"
            name="direccion"
            value={form.direccion}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Ciudad</label>
          <select
            name="idciudad"
            value={form.idciudad}
            onChange={handleChange}
            required
          >
            <option value="">Seleccione ciudad...</option>
            {ciudades.map((c) => (
              <option key={c.IdCiudad} value={c.IdCiudad}>
                {c.NombreCiudad}
              </option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <label>Grupo sanguíneo</label>
          <input
            type="text"
            name="grupo_sanguineo"
            value={form.grupo_sanguineo}
            onChange={handleChange}
            required
          />
        </div>

        <div className="form-group">
          <label>Alergias</label>
          <input
            type="text"
            name="alergias"
            value={form.alergias}
            onChange={handleChange}
          />
        </div>

        <div className="form-group">
          <label>Antecedentes</label>
          <input
            type="text"
            name="antecedentes"
            value={form.antecedentes}
            onChange={handleChange}
          />
        </div>

        <button type="submit" className="btn-save">Registrar Paciente</button>
      </form>
    </div>
  );
}

export default RegistrarPaciente;

import React, { useState, useEffect } from "react";
import "./Resultados.css";

function Resultados() {
  const profesional = JSON.parse(localStorage.getItem("profesional"));
  const [resultados, setResultados] = useState([]);
  const [form, setForm] = useState({
    documento: "",
    titulo: "",
    descripcion: "",
    archivo: null,
  });
  const [mensaje, setMensaje] = useState("");
  const [error, setError] = useState("");

  useEffect(() => {
    const fetchResultados = async () => {
      if (!form.documento) return;
      try {
        const res = await fetch(`http://127.0.0.1:7000/resultados/paciente/${form.documento}`);
        if (!res.ok) throw new Error("Error al obtener resultados");
        const data = await res.json();
        setResultados(data);
      } catch (err) {
        console.error("Error cargando resultados:", err);
      }
    };
    fetchResultados();
  }, [form.documento]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setForm({ ...form, [name]: value });
  };

  const handleFileChange = (e) => {
    setForm({ ...form, archivo: e.target.files[0] });
  };

  const handleSubirResultado = async (e) => {
    e.preventDefault();
    try {
      // 1. Subir archivo al backend
      let nombreArchivo = null;
      if (form.archivo) {
        const formData = new FormData();
        formData.append("file", form.archivo);

        const resArchivo = await fetch("http://127.0.0.1:7000/resultados/subir-archivo", {
          method: "POST",
          body: formData,
        });
        if (!resArchivo.ok) throw new Error("Error al subir archivo");
        const dataArchivo = await resArchivo.json();
        nombreArchivo = dataArchivo.archivo;
      }

      // 2. Buscar paciente por documento
      const resPaciente = await fetch(`http://127.0.0.1:7000/paciente/documento/${form.documento}`);
      if (!resPaciente.ok) throw new Error("Paciente no encontrado");
      const paciente = await resPaciente.json();

      // 3. Construir payload resultado
      const resultadoPayload = {
        idresultado: crypto.randomUUID(),
        idpaciente: paciente.IdPaciente,
        idprofesional: profesional.idprofesional,
        titulo: form.titulo,
        descripcion: form.descripcion,
        archivo: nombreArchivo,
        activo: true,
      };

      // 4. Registrar resultado en la BD
      const res = await fetch("http://127.0.0.1:7000/resultados/registrar", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(resultadoPayload),
      });

      const data = await res.json();
      if (!res.ok || data.error) {
        throw new Error(data.error || JSON.stringify(data.detail));
      }

      setMensaje("✅ Resultado registrado con éxito");
      setError("");
      setForm({ documento: "", titulo: "", descripcion: "", archivo: null });

      // Refrescar lista
      setResultados((prev) => [...prev, resultadoPayload]);
    } catch (err) {
      console.error(err);
      setError("❌ No se pudo registrar el resultado: " + err.message);
      setMensaje("");
    }
  };

  return (
    <div className="resultados-container">
      <h2>📂 Resultados y Documentos</h2>
      <p>Sube y consulta los resultados médicos de tus pacientes.</p>

      {/* Formulario */}
      <form className="resultado-form" onSubmit={handleSubirResultado}>
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
          <label>Título del resultado</label>
          <input
            type="text"
            name="titulo"
            value={form.titulo}
            onChange={handleChange}
            placeholder="Ej: Examen de sangre"
            required
          />
        </div>
        <div className="form-group">
          <label>Descripción</label>
          <textarea
            name="descripcion"
            value={form.descripcion}
            onChange={handleChange}
            placeholder="Detalles del resultado"
          />
        </div>
        <div className="form-group">
          <label>Archivo</label>
          <input type="file" onChange={handleFileChange} />
        </div>
        <button type="submit" className="btn-upload">📤 Subir Resultado</button>
      </form>

      {/* Mensajes */}
      {mensaje && <p className="mensaje-exito">{mensaje}</p>}
      {error && <p className="mensaje-error">{error}</p>}

      {/* Tabla */}
      <div className="resultados-table-container">
        <table className="resultados-table">
          <thead>
            <tr>
              <th>Título</th>
              <th>Descripción</th>
              <th>Archivo</th>
              <th>Profesional</th>
              <th>Estado</th>
            </tr>
          </thead>
          <tbody>
            {resultados.map((r) => (
              <tr key={r.idresultado}>
                <td>{r.titulo}</td>
                <td>{r.descripcion}</td>
                <td>
                  {r.archivo ? (
                    <a href={`http://127.0.0.1:7000/uploads/${r.archivo}`} target="_blank" rel="noopener noreferrer">
                      {r.archivo}
                    </a>
                  ) : (
                    "Sin archivo"
                  )}
                </td>
                <td>{r.nombre_profesional}</td>
                <td>
                  <span className={`status ${r.activo ? "activo" : "inactivo"}`}>
                    {r.activo ? "Activo" : "Inactivo"}
                  </span>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Resultados;

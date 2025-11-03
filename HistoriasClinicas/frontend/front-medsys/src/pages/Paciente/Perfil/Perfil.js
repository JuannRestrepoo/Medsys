import React, { useState } from "react";
import "./Perfil.css";

function PerfilPaciente() {
  const [perfil, setPerfil] = useState({
    nombre: "Ana Gómez",
    documento: "12345678",
    edad: 32,
    genero: "Femenino",
    telefono: "3001234567",
    correo: "ana.gomez@correo.com",
    direccion: "Calle 123 #45-67",
    eps: "Salud Total",
  });

  const [editando, setEditando] = useState(false);

  const handleChange = (e) => {
    setPerfil({ ...perfil, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setEditando(false);
    alert("✅ Perfil actualizado correctamente");
    // Aquí luego harías un PUT al backend con axios/fetch
  };

  return (
    <div className="perfil-container">
      <h2>⚙️ Mi Perfil</h2>
      <p>Consulta y actualiza tu información personal.</p>

      {!editando ? (
        <div className="perfil-info">
          <p><strong>Nombre:</strong> {perfil.nombre}</p>
          <p><strong>Documento:</strong> {perfil.documento}</p>
          <p><strong>Edad:</strong> {perfil.edad}</p>
          <p><strong>Género:</strong> {perfil.genero}</p>
          <p><strong>Teléfono:</strong> {perfil.telefono}</p>
          <p><strong>Correo:</strong> {perfil.correo}</p>
          <p><strong>Dirección:</strong> {perfil.direccion}</p>
          <p><strong>EPS:</strong> {perfil.eps}</p>
          <button className="btn-edit" onClick={() => setEditando(true)}>
            Editar Perfil
          </button>
        </div>
      ) : (
        <form className="perfil-form" onSubmit={handleSubmit}>
          <div className="form-group">
            <label>Nombre</label>
            <input type="text" name="nombre" value={perfil.nombre} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Documento</label>
            <input type="text" name="documento" value={perfil.documento} onChange={handleChange} disabled />
          </div>
          <div className="form-group">
            <label>Edad</label>
            <input type="number" name="edad" value={perfil.edad} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Género</label>
            <select name="genero" value={perfil.genero} onChange={handleChange}>
              <option value="Femenino">Femenino</option>
              <option value="Masculino">Masculino</option>
              <option value="Otro">Otro</option>
            </select>
          </div>
          <div className="form-group">
            <label>Teléfono</label>
            <input type="text" name="telefono" value={perfil.telefono} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Correo</label>
            <input type="email" name="correo" value={perfil.correo} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>Dirección</label>
            <input type="text" name="direccion" value={perfil.direccion} onChange={handleChange} />
          </div>
          <div className="form-group">
            <label>EPS</label>
            <input type="text" name="eps" value={perfil.eps} onChange={handleChange} />
          </div>
          <button type="submit" className="btn-save">Guardar Cambios</button>
          <button type="button" className="btn-cancel" onClick={() => setEditando(false)}>Cancelar</button>
        </form>
      )}
    </div>
  );
}

export default PerfilPaciente;

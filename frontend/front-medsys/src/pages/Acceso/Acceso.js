import React from "react";
import { useNavigate } from "react-router-dom";
import "./Acceso.css";

function Acceso() {
  const navigate = useNavigate();

  return (
    <div className="acceso-container">
      <div className="acceso-card">
        <h2>Acceso al Sistema</h2>
        <p>Selecciona tu rol para iniciar sesión</p>

        <div className="acceso-buttons">
          <button
            className="btn-acceso profesional"
            onClick={() => navigate("/profesional/login")}
          >
            Soy Profesional
          </button>

          <button
            className="btn-acceso paciente"
            onClick={() => navigate("/paciente/login")}
          >
            Soy Paciente
          </button>
        </div>

        <div className="extra-links">
          <a href="/">← Volver al inicio</a>
        </div>
      </div>
    </div>
  );
}

export default Acceso;

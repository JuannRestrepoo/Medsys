import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginPaciente.css";

function LoginPaciente() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await fetch("http://127.0.0.1:7000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          correo: email,
          contrasena: password, // el paciente ingresa su documento como contraseña
        }),
      });

      const data = await response.json();

      if (data.mensaje) {
        // ✅ Login exitoso
        console.log("Login correcto:", data);

        // Puedes guardar info en localStorage si quieres mantener sesión
        localStorage.setItem("paciente", JSON.stringify(data));

        navigate("/paciente/portal");
      } else {
        // ❌ Error en login
        setError(data.error || "Credenciales inválidas");
      }
    } catch (err) {
      setError("No se pudo conectar con el servidor");
    }
  };

  return (
    <div className="login-paciente-container">
      <div className="login-card">
        <h2>Acceso del Paciente</h2>
        <p>Ingresa tu correo y contraseña para ver tu información médica</p>

        <form onSubmit={handleLogin} className="login-form">
          <label htmlFor="email">Correo electrónico</label>
          <input
            type="email"
            id="email"
            placeholder="ejemplo@correo.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label htmlFor="password">Contraseña</label>
          <input
            type="password"
            id="password"
            placeholder="••••••••"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          {error && <p className="error-message">{error}</p>}

          <button type="submit" className="btn-login">Iniciar sesión</button>
        </form>

        <div className="extra-links">
          <a href="/">← Volver al inicio</a>
        </div>
      </div>
    </div>
  );
}

export default LoginPaciente;

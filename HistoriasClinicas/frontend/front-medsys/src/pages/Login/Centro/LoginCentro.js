import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./LoginCentro.css";

function LoginCentro() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate(); // 👈 declarado

  const handleLogin = async (e) => {
    e.preventDefault();

    try {
      const response = await fetch("http://127.0.0.1:7000/auth/login", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          correo: email,
          contrasena: password
        })
      });

      const data = await response.json();

      if (data.mensaje) {
        // ✅ Guardar sesión en localStorage
        localStorage.setItem("usuario", JSON.stringify(data));

        // ✅ Redirigir al dashboard
        navigate("/profesional/dashboard");
      } else {
        alert(data.error || "Error en el login");
      }
    } catch (err) {
      alert("No se pudo conectar con el servidor");
    }
  };
  return (
    <div className="login-centro-container">
      <div className="login-card">
        <h2>Acceso del Profesional</h2>
        <form onSubmit={handleLogin} className="login-form">
          <label>Correo electrónico</label>
          <input
            type="email"
            placeholder="ejemplo@correo.com"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />

          <label>Contraseña</label>
          <input
            type="password"
            placeholder="••••••••"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />

          <button type="submit" className="btn-login">
            Iniciar sesión
          </button>
        </form>
      </div>
    </div>
  );
}

export default LoginCentro;

// src/components/RutaProtegidaPaciente.jsx
import React from "react";
import { Navigate, useLocation } from "react-router-dom";

function RutaProtegidaPaciente({ children }) {
  const location = useLocation();

  // Leer sesión segura
  let paciente = null;
  try {
    const raw = localStorage.getItem("paciente");
    paciente = raw ? JSON.parse(raw) : null;
  } catch {
    paciente = null;
  }

  const isLoggedIn = Boolean(paciente && paciente.idusuario);

  if (!isLoggedIn) {
    // Redirige al login y recuerda la ruta que intentaba acceder
    return <Navigate to="/paciente/login" replace state={{ from: location }} />;
  }

  return children;
}

export default RutaProtegidaPaciente;

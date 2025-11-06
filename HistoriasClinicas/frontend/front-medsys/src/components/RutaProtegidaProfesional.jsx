import React from "react";
import { Navigate, useLocation } from "react-router-dom";

function RutaProtegidaProfesional({ children }) {
  const location = useLocation();

  // Leer sesión segura del profesional
  let profesional = null;
  try {
    const raw = localStorage.getItem("profesional");
    profesional = raw ? JSON.parse(raw) : null;
  } catch {
    profesional = null;
  }

  const isLoggedIn = Boolean(profesional && profesional.idusuario);

  if (!isLoggedIn) {
    // Redirige al login de profesional y recuerda la ruta que intentaba acceder
    return <Navigate to="/profesional/login" replace state={{ from: location }} />;
  }

  return children;
}

export default RutaProtegidaProfesional;

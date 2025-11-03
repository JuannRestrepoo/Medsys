
import React from "react";
import { Navigate } from "react-router-dom";

function RutaProtegidaPaciente({ children }) {
  const paciente = JSON.parse(localStorage.getItem("paciente") || "{}");

  if (!paciente.idusuario) {
    return <Navigate to="/paciente/login" replace />;
  }

  return children;
}

export default RutaProtegidaPaciente;

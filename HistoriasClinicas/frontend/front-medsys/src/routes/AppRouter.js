// src/routes/AppRouter.js
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

// Páginas generales
import LandingPage from "../pages/LandingPage/LandingPage";
import Acceso from "../pages/Acceso/Acceso";

// Login
import LoginCentro from "../pages/Login/Centro/LoginCentro";
import LoginPaciente from "../pages/Login/Paciente/LoginPaciente";

// Registrar
import RegistrarPaciente from "../pages/Register/Paciente/RegistrarPaciente";

// Dashboard Profesional
import ProfesionalLayout from "../layouts/ProfesionalLayout/ProfesionalLayout";
import DashboardProfesional from "../pages/DashboardProfesional/DashboardProfesional";
import Citas from "../pages/Profesional/Citas/Citas";
import Historias from "../pages/Profesional/Historias/Historias";
import Recetas from "../pages/Profesional/Recetas/Recetas";
import Resultados from "../pages/Profesional/Resultados/Resultados";
import Mensajes from "../pages/Profesional/Mensajes/Mensajes";
import Pagos from "../pages/Profesional/Pagos/Pagos";
import Configuracion from "../pages/Profesional/Configuracion/Configuracion";

// Portal Paciente y módulos (solo consulta)
import PacienteLayout from "../layouts/PacienteLayout/PacienteLayout";
import PortalPaciente from "../pages/PortalPaciente/PortalPaciente";
import CitasPaciente from "../pages/Paciente/Citas/Citas";
import HistorialPaciente from "../pages/Paciente/Historial/Historial";
import RecetasPaciente from "../pages/Paciente/Recetas/Recetas";
import ResultadosPaciente from "../pages/Paciente/Resultados/Resultados";
import MensajesPaciente from "../pages/Paciente/Mensajes/Mensajes";
import PagosPaciente from "../pages/Paciente/Pagos/Pagos";
import PerfilPaciente from "../pages/Paciente/Perfil/Perfil";

// Protección
import RutaProtegidaPaciente from "../components/RutaProtegidaPaciente";
import RutaProtegidaProfesional from "../components/RutaProtegidaProfesional";

function AppRouter() {
  return (
    <Router>
      <Routes>
        {/* Rutas públicas */}
        <Route path="/" element={<LandingPage />} />
        <Route path="/acceso" element={<Acceso />} />

        {/* Login */}
        <Route path="/profesional/login" element={<LoginCentro />} />
        <Route path="/paciente/login" element={<LoginPaciente />} />

        {/* Bloque protegido: todo /paciente/* requiere sesión */}
        <Route
          path="/paciente"
          element={
            <RutaProtegidaPaciente>
              <PacienteLayout />
            </RutaProtegidaPaciente>
          }
        >
          <Route path="portal" element={<PortalPaciente />} />
          <Route path="citas" element={<CitasPaciente />} />
          <Route path="historial" element={<HistorialPaciente />} />
          <Route path="recetas" element={<RecetasPaciente />} />
          <Route path="resultados" element={<ResultadosPaciente />} />
          <Route path="mensajes" element={<MensajesPaciente />} />
          <Route path="pagos" element={<PagosPaciente />} />
          <Route path="perfil" element={<PerfilPaciente />} />
        </Route>

        {/* Bloque protegido: todo /profesional/* requiere sesión */}
        <Route
          path="/profesional"
          element={
            <RutaProtegidaProfesional>
              <ProfesionalLayout />
            </RutaProtegidaProfesional>
          }
        >
          <Route path="dashboard" element={<DashboardProfesional />} />
          <Route path="citas" element={<Citas />} /> {/* 🔹 Aquí agenda el profesional */}
          <Route path="historias" element={<Historias />} />
          <Route path="recetas" element={<Recetas />} />
          <Route path="resultados" element={<Resultados />} />
          <Route path="mensajes" element={<Mensajes />} />
          <Route path="pagos" element={<Pagos />} />
          <Route path="configuracion" element={<Configuracion />} />
          <Route path="pacientes/registrar" element={<RegistrarPaciente />} />
        </Route>

        {/* Fallback */}
        <Route path="*" element={<LandingPage />} />
      </Routes>
    </Router>
  );
}

export default AppRouter;

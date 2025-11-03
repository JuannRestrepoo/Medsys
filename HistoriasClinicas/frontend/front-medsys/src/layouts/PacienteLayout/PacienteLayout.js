import React from "react";
import { Outlet, useNavigate } from "react-router-dom";
import "./PacienteLayout.css";

function PacienteLayout() {
  const navigate = useNavigate();

  return (
    <div className="paciente-layout">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>MedSys Paciente</h2>
        </div>
        <nav className="sidebar-nav">
          <ul>
            <li onClick={() => navigate("/paciente/portal")}>🏠 Inicio</li>
            <li onClick={() => navigate("/paciente/citas")}>📅 Mis Citas</li>
            <li onClick={() => navigate("/paciente/historial")}>🧾 Historial Médico</li>
            <li onClick={() => navigate("/paciente/recetas")}>💊 Mis Recetas</li>
            <li onClick={() => navigate("/paciente/resultados")}>📂 Resultados</li>
            <li onClick={() => navigate("/paciente/mensajes")}>💬 Mensajes</li>
            <li onClick={() => navigate("/paciente/pagos")}>💳 Pagos</li>
            <li onClick={() => navigate("/paciente/perfil")}>⚙️ Perfil</li>
          </ul>
        </nav>
      </aside>

      {/* Contenido principal */}
      <div className="main-content">
        {/* Topbar */}
        <header className="topbar">
          <div className="topbar-left">
            <h2>Portal del Paciente</h2>
            <p>Bienvenido a tu espacio personal de salud</p>
          </div>
          <div className="topbar-center">
            <input
              type="text"
              placeholder="Buscar citas, recetas, resultados..."
              className="search-bar"
            />
          </div>
          <div className="topbar-right">
            <div className="notifications">
              🔔 <span className="badge">2</span>
            </div>
            <button
              className="btn-secondary"
              onClick={() => navigate("/paciente/perfil")}
            >
              Mi Perfil
            </button>
          </div>
        </header>

        {/* Aquí se renderiza el contenido de cada módulo */}
        <main className="content-area">
          <Outlet />
        </main>
      </div>
    </div>
  );
}

export default PacienteLayout;

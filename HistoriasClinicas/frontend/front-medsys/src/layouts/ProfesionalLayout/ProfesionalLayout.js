import React from "react";
import { Outlet, useNavigate } from "react-router-dom";
import "./ProfesionalLayout.css";

function ProfesionalLayout() {
  const navigate = useNavigate();

  const handleLogout = () => {
    // Limpia la sesión del profesional
    localStorage.removeItem("profesional");
    // Si también quieres limpiar pacientes por seguridad:
    localStorage.removeItem("paciente");
    // Redirige al login general o al de profesional
    navigate("/profesional/login");
  };

  return (
    <div className="profesional-layout">
      {/* Sidebar */}
      <aside className="sidebar">
        <div className="sidebar-header">
          <h2>MedSys Pro</h2>
        </div>
        <nav className="sidebar-nav">
          <ul>
            <li onClick={() => navigate("/profesional/dashboard")}>🏠 Dashboard</li>
            <li onClick={() => navigate("/profesional/citas")}>📅 Citas</li>
            <li onClick={() => navigate("/profesional/historias")}>🧾 Historias Clínicas</li>
            <li onClick={() => navigate("/profesional/recetas")}>💊 Recetas</li>
            <li onClick={() => navigate("/profesional/resultados")}>📂 Resultados</li>
            <li onClick={() => navigate("/profesional/mensajes")}>💬 Mensajes</li>
            <li onClick={() => navigate("/profesional/pagos")}>💳 Pagos</li>
            <li onClick={() => navigate("/profesional/configuracion")}>⚙️ Configuración</li>
          </ul>
        </nav>
      </aside>

      {/* Contenido principal */}
      <div className="main-content">
        {/* Topbar */}
        <header className="topbar">
          <div className="topbar-left">
            <h2>Panel del Profesional</h2>
            <p>Gestión de pacientes y agenda</p>
          </div>
          <div className="topbar-center">
            <input
              type="text"
              placeholder="Buscar pacientes, citas o documentos..."
              className="search-bar"
            />
          </div>
          <div className="topbar-right">
            <button
              className="btn-primary"
              onClick={() => navigate("/profesional/pacientes/registrar")}
            >
              + Registrar Paciente
            </button>
            <div className="notifications">
              🔔 <span className="badge">3</span>
            </div>
            <button
              className="btn-secondary"
              onClick={() => navigate("/profesional/configuracion")}
            >
              Perfil
            </button>
            <button className="btn-logout" onClick={handleLogout}>
              🚪 Cerrar sesión
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

export default ProfesionalLayout;

import React from "react";
import { useNavigate } from "react-router-dom";
import "./PortalPaciente.css";

function PortalPaciente() {
  const navigate = useNavigate();

  return (
    <div className="portal-paciente">
      {/* Panel de resumen */}
      <section className="summary-cards">
        <div className="card">📅 1 cita próxima</div>
        <div className="card">💊 2 recetas activas</div>
        <div className="card">🧾 1 factura pendiente</div>
      </section>

      {/* Fila 1 */}
      <div className="cards-row three">
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/citas")}
        >
          <h3>📅 Mis Citas</h3>
          <p>Gestiona tus citas médicas</p>
        </section>
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/historial")}
        >
          <h3>🧾 Historial Clínico</h3>
          <p>Consulta tus atenciones previas</p>
        </section>
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/recetas")}
        >
          <h3>💊 Recetas y Tratamientos</h3>
          <p>Revisa tus medicamentos activos</p>
        </section>
      </div>

      {/* Fila 2 */}
      <div className="cards-row three">
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/resultados")}
        >
          <h3>📂 Resultados</h3>
          <p>Accede a tus exámenes y documentos</p>
        </section>
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/mensajes")}
        >
          <h3>💬 Mensajes</h3>
          <p>Comunícate con tu profesional</p>
        </section>
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/pagos")}
        >
          <h3>💳 Pagos y Facturación</h3>
          <p>Consulta tus facturas y pagos</p>
        </section>
      </div>

      {/* Fila 3 */}
      <div className="cards-row one">
        <section
          className="dashboard-section clickable"
          onClick={() => navigate("/paciente/perfil")}
        >
          <h3>🧍 Perfil Personal</h3>
          <p>Actualiza tu información y preferencias</p>
        </section>
      </div>

      {/* Consejo de bienestar */}
      <div className="cards-row one">
        <section className="dashboard-section">
          <h3>Consejo de Bienestar</h3>
          <p>💡 Hidrátate correctamente antes de tu sesión de fisioterapia.</p>
        </section>
      </div>
    </div>
  );
}

export default PortalPaciente;

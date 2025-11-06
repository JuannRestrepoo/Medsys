import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./PortalPaciente.css";

function PortalPaciente() {
  const navigate = useNavigate();
  const paciente = JSON.parse(localStorage.getItem("paciente")) || {};

  const [citasProximas, setCitasProximas] = useState(0);
  const [recetasActivas, setRecetasActivas] = useState(0);
  const [resultadosPendientes, setResultadosPendientes] = useState(0);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const id = paciente.IdPaciente || paciente.idpaciente;

        if (!id) {
          console.warn("No se encontró IdPaciente en localStorage");
          return;
        }

        // 📅 Citas próximas
        const resCitas = await fetch(`http://127.0.0.1:7000/paciente/citas/proximas/${id}`);
        const dataCitas = await resCitas.json();
        setCitasProximas(Array.isArray(dataCitas) ? dataCitas.length : 0);

        // 💊 Recetas activas
        const resRecetas = await fetch(`http://127.0.0.1:7000/paciente/recetas/activas/${id}`);
        const dataRecetas = await resRecetas.json();
        setRecetasActivas(Array.isArray(dataRecetas) ? dataRecetas.length : 0);

        // 📂 Resultados pendientes
        const resResultados = await fetch(`http://127.0.0.1:7000/paciente/resultados/pendientes/${id}`);
        const dataResultados = await resResultados.json();
        setResultadosPendientes(
          dataResultados && typeof dataResultados.pendientes === "number"
            ? dataResultados.pendientes
            : 0
        );

      } catch (err) {
        console.error("Error cargando portal paciente:", err);
      }
    };

    fetchData();
  }, [paciente]);


  return (
    <div className="portal-paciente">
      {/* Panel de resumen */}
      <section className="summary-cards">
        <div className="card">
          <div className="card-icon">📅</div>
          <div className="card-text">{citasProximas} cita(s) próxima(s)</div>
        </div>
        <div className="card">
          <div className="card-icon">💊</div>
          <div className="card-text">{recetasActivas} recetas activas</div>
        </div>
        <div className="card">
          <div className="card-icon">📂</div>
          <div className="card-text">{resultadosPendientes} resultado(s) pendiente(s) de ver o descargar</div>
        </div>
      </section>

      {/* Fila 1 */}
      <div className="cards-row three">
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/citas")}>
          <h3>📅 Mis Citas</h3>
          <p>Gestiona tus citas médicas</p>
        </section>
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/historial")}>
          <h3>🧾 Historias Clínicas</h3>
          <p>Consulta tus atenciones previas</p>
        </section>
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/recetas")}>
          <h3>💊 Recetas y Tratamientos</h3>
          <p>Revisa tus medicamentos activos</p>
        </section>
      </div>

      {/* Fila 2 */}
      <div className="cards-row three">
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/resultados")}>
          <h3>📂 Resultados</h3>
          <p>Accede a tus exámenes y documentos</p>
        </section>
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/mensajes")}>
          <h3>💬 Mensajes</h3>
          <p>Comunícate con tu profesional</p>
        </section>
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/pagos")}>
          <h3>💳 Pagos y Facturación</h3>
          <p>Consulta tus facturas y pagos</p>
        </section>
      </div>

      {/* Fila 3 */}
      <div className="cards-row one">
        <section className="dashboard-section clickable" onClick={() => navigate("/paciente/perfil")}>
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

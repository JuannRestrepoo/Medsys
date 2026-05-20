import React from "react";
import "./LandingPage.css";

function LandingPage() {
  return (
    <div className="landing">
      {/* Header */}
      <header className="header">
        <div className="logo">MedSys</div>
        <nav className="nav">
          <a href="#inicio">Inicio</a>
          <a href="#servicios">Servicios</a>
          <a href="#nosotros">Sobre Nosotros</a>
          <a href="#contacto">Contacto</a>
        </nav>
        <div className="actions">
          <a href="/acceso" className="btn-acceso">Acceso</a>
        </div>
      </header>

      {/* Hero Section */}
      <section className="hero" id="inicio">
        <div className="hero-text">
          <h1>Gestiona tu centro de salud, simplifica tu vida</h1>
          <p>
            MedSys es la plataforma todo en uno para pequeñas y medianas empresas del área de la salud. 
            Agenda citas, gestiona clientes y controla tus cobros en un solo lugar.
          </p>
          <a href="/acceso" className="btn-primary">Comienza tu prueba gratis</a>
        </div>
        <div className="hero-image">
          <img
            src="https://via.placeholder.com/450x300"
            alt="Vista previa de MedSys"
          />
        </div>
      </section>

      {/* ¿Para quién es MedSys? */}
      <section className="audience" id="servicios">
        <h2>¿Para quién es MedSys?</h2>
        <p>
          MedSys está diseñado para cualquier empresa de salud que quiera simplificar su gestión. 
          Desde consultorios independientes hasta clínicas medianas, ofrecemos una plataforma adaptable a tus necesidades.
        </p>
        <div className="cards">
          <div className="card">
            <h3>📅 Agenda de citas</h3>
            <p>Permite que tus clientes reserven el servicio que necesitan de forma rápida.</p>
          </div>
          <div className="card">
            <h3>👥 Gestión de clientes</h3>
            <p>Accede al historial y datos de tus pacientes en segundos.</p>
          </div>
          <div className="card">
            <h3>💳 Cobros y facturación</h3>
            <p>Administra pagos y facturas sin complicaciones.</p>
          </div>
          <div className="card">
            <h3>📊 Reportes claros</h3>
            <p>Visualiza el rendimiento de tu negocio con métricas fáciles de entender.</p>
          </div>
        </div>
      </section>

      {/* Testimonios */}
      <section className="testimonials" id="nosotros">
        <h2>Lo que dicen nuestros usuarios</h2>
        <div className="testimonial-cards">
          <div className="testimonial">
            <p>
              “Desde que usamos MedSys, organizar las citas en nuestro consultorio es mucho más fácil. 
              Nuestros pacientes están felices.”
            </p>
            <span>- Clínica Sonrisa</span>
          </div>
          <div className="testimonial">
            <p>
              “La gestión de cobros y reportes nos ahorra horas de trabajo administrativo cada semana.”
            </p>
            <span>- Centro de Bienestar Vital</span>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer" id="contacto">
        <p>© 2025 MedSys - Todos los derechos reservados</p>
        <p>Contacto: contacto@medsys.com | Tel: +57 300 000 0000</p>
      </footer>
    </div>
  );
}

export default LandingPage;

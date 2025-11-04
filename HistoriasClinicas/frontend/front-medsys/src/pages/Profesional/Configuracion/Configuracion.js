import React, { useState, useEffect } from "react";
import "./Configuracion.css";

function Configuracion() {
  const [profesional, setProfesional] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const session = JSON.parse(localStorage.getItem("profesional"));
    if (session?.idusuario) {
      fetch(`http://127.0.0.1:7000/profesional/consultar_profesional_usuario?idusuario=${session.idusuario}`)
        .then((res) => res.json())
        .then((data) => {
          if (data?.Nombre_Completo) {
            setProfesional(data);
          } else {
            setProfesional(null);
          }
          setLoading(false);
        })
        .catch((err) => {
          console.error("Error cargando profesional:", err);
          setLoading(false);
        });
    } else {
      setLoading(false);
    }
  }, []);

  if (loading) return <p>Cargando datos del profesional...</p>;
  if (!profesional) return <p>No se encontraron datos del profesional ❌</p>;

  return (
    <div className="config-container">
      <h2>👤 Perfil del Profesional</h2>
      <p>Aquí puedes ver tu información registrada en el sistema.</p>

      <div className="perfil-datos">
        <p><strong>Nombre completo:</strong> {profesional.Nombre_Completo}</p>
        <p><strong>Correo electrónico:</strong> {profesional.Correo}</p>
        <p><strong>Teléfono:</strong> {profesional.Telefono || "No registrado"}</p>
        <p><strong>Cargo:</strong> {profesional.Cargo}</p>
      </div>
    </div>
  );
}

export default Configuracion;

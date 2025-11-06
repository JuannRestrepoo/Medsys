// src/pages/Paciente/Perfil/PerfilPaciente.jsx
import React, { useEffect, useState } from "react";
import "./Perfil.css";


function PerfilPaciente() {
  const [perfil, setPerfil] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Leer sesión del paciente desde localStorage
    const raw = localStorage.getItem("paciente");
    const paciente = raw ? JSON.parse(raw) : null;

    if (!paciente || !paciente.idusuario) {
      setLoading(false);
      return;
    }

    // Llamada al backend para traer datos del paciente
    const fetchPerfil = async () => {
      try {
        const response = await fetch(
          `http://127.0.0.1:7000/paciente/consultar_paciente_usuario?idusuario=${paciente.idusuario}`
        );
        const data = await response.json();
        console.log("Perfil recibido desde backend:", data);
        setPerfil(data);
      } catch (error) {
        console.error("Error cargando perfil del paciente:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchPerfil();
  }, []);

  if (loading) return <p>Cargando perfil...</p>;
  if (!perfil) return <p>No se encontró información del paciente.</p>;

  return (
    <div className="perfil-paciente">
      <h2 className="perfil-titulo">Perfil del Paciente</h2>
      <div className="perfil-datos">
        <p><strong>Nombre:</strong> {perfil.Nombre_Completo}</p>
        <p><strong>Correo:</strong> {perfil.Correo}</p>
        <p><strong>Número de documento:</strong> {perfil.Numero_Documento}</p>
        <p><strong>Dirección:</strong> {perfil.Direccion}</p>
        <p><strong>Teléfono:</strong> {perfil.Telefono}</p>
        <p><strong>Edad:</strong> {perfil.Edad}</p>
      </div>
    </div>
  );
}

export default PerfilPaciente;

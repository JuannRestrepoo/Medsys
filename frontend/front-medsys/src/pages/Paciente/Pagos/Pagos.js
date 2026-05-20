import React, { useState, useEffect } from "react";
import "./Pagos.css";

function PagosPaciente() {
  const [facturas, setFacturas] = useState([]);

  useEffect(() => {
    const fetchFacturas = async () => {
      try {
        const paciente = JSON.parse(localStorage.getItem("paciente"));
        if (!paciente || !paciente.documento) {
          console.warn("⚠️ No hay documento del paciente en localStorage");
          return;
        }

        const res = await fetch(`http://127.0.0.1:7000/cobro/paciente/${paciente.documento}`);
        const data = await res.json();
        setFacturas(Array.isArray(data) ? data : []);
      } catch (err) {
        console.error("Error cargando facturas:", err);
        setFacturas([]);
      }
    };

    fetchFacturas();
  }, []);
  
  const handleVerFactura = (archivo) => {
    if (!archivo) {
      alert("⚠️ Esta factura aún no tiene archivo generado");
      return;
    }
    const url = `http://127.0.0.1:7000/uploads/facturas/${archivo}`;
    window.open(url, "_blank");
  };

  return (
    <div className="pagos-container">
      <h2>💳 Pagos</h2>
      <p>Consulta tus facturas médicas y el estado de tus pagos.</p>

      {/* Resumen */}
      <div className="pagos-summary">
        <div className="summary-card">
          <h3>{facturas.filter(f => !f.activo).length}</h3>
          <p>Facturas Pendientes</p>
        </div>
        <div className="summary-card">
          <h3>{facturas.filter(f => f.activo).length}</h3>
          <p>Facturas Pagadas</p>
        </div>
        <div className="summary-card">
          <h3>
            $
            {facturas
              .filter(f => !f.activo)
              .reduce((acc, f) => acc + Number(f.total), 0)
              .toLocaleString()}
          </h3>
          <p>Total Pendiente</p>
        </div>
      </div>

      {/* Tabla */}
      <div className="pagos-table-container">
        <table className="pagos-table">
          <thead>
            <tr>
              <th>Fecha</th>
              <th>Servicio</th>
              <th>Monto</th>
              <th>Estado</th>
              <th>Profesional</th>
              <th>Centro</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {facturas.map((f) => (
              <tr key={f.idcobro}>
                <td>{new Date(f.fecha).toLocaleDateString()}</td>
                <td>{f.productoservicio}</td>
                <td>${Number(f.total).toLocaleString()}</td>
                <td>
                  <span className={`status ${f.activo ? "pagado" : "pendiente"}`}>
                    {f.activo ? "Pagado" : "Pendiente"}
                  </span>
                </td>
                <td>{f.nombre_profesional}</td>
                <td>{f.nombre_centro}</td>
                <td>
                  {f.activo ? (
                    <button
                      className="btn-view"
                      onClick={() => handleVerFactura(f.archivofactura)}
                    >
                      Ver Recibo
                    </button>
                  ) : (
                    <button className="btn-pay">Pagar</button>
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>

      {/* Nota */}
      <div className="pagos-nota">
        <p>
          ℹ️ Puedes realizar tus pagos en línea o en el centro médico. Una vez
          confirmado, el estado cambiará a "Pagado".
        </p>
      </div>
    </div>
  );
}

export default PagosPaciente;

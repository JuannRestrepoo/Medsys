from fastapi import FastAPI

from application.Geografia.PaisRouter import router as pais_router
from application.Geografia.DepartamentoRouter import router as departamento_router
from application.Geografia.CiudadRouter import router as ciudad_router

from application.Organizacion.Centro.CentroRouter import router as centro_router

from application.Clinico.CitaMedicaRouter import router as citamedica_router
from application.Clinico.DiagnosticoRouter import router as diagnostico_router
from application.Clinico.HistoriaClinicaRouter import router as historiaclinica_router
from application.Clinico.RecetaMedicaRouter import router as recetamedica_router

from application.Usuario.Usuario.UsuarioRouter import router as usuario_router
from application.Usuario.Paciente.PacienteRouter import router as paciente_router
from application.Usuario.Profesional.ProfesionalRouter import router as profesional_router
from application.Usuario.TipoGenero.TipoGeneroRouter import router as tipogenero_router
from application.Usuario.TipoDocumento.TipoDocumentoRouter import router as tipodocumento_router

from application.Servicios.ProductoServicio.ProductoServicioRouter import router as productoservicio_router
from application.Servicios.TipoServicio.TipoServicioRouter import router as tiposervicio_router

from application.Transaccion.Cobro.CobroRouter import router as cobro_router
from application.Transaccion.EstadoPago.EstadoPagoRouter import router as estadopago_router
from application.Transaccion.DetalleCobro.DetalleCobroRouter import router as detallecobro_router
from application.auth.auth_router import router as auth_router

from application.Registrar.RegistrarPaciente import router as registrarpaciente_router

app: FastAPI = FastAPI (
    title="web API HistoriasClinicas",
    description="UDMPITW"
    
)

app.include_router(pais_router)
app.include_router(departamento_router)
app.include_router(ciudad_router)
app.include_router(centro_router)
app.include_router(citamedica_router)
app.include_router(diagnostico_router)
app.include_router(historiaclinica_router)
app.include_router(recetamedica_router)

app.include_router(usuario_router)
app.include_router(paciente_router)
app.include_router(profesional_router)
app.include_router(tipogenero_router)
app.include_router(tipodocumento_router)

app.include_router(productoservicio_router)
app.include_router(tiposervicio_router)
app.include_router(cobro_router)
app.include_router(estadopago_router)
app.include_router(detallecobro_router)
app.include_router(auth_router)
app.include_router(registrarpaciente_router)
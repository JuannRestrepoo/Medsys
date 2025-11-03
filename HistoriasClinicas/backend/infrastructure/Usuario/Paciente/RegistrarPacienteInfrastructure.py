# infrastructure/RegistrarPacienteInfrastructure.py
import psycopg2
import uuid
from  domain.Usuario.Paciente.RegistrarPacienteModel import RegistrarPacienteModel
from core.Security.security import hash_password

class RegistrarPacienteInfrastructure:

    @staticmethod
    def registrar_paciente(data: RegistrarPacienteModel):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                # 1. Buscar IdTipoGenero según el nombre
                cur.execute(
                    'SELECT "IdTipoGenero" FROM "TipoGenero" WHERE "Nombre" = %s',
                    (data.genero,)
                )
                row = cur.fetchone()
                if not row:
                    raise Exception(f"Género '{data.genero}' no existe en TipoGenero")
                idtipogenero = row[0]

                # 2. Generar hash de la contraseña usando el documento
                contrasena_hash = hash_password(data.documento)

                # 3. Insertar en Usuario (incluyendo ContrasenaHash)
                idusuario = str(uuid.uuid4())
                cur.execute(
                    '''
                    INSERT INTO "Usuario"(
                        "IdUsuario","Nombre_Completo","Numero_Documento",
                        "Correo","Telefono","Direccion",
                        "IdTipoGenero","IdCiudad","IdTipoDocumento","Contrasena_Hash","Rol","Fecha_Nacimiento","Activo"
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,B'1')
                    ''',
                    (
                        idusuario,
                        data.nombre,
                        data.documento,
                        data.correo,
                        data.telefono,
                        data.direccion,
                        idtipogenero,
                        data.idciudad,
                        data.idtipodocumento,
                        contrasena_hash,
                        "Paciente",
                        data.fecha_nacimiento
                           # 👈 aquí va el hash
                    )
                )

                # 4. Insertar en Paciente
                idpaciente = str(uuid.uuid4())
                cur.execute(
                    '''
                    INSERT INTO "Paciente"(
                        "IdPaciente","IdUsuario","Grupo_Sanguineo",
                        "Alergias","Antecedentes","Edad","Activo"
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,B'1')
                    ''',
                    (
                        idpaciente,
                        idusuario,
                        data.grupo_sanguineo,
                        data.alergias,
                        data.antecedentes,
                        data.edad
                    )
                )

                conn.commit()
                return {
                    "mensaje": "Paciente registrado correctamente",
                    "idusuario": idusuario,
                    "idpaciente": idpaciente
                }

        except Exception as e:
            if conn:
                conn.rollback()
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
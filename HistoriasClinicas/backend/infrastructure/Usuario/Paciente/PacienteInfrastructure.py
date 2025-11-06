import psycopg2
import psycopg2.extras
from domain.Usuario.Paciente.PacienteModel import PacienteModel

class PacienteInfrastructure:



# perfil paciente
    @staticmethod
    def consultar_paciente_usuario(idusuario: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    '''
                    SELECT u."Nombre_Completo",
                        u."Correo",
                        u."Numero_Documento",
                        u."Direccion",
                        u."Telefono",
                        p."Edad"
                    FROM "Usuario" u
                    JOIN "Paciente" p ON u."IdUsuario" = p."IdUsuario"
                    WHERE u."IdUsuario" = %s
                    ''',
                    (idusuario,)
                )
                result = cur.fetchone()
                return result if result else {"mensaje": "Paciente no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    @staticmethod
    def ingresar_paciente(paciente: PacienteModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarPaciente(%s,%s,%s,%s,%s);",
                            (paciente.idusuario, paciente.grupo_sanguineo,
                             paciente.alergias, paciente.antecedentes, paciente.edad))
                conn.commit()
                return {"mensaje": "Paciente ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_paciente(paciente: PacienteModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarPaciente(%s,%s,%s,%s,%s,%s,%s);",
                            (paciente.idpaciente, paciente.idusuario,
                             paciente.grupo_sanguineo, paciente.alergias,
                             paciente.antecedentes, paciente.edad,
                             '1' if paciente.activo else '0'))
                conn.commit()
                return {"mensaje": "Paciente modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Desactivar (borrado lógico)
    @staticmethod
    def desactivar_paciente(idpaciente: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarPaciente(%s);", (idpaciente,))
                conn.commit()
                return {"mensaje": f"Paciente {idpaciente} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Eliminar (borrado físico)
    @staticmethod
    def eliminar_paciente(idpaciente: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarPaciente(%s);", (idpaciente,))
                conn.commit()
                return {"mensaje": f"Paciente {idpaciente} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_paciente_por_id(idpaciente: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarPacientePorId(%s);", (idpaciente,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Paciente no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    @staticmethod
    def obtener_paciente_por_documento(documento: str):
        conn = None
        try:
            conn = psycopg2.connect(
                dbname="dbaMedSys",
                user="postgres",
                password="",
                host="127.0.0.1",
                port="5432"
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute(
                    '''
                    SELECT pa."IdPaciente",
                           u."IdUsuario",
                           u."Numero_Documento",
                           u."Nombre_Completo"
                    FROM "Paciente" pa
                    JOIN "Usuario" u ON pa."IdUsuario" = u."IdUsuario"
                    WHERE u."Numero_Documento" = %s
                    ''',
                    (documento,)
                )
                result = cur.fetchone()
                if result:
                    return result
                return {"error": "Paciente no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
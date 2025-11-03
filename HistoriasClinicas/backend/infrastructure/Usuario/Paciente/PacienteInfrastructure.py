import psycopg2
import psycopg2.extras
from domain.Usuario.Paciente.PacienteModel import PacienteModel

class PacienteInfrastructure:

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

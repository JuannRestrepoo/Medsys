import psycopg2
import psycopg2.extras
from domain.Geografia.Departamento.DepartamentoModel import DepartamentoModel
from domain.Geografia.Pais.PaisModel import PaisModel

class DepartamentoInfrastructure:

    # 🔹 Insertar
    @staticmethod
    def ingresar_departamento(departamento: DepartamentoModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarDepartamento(%s, %s);",
                            (departamento.nombre, departamento.idpais))
                conn.commit()
                return {"mensaje": "Departamento ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Modificar
    @staticmethod
    def modificar_departamento(departamento: DepartamentoModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarDepartamento(%s, %s, %s);",
                            (departamento.iddepartamento, departamento.nombre, departamento.idpais))
                conn.commit()
                return {"mensaje": "Departamento modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_departamento(iddepartamento: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarDepartamento(%s);", (iddepartamento,))
                conn.commit()
                return {"mensaje": f"Departamento {iddepartamento} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()


    # 🔹 Eliminar
    @staticmethod
    def eliminar_departamento(iddepartamento: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarDepartamento(%s);", (iddepartamento,))
                conn.commit()
                return {"mensaje": f"Departamento {iddepartamento} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar todos
    @staticmethod
    def consultar_departamento():
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDepartamento();")
                result = cur.fetchall()
            return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    # 🔹 Consultar por Id
    @staticmethod
    def consultar_departamento_por_id(iddepartamento: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarDepartamentoPorId(%s);", (iddepartamento,))
                result = cur.fetchone()
            if result:
                return result
            else:
                return {"mensaje": f"No se encontró un departamento con Id {iddepartamento}"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

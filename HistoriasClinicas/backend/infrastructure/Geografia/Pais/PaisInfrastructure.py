import psycopg2
import psycopg2.extras
from domain.Geografia.Pais.PaisModel import PaisModel

class PaisInfrastructure:

    # 🔹 Consultar todos los países
    @staticmethod
    def consultar_pais():
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarPais();")
                result = cur.fetchall()
            return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
    # 🔹 Consultar país por ID (UUID)
    @staticmethod
    def consultar_pais_por_id(idpais: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarPaisPorId(%s);", (idpais,))
                result = cur.fetchone()
            if result:
                return result
            else:
                return {"mensaje": f"No se encontró un país con Id {idpais}"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    # 🔹 Listar países activos
    @staticmethod
    def listar_paises_activos():
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
                cur.execute("""
                    SELECT "IdPais", "Nombre", "Activo"
                    FROM "Pais"
                    WHERE "Activo" = B'1';
                """)
                rows = cur.fetchall()
                # Convertimos a lista de diccionarios
                result = [
                    {"id": row[0], "nombre": row[1], "activo": bool(int(row[2]))}
                    for row in rows
                ]
                return result
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    # 🔹 Ingresar país
    @staticmethod
    def ingresar_pais(paismodel: PaisModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarPais(%s);", (paismodel.nombre,))
                conn.commit()
                return {"mensaje": "País ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()
                
    # 🔹 Modificar país
    @staticmethod
    def modificar_pais(paismodel: PaisModel):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarPais(%s, %s);", 
                            (paismodel.idpais, paismodel.nombre))
                conn.commit()
                return {"mensaje": "País modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    # 🔹 Eliminar país
    @staticmethod
    def eliminar_pais(idpais: str):
        try:
            conn = psycopg2.connect(
                dbname='dbaMedSys',
                user='postgres',
                password='',
                host='127.0.0.1',
                port='5432'
            )
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarPais(%s);", (idpais,))
                conn.commit()
                return {"mensaje": f"País con Id {idpais} eliminado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

    # 🔹 Desactivar país (borrado lógico)
    @staticmethod
    def desactivar_pais(idpais: str):
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
                # Llamamos la función de borrado lógico
                cur.execute("SELECT spaDesactivarPais(%s);", (idpais,))
                conn.commit()
                return {"mensaje": f"País con Id {idpais} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn:
                conn.close()

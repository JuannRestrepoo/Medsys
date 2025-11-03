import psycopg2
import psycopg2.extras
from domain.Servicios.ProductoServicio.ProductoServicioModel import ProductoServicioModel

class ProductoServicioInfrastructure:

    @staticmethod
    def ingresar_productoservicio(ps: ProductoServicioModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaIngresarProductoServicio(%s,%s,%s,%s);",
                            (ps.nombre, ps.descripcion, ps.precio, ps.idtiposervicio))
                conn.commit()
                return {"mensaje": "Producto/Servicio ingresado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def modificar_productoservicio(ps: ProductoServicioModel):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaModificarProductoServicio(%s,%s,%s,%s,%s,%s);",
                            (ps.idproductoservicio, ps.nombre, ps.descripcion,
                             ps.precio, ps.idtiposervicio,
                             '1' if ps.activo else '0'))
                conn.commit()
                return {"mensaje": "Producto/Servicio modificado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def desactivar_productoservicio(idproductoservicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaDesactivarProductoServicio(%s);", (idproductoservicio,))
                conn.commit()
                return {"mensaje": f"Producto/Servicio {idproductoservicio} desactivado correctamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def eliminar_productoservicio(idproductoservicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor() as cur:
                cur.execute("SELECT spaEliminarProductoServicio(%s);", (idproductoservicio,))
                conn.commit()
                return {"mensaje": f"Producto/Servicio {idproductoservicio} eliminado físicamente"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

    @staticmethod
    def consultar_productoservicio_por_id(idproductoservicio: str):
        try:
            conn = psycopg2.connect(dbname='dbaMedSys', user='postgres',
                                    password='', host='127.0.0.1', port='5432')
            with conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor) as cur:
                cur.execute("SELECT * FROM spaConsultarProductoServicioPorId(%s);", (idproductoservicio,))
                result = cur.fetchone()
                return result if result else {"mensaje": "Producto/Servicio no encontrado"}
        except Exception as e:
            return {"error": str(e)}
        finally:
            if conn: conn.close()

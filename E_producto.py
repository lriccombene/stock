import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()

class E_producto(base):
      __tablename__="producto"
      id_producto = Column(Integer, primary_key=True, autoincrement=True)
      nombre = Column(String)
      codigo_interno = Column(String)
      codigo_producto = Column(String)
      fecha =  Column(DateTime)
      descripcion =  Column(String)
      lote  =  Column(DateTime)
      marca = Column(String)
      categoria = Column(String)
      detalle = Column(String)
      unidad = Column(String)

      def __init__(self):
          obj_conexion = configuracion()
          engine = create_engine(obj_conexion.config())
          Session = sessionmaker(bind=engine)
          self.session = Session()

      @classmethod
      def guardar(cls, obj_producto):
          obj_E_producto = cls()
          try:

              obj_E_producto.nombre = obj_producto.nombre
              obj_E_producto.codigo_interno = obj_producto.codigo_interno
              obj_E_producto.codigo_producto = obj_producto.codigo_producto
              obj_E_producto.fecha = obj_producto.fecha
              obj_E_producto.descripcion = obj_producto.descripcion
              obj_E_producto.lote = obj_producto.lote
              obj_E_producto.marca = obj_producto.marca
              obj_E_producto.categoria = obj_producto.categoria
              obj_E_producto.unidad = obj_producto.unidad
              obj_E_producto.detalle  = obj_producto.detalle
              obj_E_producto.session.add(obj_E_producto)

              obj_E_producto.session.commit()
              obj_cliente_result = obj_E_producto.session.query(E_producto).filter_by(
                  codigo_interno=str(obj_producto.codigo_interno)).first()
              obj_E_producto.session.close()
              return obj_cliente_result.id_producto

          except IntegrityError:
              obj_E_producto.session.rollback()
              obj_E_producto.session.close()
              return False

      def get_producto_nombre(self, nombre):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_producto = self.session.query(E_producto).filter_by(nombre=str(nombre)).first()
          self.session.close()
          try:
              a = obj_producto.id_producto
              return obj_producto
          except:
              return False


      def get_producto_codigo_interno(self, cod_int):
          obj_producto = self.session.query(E_producto).filter_by(codigo_interno=str(cod_int)).first()
          self.session.close()
          try:
              a = obj_producto.id_cliente
              return obj_producto
          except:
              return False

      def get_lista_productos(self):
          lista_productos = self.session.query(E_producto).all()
          self.session.close()
          return lista_productos

      def get_producto_nombre_like(self, nombre):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          sql = text("select  id_producto, nombre, codigo_interno, codigo_producto, fecha, descripcion, lote, marca, categoria, detalle , unidad from producto WHERE nombre LIKE '"+nombre + "%'" )
          result = self.session.execute(sql)
          try:
              self.session.close()
              return result
          except:
              self.session.close()
              return False

          self.session.close()
          return lista_E_cuenta

      def get_producto_codigo_like(self,codigo):
          # pyqtRemoveInputHook()
          # import pdb; pdb.set_trace()
          sql = text(
              "select  id_producto, nombre, codigo_interno, codigo_producto, fecha, descripcion, lote, marca, categoria, detalle , unidad from producto WHERE codigo_producto LIKE '" + codigo + "%'")
          result = self.session.execute(sql)
          try:
              self.session.close()
              return result
          except:
              self.session.close()
              return False

      def get_producto_id(self,id):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_producto = self.session.query(E_producto).filter_by(id_producto=id).first()
          self.session.close()
          try:
              a = obj_producto.id_producto
              return obj_producto
          except:
              return False

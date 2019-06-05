from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()

class E_movimiento(base):
      __tablename__="movimientos"
      id_movimiento = Column(Integer, primary_key=True, autoincrement=True)
      id_producto = Column(Integer)
      cantidad = Column(Numeric)
      fecha =Column(DateTime)
      tipo=Column(String)
      responsable = Column(String)


      def __init__(self):
          obj_conexion = configuracion()
          engine = create_engine(obj_conexion.config())
          Session = sessionmaker(bind=engine)
          self.session = Session()

      @classmethod
      def guardar(cls, obj_movimiento):
          obj_E_movimiento = cls()
          try:
              #pyqtRemoveInputHook()
              #import pdb; pdb.set_trace()
              obj_E_movimiento.id_producto = obj_movimiento.id_producto
              obj_E_movimiento.cantidad = obj_movimiento.cantidad.replace(",", ".")
              obj_E_movimiento.fecha = obj_movimiento.fecha
              obj_E_movimiento.tipo = obj_movimiento.tipo
              obj_E_movimiento.responsable = obj_movimiento.responsable

              obj_E_movimiento.session.add(obj_E_movimiento)
              obj_E_movimiento.session.commit()
              return True

          except :
              obj_E_movimiento.session.rollback()
              obj_E_movimiento.session.close()
              return False


      def actualizar(self,obj_movimiento):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            u = update(E_movimiento).where(E_movimiento.id_inventario == obj_movimiento.id_movimiento).values(cantidad=obj_movimiento.cantidad)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def get_movimientos(self):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_movimiento = self.session.query(E_movimiento).all()
          self.session.close()
          try:
              return obj_movimiento
          except:
              return False
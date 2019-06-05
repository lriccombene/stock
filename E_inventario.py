from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func,Boolean, Numeric, update,Float,text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from PyQt5.QtCore import pyqtRemoveInputHook
from E_configuracion import configuracion

base = declarative_base()

class E_inventario(base):
      __tablename__="inventario"
      id_inventario = Column(Integer, primary_key=True, autoincrement=True)
      id_producto = Column(Integer)
      cantidad = Column(Numeric)


      def __init__(self):
          obj_conexion = configuracion()
          engine = create_engine(obj_conexion.config())
          Session = sessionmaker(bind=engine)
          self.session = Session()

      @classmethod
      def guardar(cls, obj_inventario):
          obj_E_inventario = cls()
          try:

              #pyqtRemoveInputHook()
              #import pdb; pdb.set_trace()

              obj_E_inventario.id_producto = obj_inventario.id_producto
              obj_E_inventario.cantidad = obj_inventario.cantidad.replace(",", ".")
              obj_E_inventario.session.add(obj_E_inventario)
              obj_E_inventario.session.commit()
              return True

          except :
              obj_E_inventario.session.rollback()
              obj_E_inventario.session.close()
              return False


      def actualizar(self,obj_inventario):
            #pyqtRemoveInputHook()
            #import pdb; pdb.set_trace()
            u = update(E_inventario).where(E_inventario.id_inventario == obj_inventario.id_inventario).values(cantidad=obj_inventario.cantidad)
            self.session.execute(u)
            self.session.commit()
            self.session.close()

      def get_inventario_id_producto(self, id_producto):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_inventario = self.session.query(E_inventario).filter_by(id_producto=str(id_producto)).first()
          self.session.close()
          try:
              a = obj_inventario.id_producto
              return obj_inventario
          except:
              return False

      def get_inventario(self):
          #pyqtRemoveInputHook()
          #import pdb; pdb.set_trace()
          obj_inventario = self.session.query(E_inventario).all()
          self.session.close()
          try:
              return obj_inventario
          except:
              return False


      def get_inventario_tipo_prod(self,tipo_producto):
          # pyqtRemoveInputHook()
          # import pdb; pdb.set_trace()
          sql = text("select i.cantidad, p.nombre from inventario i inner join producto p on i.id_producto = p.id_producto where p.categoria='"+ tipo_producto+"'")
          result = self.session.execute(sql)
          try:
              self.session.close()
              return result
          except:
              self.session.close()
              return False

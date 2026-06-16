from .database import Base
from sqlalchemy import Column, Integer, String

class Contato(Base):
    __tablename__ = "contato"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(150), nullable=False)
    mensagem = Column(String(1500), nullable=False)


from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()


class Usuario(Base):
    # Definindo características da tabela no banco de dados.
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150),unique=True)
    senha = Column(String(150))

    # Definindo características da classe.
    def __init__(self,nome:str,email:str,senha:str):
        self.nome=nome
        self.email=email        
        self.senha=senha

        if not nome:
            raise ValueError("nome vazio.")
        if not isinstance(nome, str):
            raise TypeError("nome invalido.")
            
        if not email:
            raise ValueError("email vazio.")
        if not isinstance(email, str):
            raise TypeError("email invalido.")
            
            
        if not senha:
            raise ValueError("senha vazia.")
        if not isinstance(senha, str):
            raise TypeError("senha invalida.")  


# Criando tabela no banco de dados.
Base.metadata.create_all(bind=db)

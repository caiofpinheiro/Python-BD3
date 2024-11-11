from app.models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository


class UsuarioService:

    def __init__(self, respository: UsuarioRepository):
        self.repository = respository

    def criar_usuario(self, nome: str, email: str, senha: str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            cadastrado = self.repository.pesquisar_usuario_por_email(usuario.email)

            if cadastrado:
                print("Usuário já cadastrado!")
                return

            self.repository.salvar_usuario(usuario)
            print("Usuário cadastrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro:
            print(f"Houve um erro inesperado: {erro}")
 

    def listar_todos_usuario(self):
        return self.repository.listar_usuarios()

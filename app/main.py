import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.services.usuario_service import UsuarioService
from app.repositories.usuario_repository import UsuarioRepository
from app.config.database import Session





def main():

    
    session=Session()
    repository=UsuarioRepository(session)
    service=UsuarioService(repository)


    while True:
        print("=======SENAI SOLUTION========")
        print("1.Adicionar Usuário")
        print("2.Pesquisar Usuário")
        print("3.Atualizar Usuário")
        print("4.Excluir Usuário")
        print("5.Exibir todos os  Usuários")
        print("0.Sair")
        opcao=input("Selecione a opção que deseja: ")

       
        match opcao:
            case "1":
                print("\nAdicionando Usuario")
                nome=input("Digite seu nome: ")
                email=input("Digite seu email: ")
                senha=input("Digite sua senha: ")
                service.criar_usuario(nome=nome,email=email,senha=senha)
                

            case "2":
                try:
                    usuario_email = input("Digite o email do usuário que você deseja encontrar: ")

                    usuario = service.repository.pesquisar_usuario_por_email(usuario_email)

                    if usuario:
                        print(f"Usuário encontrado: ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")
                    else:
                        print("Usuário inexistente.")

                except ValueError:
                    print("Por favor, coloque um email válido.")
                except Exception as e:
                    print(f"Houve um erro ao procurar o usuário: {e}")
                break

            case "3":
                print("Atualizando usuario")
                try:
                    usuario_id = int(input("Digite o email do usuário a ser atualizado: "))

                    usuario = repository.buscar_id(usuario_id)

                    
                    if usuario:
                        print(f"Usuário encontrado:| Nome: {usuario.nome} | Email: {usuario.email}")

                        novoNome = input(f"Digite o novo nome (atual: {usuario.nome}): ")
                        novoEmail = input(f"Digite o novo email (atual: {usuario.email}): ")
                        novaSenha = input("Digite a nova senha: ")

                        service.atualizar_usuario(novoNome, novoEmail, novaSenha)
                        print("Usuário atualizado com sucesso!")
                    else:
                        print("Usuário não encontrado.")

                except ValueError:
                    print("Por favor, cloque um email válido.")
                except Exception as e:
                    print(f"Houve um erro ao atualizar o usuário: {e}")
                break
              
                break

            case "4":
                print("Excluindo usuário")
                try:
                    usuario_id = int(input("Digite o email do usuário a ser excluído: "))
                    usuario=service.repository.excluir_usuario(usuario)
                    print("Usuario excluido com sucesso")
                except ValueError:
                    print("Por favor, coloque um email válido.")
                   
                    
                
            case "5":

                print("Exibir todos os usuarios")

                service.listar_todos_usuario()

                print("\nExibindo todos os usuários cadastrados:")

                usuarios = service.listar_todos_usuario()

                if usuarios:
                    for usuario in usuarios:
                        print(f"Nome: {usuario.nome} | Email: {usuario.email}")
                
                else:
                    print("Nenhum usuário cadastrado.")
                    break
               
            case "0":
                break
            
 

if __name__ == "__main__":
    os.system("cls||clear")
    main()
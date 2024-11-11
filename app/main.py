from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os


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
        # Solicita o email do usuário
                    usuario_email = input("Digite o email do usuário que você deseja encontrar: ")

        # Chama o método de pesquisa no serviço
                    usuario = service.repository.pesquisar_usuario__por__email(usuario_email)

        # Exibe as informações do usuário encontrado
                    if usuario:
                        print(f"Usuário encontrado: ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")
                    else:
                        print("Usuário não encontrado.")

                except ValueError:
                    print("Por favor, insira um email válido.")
                except Exception as e:
                    print(f"Ocorreu um erro ao procurar o usuário: {e}")
                break

            case "3":
                print("Atualizando usuario")
                try:
                    # Solicita o ID do usuário a ser atualizado
                    usuario_id = int(input("Digite o ID do usuário a ser atualizado: "))

                    # Pesquisa o usuário pelo ID para garantir que ele exista
                    usuario = repository.buscar_por_id(usuario_id)

                    
                    if usuario:
                        print(f"Usuário encontrado: ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")

                        # Solicita os novos dados
                        novo_nome = input(f"Digite o novo nome (atual: {usuario.nome}): ")
                        novo_email = input(f"Digite o novo email (atual: {usuario.email}): ")
                        nova_senha = input("Digite a nova senha: ")

                        # Chama o serviço para atualizar o usuário
                        service.atualizar_usuario(usuario_id, novo_nome, novo_email, nova_senha)
                        print("Usuário atualizado com sucesso!")
                    else:
                        print("Usuário não encontrado.")

                except ValueError:
                    print("Por favor, insira um ID válido.")
                except Exception as e:
                    print(f"Ocorreu um erro ao atualizar o usuário: {e}")
                break
              
                break

            case "4":
                print("Excluindo usuário")
                try:
                    usuario_id = int(input("Digite o ID do usuário a ser excluído: "))
                    usuario=service.repository.excluir_usuario(usuario_id)
                    print("Usuario excluido com sucesso")
                except ValueError:
                    print("Por favor, insira um ID válido.")
                   
                    
                
            case "5":

                print("Exibir todos os usuarios")

                service.listar_todos_usuarios()

                print("\nExibindo todos os usuários cadastrados:")

                usuarios = service.listar_todos_usuarios()

                if usuarios:
                    for usuario in usuarios:
                        print(f"ID: {usuario.id} | Nome: {usuario.nome} | Email: {usuario.email}")
                
                else:
                    print("Nenhum usuário cadastrado.")
                    break
               
            case "0":
                break
            
 
    

    #Listar todos os usuários cadastrados
        #print("\nListando todos os usuarios cadastrados.")
        #lista_usuarios=service.listar_todos_usuarios()

        #for usuario in lista_usuarios:
            #print(f"{usuario.nome} - {usuario.email} - {usuario.senha}")

if __name__ == "__main__":
    os.system("cls||clear")
    main()
from datetime import datetime, date, timedelta
from src.plantacoes import cadastrar, editar, visualizar, relatorios, apagar
import src.utils as utils
import src.usuario as usuario

def iniciar_sistema():
    usuarios = usuario.carregar_usuarios()
    usuario.cadastrodeusuario(usuarios)

    plantacoes = utils.carregar_dados()
    menu(plantacoes, usuarios)


def menu(plantacoes, usuarios):

    while True:

        utils.limpar_tela()

        opcoes = [
            "Cadastrar Plantação",
            "Editar Plantação",
            "Visualizar Plantações Cadastradas",
            "Relatórios de Plantações",
            "Apagar Plantação",
            "Trocar Nome de Usuário",
            "Sair"
        ]

        utils.titulo("🌱 SISTEMA DE MANUSEIO DE PLANTAÇÕES 🌱")
        print(f"Bem Vindo(a) {usuarios[0]['nome']}, o que quer fazer hoje?\n")

        for i, opcao in enumerate(opcoes):
            print(f"{i}. {opcao}")

        try:
            escolha = int(input("\nSelecione a opção desejada do menu: "))

            if escolha == 0:
                cadastrar(plantacoes)

            elif escolha == 1:
                editar(plantacoes)

            elif escolha == 2:
                visualizar(plantacoes)

            elif escolha == 3:
                relatorios(plantacoes)
            
            elif escolha == 4:
                apagar(plantacoes)

            elif escolha == 5:
                usuario.apagarusuario(usuarios)
                usuario.cadastrodeusuario(usuarios)

            elif escolha == 6:
                utils.barrinha()
                print(f"{'Programa Encerrado!':^50}")
                utils.barrinha()
                break

            else:
                print("❌ ERRO: Opção inválida!")
                utils.pausa_pressione()

        except ValueError:
            print("❌ ERRO: Digite apenas números ou uma entrada válida!")
            utils.pausa_pressione()

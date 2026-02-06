from src.plantacoes import chamadadefuncoes
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

            if escolha == len(opcoes):
                utils.subtitulo(f"{'Programa Encerrado!':^{utils.largura_tela}}")
                break

            else:
                chamadadefuncoes(escolha, plantacoes, usuarios)

        except ValueError:
            print("❌ ERRO: Digite apenas números ou uma entrada válida!")
            utils.pausa_pressione()
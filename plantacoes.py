from datetime import datetime
import utils
import usuario

plantacoes = []

def menu(plantacoes, usuarios):

    while True:
        
        utils.limpar_tela()

        opcoes = [
            "Cadastrar Plantação",
            "Editar Plantação",
            "Visualizar Plantações Cadastradas",
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

            if escolha == 5:
                utils.barrinha()
                print(f"{'Programa Encerrado!':^50}")
                utils.barrinha()
                break

            elif escolha == 0:
                cadastrar(plantacoes)

            elif escolha == 1:
                editar(plantacoes)

            elif escolha == 2:
                visualizar(plantacoes)
            
            elif escolha == 3:
                apagar(plantacoes)

            elif escolha == 4:
                usuario.apagarusuario(usuarios)
                usuario.cadastrodeusuario(usuarios)

            else:
                print("❌ ERRO: Opção inválida!")
                utils.pausa_pressione()

        except ValueError:
            print("❌ ERRO: Digite apenas números!")
            utils.pausa_pressione()


def cadastrar(lista):

    utils.limpar_tela()

    nome = input("Digite o nome da plantação: ")
    semente = input("Digite a semente utilizada: ")

    data_plantio = utils.converter_data(input("Digite a data de plantio (dd/mm/aaaa): "))

    if not utils.validar_data(data_plantio):
        print("ERRO: Data inválida!")
        utils.pausa_pressione()
        return

    data_colheita = utils.converter_data(input("Digite a data de colheita (dd/mm/aaaa): "))

    if not utils.validar_data(data_colheita):
        print("ERRO: Data inválida!")
        utils.pausa_pressione()
        return

    plantacao = {"nome": nome, "semente": semente, "plantio": data_plantio, "colheita": data_colheita}

    lista.append(plantacao)
    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON

    utils.barrinha()
    print("Plantação cadastrada com sucesso! ✅")
    utils.barrinha()

    utils.pausa_tempo()


def visualizar(lista):

    utils.limpar_tela()

    if not lista:
        print("⚠️  Nenhuma plantação cadastrada.")
        utils.pausa_pressione()
        return

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    try:
        escolha = int(input("\nEscolha uma plantação para analisar: "))
        if 0 <= escolha < len(lista):
            analisar(lista, escolha)
        else:
            print("❌ ERRO: Opção inválida!")
            utils.pausa_pressione()
    except ValueError:
        print("❌ ERRO: Digite apenas números!")
        utils.pausa_pressione()


def analisar(lista, indice):

    utils.limpar_tela()

    plantacao = lista[indice]

    utils.titulo(f"Plantação: {plantacao['nome']}")
    print(f"Semente: {plantacao['semente']}")
    print(f"Data de plantio: {plantacao['plantio']}")
    print(f"Data de colheita: {plantacao['colheita']}")

    dias = (datetime.strptime(plantacao['colheita'], "%d/%m/%Y") - datetime.strptime(plantacao['plantio'], "%d/%m/%Y"))

    print(f"Faltam {dias.days} dias para a colheita!")

    utils.pausa_pressione()


def editar(lista):

    utils.limpar_tela()

    utils.barrinha()

    if not lista:
        print("⚠️  Nenhuma plantação cadastrada.")
        utils.pausa_pressione()
        return

    # Mostra as plantações
    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    try:
        escolha = int(input("\nEscolha a plantação para editar: "))
        if not (0 <= escolha < len(lista)):
            print("❌ ERRO: Opção inválida!")
            utils.pausa_pressione()
            return
    except ValueError:
        print("❌ ERRO: Digite apenas números!")
        utils.pausa_pressione()
        return

    utils.limpar_tela()

    plantacao = lista[escolha]

    utils.titulo(f"Editando: {plantacao['nome']}")

    # Campos que o usuário vê
    campos = ["Nome", "Semente", "Data de Plantio", "Data de Colheita"]

    # Campos reais do dicionário
    mapa_campos = ["nome", "semente", "plantio", "colheita"]

    for i, campo in enumerate(campos):
        print(f"{i}. {campo}")

    try:
        campo_escolhido = int(input("\nQual campo deseja editar? "))
        if campo_escolhido not in range(4):
            print("❌ ERRO: Opção inválida!")
            utils.pausa_pressione()
            return
    except ValueError:
        print("❌ ERRO: Digite apenas números!")
        utils.pausa_pressione()
        return

    novo_valor = input(f"Digite o novo valor para {campos[campo_escolhido]}: ")

    # Se for data, valida
    if campo_escolhido in [2, 3]:
        novo_valor = utils.converter_data(novo_valor)
        if not utils.validar_data(novo_valor):
            print("❌ ERRO: Data inválida!")
            utils.pausa_pressione()
            return

    # Final
    chave = mapa_campos[campo_escolhido]
    plantacao[chave] = novo_valor

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON

    utils.barrinha()
    print("Plantação atualizada com sucesso! ✅")
    utils.barrinha()

    utils.pausa_tempo()

def apagar(lista):

    utils.limpar_tela()

    utils.barrinha()

    if not lista:
        print("⚠️ Nenhuma plantação cadastrada.")
        utils.pausa_pressione()
        return

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    try:
        escolha = int(input("\nEscolha uma plantação para apagar: "))
        if 0 <= escolha < len(lista):
            confirmar = input(f"Tem certeza que deseja apagar {lista[escolha]['nome']}? (s/n) ").lower()
            if confirmar != 's':
                return
            lista.pop(escolha)
            utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
            utils.barrinha()
            print("Plantação deletada com sucesso! ✅")
            utils.barrinha()
            utils.pausa_tempo()
        else:
            print("❌ ERRO: Opção inválida!")
            utils.pausa_pressione()
    except ValueError:
        print("❌ ERRO: Digite apenas números!")
        utils.pausa_pressione()

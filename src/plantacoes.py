from datetime import datetime, timedelta
import src.utils as utils
import src.usuario as usuario


def chamadadefuncoes(escolha, plantacoes, usuarios):

        if escolha in range(5):
            opcoesdefuncoes = [cadastrar, editar, visualizar, relatorios, apagar]
            opcoesdefuncoes[escolha](plantacoes)

        elif escolha == 5:
            usuario.apagarusuario(usuarios)
            usuario.cadastrodeusuario(usuarios)

        else:
            print("❌ ERRO: Opção inválida!")
            utils.pausa_pressione()


def mostrar_sementes(sementes, coluna=3):
    """
    Este bloco é uma função de suporte que explica a lógica usada para imprimir sementes
    em colunas de 3 (editável) para que o usuário escolha corretamente.
    """

    print("\nEscolha uma das seguintes sementes: \n")

    printar = ""

    for i in range(len(sementes)):
        item = f"{i}. {sementes[i]}"
        printar += f"{item:^25} | "
        if (i + 1) % coluna == 0:
            print(printar.rstrip(" | "))
            printar = ""

    if printar:
        print(printar.rstrip(" | "))


def cadastrar(lista):

    utils.limpar_tela()
    utils.subtitulo("Cadastro de Plantações")

    nome = input("Digite o nome da plantação: ")

    sementes = utils.carregar_dados(utils.SEMENTES)

    mostrar_sementes(sementes)

    semente = int(input("\nDigite a semente utilizada: "))

    data_plantio = utils.converter_data(input("Digite a data de plantio (dd/mm/aaaa): "))

    if not utils.validar_data(data_plantio):
        print("❌ ERRO: Data inválida!")
        utils.pausa_pressione()
        return

    data_colheita = utils.converter_data(input("Digite a data de colheita (dd/mm/aaaa): "))

    if not utils.validar_data(data_colheita):
        print("❌ ERRO: Data inválida!")
        utils.pausa_pressione()
        return

    plantacao = {"nome": nome, "semente": sementes[semente], "plantio": data_plantio, "colheita": data_colheita}

    lista.append(plantacao)
    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON

    utils.barrinha()
    print("Plantação cadastrada com sucesso! ✅")
    utils.barrinha()

    utils.pausa_tempo()


def editar(lista):

    utils.limpar_tela()
    utils.subtitulo("Edição de Plantação")

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

    if campo_escolhido == 1:

        sementes = utils.carregar_dados(utils.SEMENTES)

        mostrar_sementes(sementes)

        novo_valor = int(input(f"\nDigite o novo valor para {campos[campo_escolhido]}: "))

    else:
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


def visualizar(lista):

    utils.limpar_tela()
    utils.subtitulo("Visualização de Plantações")

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


def relatorios(lista):

    utils.limpar_tela()
    utils.subtitulo("Relatórios de Plantações")

    opcoes = ["Resumo de Colheita Mensal", "Status de Colheita", "Análise de Colheitas"]

    for i, opcao in enumerate(opcoes):
        print(f"{i}. {opcao}")

    escolha = int(input("\nDigite uma das opções acima: "))

    if escolha not in range(len(opcoes)):
        print("\n❌ ERRO: Selecione uma das opções exibidas")
        utils.pausa_pressione()
        return

    relatorios_2(lista, escolha, opcoes)


def relatorios_2(lista, escolha, opcoes):

    utils.limpar_tela()
    utils.subtitulo(f"{opcoes[escolha]}")

    #Resumo de Colheita Mensal
    if escolha == 0:

        print(f"Total de platações cadastradas: {len(lista)}")
        print(f"Colheitas para o mês de {utils.mesatual()}: ")
        utils.barrinha()
        
        for plantacao in lista:
            plantacao_analisada = datetime.strptime(plantacao["colheita"], "%d/%m/%Y")
            if plantacao_analisada.month == utils.mesatual(False):
                print(f"\n- {plantacao["nome"]}")
                print(f"Semente: {plantacao["semente"]}")
                print(f"Colheita: {plantacao["colheita"]}")
                print("")

    # Status de Colheita
    elif escolha == 1:

        hoje = datetime.today()

        concluidas = []
        emandamento = []
        agendadas = []

        for plantacao in lista:
            datadecolheita = datetime.strptime(plantacao["colheita"], "%d/%m/%Y")
            datadeplantio = datetime.strptime(plantacao["plantio"], "%d/%m/%Y")
            if hoje >= datadecolheita:
                concluidas.append(plantacao)
            elif datadeplantio < hoje < datadecolheita:
                emandamento.append(plantacao)
            else:
                agendadas.append(plantacao)
        
        print("")
        
        print(f"🟢 Concluídas ({len(concluidas)})")
        for plantacao in concluidas:
            print(f"- {plantacao["nome"]} | Colheita: {plantacao["colheita"]}")

        print(f"\n🟡 Em andamento ({len(emandamento)})")
        for plantacao in emandamento:
            print(f"- {plantacao["nome"]} | Colheita: {plantacao["colheita"]}")

        print(f"\n🔵 Agendadas ({len(agendadas)})")
        for plantacao in agendadas:
            print(f"- {plantacao["nome"]} | Colheita: {plantacao["colheita"]}")

    # Análise de Colheita
    elif escolha == 2:

        print(f"{'| PROXIMAS COLHEITAS (PRÓXIMOS 7 DIAS) |':^{utils.largura_tela}}")

        hoje = datetime.today()

        cont = 0
        for plantacao in lista:
            datadecolheita = datetime.strptime(plantacao["colheita"], "%d/%m/%Y")
            diasatecolheita = (datadecolheita - hoje).days
            if 0 <= diasatecolheita <= 7:
                print(f"- {plantacao["nome"]} | {plantacao["semente"]} -> {diasatecolheita} dias")
                cont += 1
        
        if cont == 0: print(f"\n{'NÃO Há COLHEITAS NOS PRÓXIMOS 7 DIAS':^{utils.largura_tela}}")

    utils.pausa_pressione()


def apagar(lista):

    utils.limpar_tela()
    utils.subtitulo("Apagar Plantação")

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
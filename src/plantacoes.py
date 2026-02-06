from datetime import datetime
import src.utils as utils
import src.usuario as usuario
import src.auxiliares as auxiliares

# Chama as Funções
def chamadadefuncoes(escolha, plantacoes, usuarios):

    opcoesdefuncoes = [cadastrar, editar, visualizar, relatorios, apagar]

    if escolha in range(len(opcoesdefuncoes)):
        opcoesdefuncoes[escolha](plantacoes)

    elif escolha == 5:
        usuario.apagarusuario(usuarios)
        usuario.cadastrodeusuario(usuarios)

    else:
        print("❌ ERRO: Opção inválida!")
        utils.pausa_pressione()


# Funções do Sistema
def cadastrar(lista):

    utils.limpar_tela()
    utils.subtitulo("Cadastro de Plantações")

    nome = input("Digite o nome da plantação: ")

    semente, sementes = auxiliares.mostrar_sementes()
    if semente is None: return

    data_plantio = utils.converter_data(input("Digite a data de plantio (dd/mm/aaaa): "))
    if not utils.validar_data(data_plantio): return

    data_colheita = utils.converter_data(input("Digite a data de colheita (dd/mm/aaaa): "))
    if not utils.validar_data(data_colheita): return

    plantacao = {"nome": nome, "semente": sementes[semente], "plantio": data_plantio, "colheita": data_colheita}

    lista.append(plantacao)

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
    utils.subtitulo("Plantação cadastrada com sucesso! ✅") # Subtitulo usado como suporte
    utils.pausa_tempo()


def editar(lista):

    # Primeira Tela: Mostras as Plantações
    utils.limpar_tela()
    utils.subtitulo("Edição de Plantação")
    if not utils.validar_lista(lista): return

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")
    
    escolha = utils.validar_inteiro(input("\nEscolha a plantação para editar: "), lista)
    if escolha is None: return

    # Segunda Tela: Edição da Plantação
    plantacao = lista[escolha]

    utils.limpar_tela()
    utils.titulo(f"Editando: {plantacao['nome']}")

    campos = ["Nome", "Semente", "Data de Plantio", "Data de Colheita"] # Campos que o usuário vê
    mapa_campos = ["nome", "semente", "plantio", "colheita"] # Campos reais do dicionário

    for i, campo in enumerate(campos):
        print(f"{i}. {campo}")

    campo_escolhido = utils.validar_inteiro(input("\nQual campo deseja editar? "), campos)

    if mapa_campos[campo_escolhido] == "semente":
        semente, sementes = auxiliares.mostrar_sementes()
        novo_valor = sementes[semente]

    elif campo_escolhido in [2, 3]: # Se for data, valida
        novo_valor = utils.converter_data(novo_valor)
        utils.verificar_data(novo_valor)

    else:
        novo_valor = input(f"Digite o novo valor para {campos[campo_escolhido]}: ")

    chave = mapa_campos[campo_escolhido]
    plantacao[chave] = novo_valor

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
    utils.subtitulo("Plantação atualizada com sucesso! ✅") # Subtitulo usado como suporte
    utils.pausa_tempo()


def visualizar(lista):

    utils.limpar_tela()
    utils.subtitulo("Visualização de Plantações")
    utils.validar_lista(lista)

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    escolha = utils.validar_inteiro(input("\nEscolha uma plantação para analisar: "), lista)
    if escolha is None: return

    analisar(lista, escolha)


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

    escolha = utils.validar_inteiro(input("\nDigite uma das opções acima: "), opcoes)
    if escolha is None: return

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
    utils.validar_lista(lista)

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    escolha = utils.validar_inteiro(input("\nEscolha uma plantação para apagar: "), lista)
    if escolha is None: return

    confirmar = input(f"Tem certeza que deseja apagar {lista[escolha]['nome']}? (s/n) ").lower()
    if confirmar != 's':
        return
    lista.pop(escolha)

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
    utils.subtitulo("Plantação deletada com sucesso! ✅")
    utils.pausa_tempo()
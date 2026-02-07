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

    data_plantio = utils.ajustar_data(input("Digite a data de plantio (dd/mm/aaaa): "))
    if not utils.validar_data(data_plantio): return

    data_colheita = utils.ajustar_data(input("Digite a data de colheita (dd/mm/aaaa): "))
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
    if utils.validar_lista(lista): return

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
    if campo_escolhido is None: return

    if mapa_campos[campo_escolhido] == "semente":
        semente, sementes = auxiliares.mostrar_sementes()
        if semente is None: return
        novo_valor = sementes[semente]

    else:
        novo_valor = input(f"Digite o novo valor para {campos[campo_escolhido]}: ")

    if campo_escolhido in [2, 3]: # Se for data, valida
        novo_valor = utils.ajustar_data(novo_valor)
        if not utils.validar_data(novo_valor): return

    chave = mapa_campos[campo_escolhido]
    plantacao[chave] = novo_valor

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
    utils.subtitulo("Plantação atualizada com sucesso! ✅") # Subtitulo usado como suporte
    utils.pausa_tempo()


def visualizar(lista):

    utils.limpar_tela()
    utils.subtitulo("Visualização de Plantações")
    if utils.validar_lista(lista): return

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

    dias = (datetime.strptime(plantacao['colheita'], utils.formato_data) - datetime.strptime(plantacao['plantio'], utils.formato_data))

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
        auxiliares.resumo_colheita_mensal(lista)

    # Status de Colheita
    elif escolha == 1:
        auxiliares.status_colheita(lista)

    # Análise de Colheita
    elif escolha == 2:
        auxiliares.analise_colheita(lista)

    utils.pausa_pressione()


def apagar(lista):

    utils.limpar_tela()
    utils.subtitulo("Apagar Plantação")
    if utils.validar_lista(lista): return

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")

    escolha = utils.validar_inteiro(input("\nEscolha uma plantação para apagar: "), lista)
    if escolha is None: return

    confirmar = input(f"Tem certeza que deseja apagar {lista[escolha]['nome']}? (s/n) ").lower()
    if confirmar != 's': return

    lista.pop(escolha)

    utils.salvar_dados(lista) # Salva a Plantação em um arquivo JSON
    utils.subtitulo("Plantação deletada com sucesso! ✅")
    utils.pausa_tempo()
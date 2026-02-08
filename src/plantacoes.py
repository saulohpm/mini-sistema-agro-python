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

    tipo_idx, dicionario_plantas = auxiliares.mostrar_plantas()
    if tipo_idx is None: return

    planta_nome = auxiliares.mostrar_plantas2(tipo_idx, dicionario_plantas)
    if planta_nome is None: return

    data_plantio = utils.ajustar_data(input("Digite a data de plantio (dd/mm/aaaa): "))
    if not utils.validar_data(data_plantio): return

    data_colheita = utils.ajustar_data(input("Digite a data de colheita (dd/mm/aaaa): "))
    if not utils.validar_data(data_colheita): return

    if utils.comparar_datas(data_colheita, data_plantio, "de colheita", "de plantio"): return

    plantacao = {
        "nome": nome, 
        "semente": planta_nome, 
        "plantio": data_plantio, 
        "colheita": data_colheita
    }

    lista.append(plantacao)
    utils.salvar_dados(lista)
    utils.subtitulo("Plantação cadastrada com sucesso! ✅")
    utils.pausa_tempo()


def editar(lista):
    utils.limpar_tela()
    utils.subtitulo("Edição de Plantação")
    if utils.validar_lista(lista): return

    for i, plantacao in enumerate(lista):
        print(f"{i}. {plantacao['nome']}")
    
    escolha = utils.validar_inteiro(input("\nEscolha a plantação para editar: "), lista)
    if escolha is None: return

    plantacao = lista[escolha]
    utils.limpar_tela()
    utils.titulo(f"Editando: {plantacao['nome']}")

    campos = ["Nome", "Semente", "Data de Plantio", "Data de Colheita"] # Usuário vê
    mapa_campos = ["nome", "semente", "plantio", "colheita"] # Python trabalha

    for i, campo in enumerate(campos):
        print(f"{i}. {campo}")

    campo_escolhido = utils.validar_inteiro(input("\nQual campo deseja editar? "), campos)
    if campo_escolhido is None: return
    
    if campo_escolhido == 1:
        tipo_idx, dados_plantas = auxiliares.mostrar_plantas()
        if tipo_idx is None: return

        novo_valor = auxiliares.mostrar_plantas2(tipo_idx, dados_plantas)
        if novo_valor is None: return

    elif campo_escolhido in [2, 3]: # Se for Data (índices 2 ou 3)
        novo_valor = utils.ajustar_data(input(f"Digite a nova {campos[campo_escolhido]}: "))
        if not utils.validar_data(novo_valor): return
        
        if campo_escolhido == 2: # Editando Plantio
            if utils.comparar_datas(plantacao['colheita'], novo_valor, "de Colheita", "de Plantio"): return
        else: # Editando Colheita
            if utils.comparar_datas(novo_valor, plantacao['plantio'], "de Colheita", "de Plantio"): return

    # Se for Nome (índice 0) ou qualquer outro campo de texto
    else:
        novo_valor = input(f"Digite o novo valor para {campos[campo_escolhido]}: ")

    # Atualiza o dicionário e salva
    chave = mapa_campos[campo_escolhido]
    plantacao[chave] = novo_valor

    utils.salvar_dados(lista)
    utils.subtitulo("Plantação atualizada com sucesso! ✅")
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

    dias = utils.dias_para_colheita(plantacao['colheita'])

    if dias >= 0: print(f"Faltam {dias} dias para a colheita!")
    else: print(f"Se passaram {dias * -1} dias da colheita!")

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
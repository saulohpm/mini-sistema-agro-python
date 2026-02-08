from datetime import datetime
import src.utils as utils

def mostrar_plantas():

    plantas = utils.carregar_dados(utils.PLANTAS)

    print(f"\nTipos de Plantas disponíveis: \n")

    for i, tipo in enumerate(plantas):
        print(f"{i}. {tipo}")

    tipo_de_planta = utils.validar_inteiro(input(f"\nDigite o tipo de planta que voçê quer acessar: "), plantas)
    return tipo_de_planta, plantas


def mostrar_plantas2(tipo_de_planta, plantas, coluna=3):

    categorias = list(plantas.keys())
    escolha_txt = categorias[tipo_de_planta]
    selecoes = plantas[escolha_txt]

    print(f"\nEscolha uma das seguintes {escolha_txt}: \n")

    printar = ""
    for i in range(len(selecoes)):
        item = f"{i}. {selecoes[i]}"
        printar += f"{item:^25} | "
        if (i + 1) % coluna == 0:
            print(printar.rstrip(" | "))
            printar = ""

    if printar:
        print(printar.rstrip(" | "))

    indice = utils.validar_inteiro(input(f"\nDigite a {escolha_txt.lower()} a ser utilizada: "), selecoes)
    
    return selecoes[indice] if indice is not None else None

def resumo_colheita_mensal(lista):

    print(f"Total de platações cadastradas: {len(lista)}")
    print(f"Colheitas para o mês de {utils.mesatual()}: ")
    utils.barrinha()
        
    for plantacao in lista:
        plantacao_analisada = datetime.strptime(plantacao["colheita"], utils.formato_data)
        if plantacao_analisada.month == utils.mesatual(False):
            print(f"\n- {plantacao['nome']}")
            print(f"Semente: {plantacao['semente']}")
            print(f"Colheita: {plantacao['colheita']}")
            print("")


def status_colheita(lista):

    hoje = datetime.today()

    concluidas = []
    emandamento = []
    agendadas = []

    for plantacao in lista:
        datadecolheita = datetime.strptime(plantacao["colheita"], utils.formato_data)
        datadeplantio = datetime.strptime(plantacao["plantio"], utils.formato_data)
        if hoje >= datadecolheita:
            concluidas.append(plantacao)
        elif datadeplantio < hoje < datadecolheita:
            emandamento.append(plantacao)
        else:
            agendadas.append(plantacao)
                
    print(f"\n🟢 Concluídas ({len(concluidas)})")
    for plantacao in concluidas:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

    print(f"\n🟡 Em andamento ({len(emandamento)})")
    for plantacao in emandamento:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

    print(f"\n🔵 Plantios Agendados ({len(agendadas)})")
    for plantacao in agendadas:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

def analise_colheita(lista):
    
    print(f"{'| PROXIMAS COLHEITAS (PRÓXIMOS 7 DIAS) |':^{utils.largura_tela}}\n")

    cont = 0
    for plantacao in lista:
        diasatecolheita = utils.dias_para_colheita(plantacao['colheita'])
        if 0 <= diasatecolheita <= 7:
            print(f"- {plantacao['nome']} em {diasatecolheita} dias")
            cont += 1
        
    if cont == 0: print(f"\n{'NÃO Há COLHEITAS NOS PRÓXIMOS 7 DIAS':^{utils.largura_tela}}\n")
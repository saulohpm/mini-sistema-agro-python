from datetime import datetime
import src.utils as utils

def mostrar_sementes(coluna=3):
    """
    Este bloco é uma função de suporte que tem os seguintes objetivos:
    1) Explica a lógica usada para imprimir sementes em colunas de 3 (editável) para que o usuário escolha corretamente.
    2) Declara uma variavel input, valida e depois retorna a variavel inputada e a lista sementes.
    """

    sementes = utils.carregar_dados(utils.SEMENTES)

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

    semente = utils.validar_inteiro(input("\nDigite a semente a ser utilizada: "), sementes)
    return semente, sementes

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
        
    print("")
        
    print(f"🟢 Concluídas ({len(concluidas)})")
    for plantacao in concluidas:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

    print(f"\n🟡 Em andamento ({len(emandamento)})")
    for plantacao in emandamento:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

    print(f"\n🔵 Plantios Agendados ({len(agendadas)})")
    for plantacao in agendadas:
        print(f"- {plantacao['nome']} | Colheita: {plantacao['colheita']}")

def analise_colheita(lista):
    
    print(f"{'| PROXIMAS COLHEITAS (PRÓXIMOS 7 DIAS) |':^{utils.largura_tela}}")

    hoje = datetime.today()

    cont = 0
    for plantacao in lista:
        datadecolheita = datetime.strptime(plantacao["colheita"], utils.formato_data)
        diasatecolheita = (datadecolheita - hoje).days
        if 0 <= diasatecolheita <= 7:
            print(f"- {plantacao['nome']} | {plantacao['semente']} -> {diasatecolheita} dias")
            cont += 1
        
    if cont == 0: print(f"\n{'NÃO Há COLHEITAS NOS PRÓXIMOS 7 DIAS':^{utils.largura_tela}}")
from datetime import datetime, date, time, timedelta
from pathlib import Path
import json
import time
import os

BASE_DIR = Path(__file__).resolve().parent
PLANTACOES = BASE_DIR.parent / "data" / "plantacoes.json"
PLANTAS = BASE_DIR.parent / "data" / "plantas.json"

largura_tela = 100
formato_data = "%d/%m/%Y"

def salvar_dados(lista, arquivo=None):
    if arquivo is None:
        arquivo = PLANTACOES

    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


def carregar_dados(arquivo=None):
    if arquivo is None:
        arquivo = PLANTACOES

    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausa_pressione():
    input("\nPressione Enter [↵] para continuar...")


def pausa_tempo(segundos=3):
    time.sleep(segundos)


def titulo(string):
    print(f"{'=' * largura_tela}")
    print(f"{string:^100}")
    print(f"{'=' * largura_tela}")


def subtitulo(string):
    print(f"{'-' * largura_tela}")
    print(f"{string:^100}")
    print(f"{'-' * largura_tela}")


def barrinha():
    print(f"{'-' * largura_tela}")


def ajustar_data(data_str):
    if len(data_str) == 8:
        nova_data_str = data_str[:2] + "/" + data_str[2:4] + "/" + data_str[4:]
        return nova_data_str
    else:
        return data_str


def validar_data(data_str):
    try:
        datetime.strptime(data_str, formato_data)
        return True
    except ValueError:
        print("❌ ERRO: Data inválida!")
        pausa_pressione()
        return False


def validar_lista(lista):
    '''
    Verifica se a lista está VAZIA (True: está | False: não está)
    '''
    if not lista:
        print("⚠️  Nenhuma plantação cadastrada.")
        pausa_pressione()
        return True
    return False


def validar_inteiro(valor, lista=None):
    '''
    Verifica se é inteiro e se está em um intervalo (range(len(lista))
    Retorna None caso contrário e o valor caso verdadeiro
    '''
    try:
        valor = int(valor)
        if lista is not None and valor not in range(len(lista)):
            print("❌ ERRO: Fora do intervalo")
            pausa_pressione()
            return None
        return valor
    except ValueError:
        print("❌ ERRO: Entrada inválida")
        pausa_pressione()
        return None


def dias_para_colheita(data_de_colheita):
    diferenca = (datetime.strptime(data_de_colheita, formato_data) - datetime.today()).days
    return diferenca


def comparar_datas(maior, menor, str_maior="maior", str_menor="menor"):
    '''
    Recebe duas datas em formato string (maior e menor)
    Compara levando em consideração quem deve ser maior e menor
    Retorna caso data maior <= data menor
    '''

    maior = datetime.strptime(maior, formato_data)
    menor = datetime.strptime(menor, formato_data)

    if maior <= menor: print(f"❌ A data {str_maior} deve ser posterior a data {str_menor}."); pausa_pressione(); return True

def mesatual(argumento=True):
    '''
    True: Retorna uma string com nome do mês, exemplo: Março
    False: Retorna um inteiro representando o mês correspondente
    '''
    mes = date.today().month
    if argumento == True:
        meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        return meses[mes - 1]
    else:
        return mes
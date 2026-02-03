from datetime import datetime, date, time, timedelta
import json
import time
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ARQUIVO = BASE_DIR.parent / "data" / "plantacoes.json"

def salvar_dados(lista):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def pausa_pressione():
    input("\nPressione Enter [↵] para continuar...")


def pausa_tempo(segundos=3):
    time.sleep(segundos)


def titulo(string):
    print(f"{'=' * 50:^50}")
    print(f"{string:^50}")
    print(f"{'=' * 50:^50}")


def subtitulo(string):
    print(f"{'-' * 50:^50}")
    print(f"{string:^50}")
    print(f"{'-' * 50:^50}")


def barrinha():
    print(f"{'-' * 50:^50}")


def converter_data(data_str):
    if len(data_str) == 8:
        nova_data_str = data_str[:2] + "/" + data_str[2:4] + "/" + data_str[4:]
        return nova_data_str
    else:
        return data_str


def validar_data(data_str):
    try:
        datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False


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
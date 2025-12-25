from datetime import datetime, date, time, timedelta
import time

plantacoes = []

def menu():
    while True:
        opcoes = ["Cadastrar Plantação","Editar Plantacao","Visualizar Plantações Cadastradas","Sair"]
        tamanho_opcoes = len(opcoes)
        titulo("🌱 SISTEMA DE MANUSEIO DE PLANTAÇÕES 🌱")
        for i in range(tamanho_opcoes):
            print(f"{str(i) + '. '  + opcoes[i]:<50}")
        try:
            escolha = int(input("Selecione a opção desejada do menu: "))
            if escolha == tamanho_opcoes - 1:
                barrinha()
                print(f"{'Programa Encerrado!':^50}")
                barrinha()
                break
            elif escolha == 0:
                cadastrar(plantacoes)
            elif escolha == 2:
                visualizar(plantacoes)
            elif escolha == 1:
                editar(plantacoes)
            else:
                print("ERRO: Digite o número que acompanha a opção desejada no menu!")
        except ValueError:
            barrinha()
            print("ERRO: Digite o número que acompanha a opção desejada no menu!")


def cadastrar(lista):
    barrinha()
    cadastro = []
    nome = input("Digite o nome da plantação que quer cadastrar: ")
    semente = input("Digite a semente utilizada: ")
    tempo_plantacao = input("Digite o dia de plantação no formato dd/mm/aaaa: ")
    tempo_plantacao = converter_data(tempo_plantacao)
    if validar_data(tempo_plantacao) is True:
        tempo_colheita = input("Digite o dia de colheita estipulado no formato dd/mm/aaaa: ")
        tempo_colheita = converter_data(tempo_colheita)
        if validar_data(tempo_colheita) is True:
            cadastro.append(nome)
            cadastro.append(semente)
            cadastro.append(tempo_plantacao)
            cadastro.append(tempo_colheita)
            lista.append(cadastro)
            barrinha()
            print(f"{'Plantação Cadastrada com Sucesso! ✅'}")
        else:
            print("ERRO: Digite uma data válida, no formado correto!")
    else:
        print("ERRO: Digite uma data válida, no formado correto!")


def visualizar(lista):
    barrinha()
    if not lista:
        print("Não foram encontrados cadastros de plantacões!")
    else:
        print(f"{'Foram encontradas as seguintes plantações:':<50}")
        for i in range(len(lista)):
                print(f"{i}. {lista[i][0]}")
        try:
            escolha = int(input("Digite uma das opções acima: "))
            if 0 <= escolha < len(lista):
                barrinha()  
                analisar(lista, escolha)
            else:
                print("ERRO: Digite o número que acompanha a opção desejada no menu!")
        except ValueError:
            print("ERRO: Digite o número que acompanha a opção desejada no menu!")


def analisar(lista, inteiro):
    barrinha()
    plantacao_escolhida = plantacoes[inteiro]
    titulo(f"Analisando plantação com nome '{plantacao_escolhida[0]}'")
    print(f"Semente: {plantacao_escolhida[1]}")
    print(f"Plantação em: {plantacao_escolhida[2]}")
    print(f"Possível Colheita em: {plantacao_escolhida[3]}")
    dias = datetime.strptime(plantacao_escolhida[3], '%d/%m/%Y') - datetime.strptime(plantacao_escolhida[2], '%d/%m/%Y')
    print(f"Faltam {dias.days} dias para a colheita!")


def editar(lista):
    if not lista:
        pass
    else:
        if not lista:
            print("Não foram encontrados cadastros de plantacões!")
        else:
            print(f"{'Foram encontradas as seguintes plantações:':<50}")
        for i in range(len(lista)):
                print(f"{i}. {lista[i][0]}")
        escolha = int(input("Digite uma das opções acima: "))
        if 0 <= escolha < len(lista):
            barrinha()
        else:
            print("ERRO: Digite o número que acompanha a opção desejada no menu!")        
        barrinha()

        plantacao_escolhida = lista[escolha]
        titulo(f"Analisando plantação com nome '{plantacao_escolhida[0]}'")
        print(f"Semente: {plantacao_escolhida[1]}")
        print(f"Plantação em: {plantacao_escolhida[2]}")
        print(f"Possível Colheita em: {plantacao_escolhida[3]}")
        dias = datetime.strptime(plantacao_escolhida[3], '%d/%m/%Y') - datetime.strptime(plantacao_escolhida[2], '%d/%m/%Y')
        print(f"Faltam {dias.days} dias para a colheita!")
        barrinha()

        opcoes = ["Nome da Plantação","Semente","Data de Plantação","Data de Colheita"]
        for i in range(len(opcoes)):
            print(f"{i}. {opcoes[i]}")
        edicao = int(input("Selecione quais das opções desejas editar: "))
        plantacao_escolhida[edicao] = input(f"Digite a atualização do(a) {opcoes[edicao]}: ")
        barrinha()
        print("Plantação Atualizada com Sucesso! ✅")
        barrinha()


def titulo(string):
    print(f"{'=' * 50:^50}")
    print(f"{string:^50}")
    print(f"{'=' * 50:^50}")


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

menu()
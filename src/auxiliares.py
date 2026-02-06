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
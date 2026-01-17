from plantacoes import menu
import utils

if __name__ == "__main__":
    plantacoes = utils.carregar_dados()
    menu(plantacoes)

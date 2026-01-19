from plantacoes import menu
from usuario import carregar_usuarios, cadastrodeusuario
import utils

if __name__ == "__main__":

    usuarios = carregar_usuarios()
    cadastrodeusuario(usuarios)

    plantacoes = utils.carregar_dados()
    menu(plantacoes, usuarios)

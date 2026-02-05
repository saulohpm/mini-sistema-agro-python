from pathlib import Path
import src.utils as utils
import json
import os

BASE_DIR = Path(__file__).resolve().parent
ARQUIVO_USUARIOS = BASE_DIR.parent / "data" / "usuarios.json"

usuarios = []

def salvar_usuarios(lista):
    with open(ARQUIVO_USUARIOS, "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)

def carregar_usuarios():
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def cadastrodeusuario(usuarios):
    utils.limpar_tela()
    if not usuarios:
        utils.titulo("🌱  Bem-vindo(a) ao Sistema! 🌱")
        nome = input("✏️  Digite seu nome ou como quer ser chamado(a): ")

        usuarios.append({"nome": nome})
        salvar_usuarios(usuarios)

        print(f"\n🎉  Obrigado, {nome}! Você será redirecionado(a) para o menu do Sistema em instantes!")

        utils.pausa_tempo()
    else:
        return

def apagarusuario(usuarios):
    usuarios.pop(0)
import xmltodict
import os

diretorio = os.path.abspath('Conversor xml em xmls')  # Diretório atual
arquivo = os.path.join(diretorio, 'nfs')
lista_arquivos = os.listdir(arquivo)


def pegar_infos(arquivos):
    pass


for arquivo in lista_arquivos:
    pegar_infos(arquivo)
import xmltodict
import os
import json
def pegar_infos(nome_arquivo):
    print(f"PEGOU AS INFORMAÇÕES DE {nome_arquivo}")
    with open(f"Conversor xml em xmls/nfs/{arquivo}", "rb") as arquivo_xml:       # abrir o arquivo
        dic_arquivo = xmltodict.parse(arquivo_xml)      # transforma o arquivo xml em um dicionario em python
        # print(json.dumps(dic_arquivo, indent=4))     # facilitar a visualiação do código em xml e captar as informações essencias
        info_nf = dic_arquivo["NFe"]['infNFe']
        numero_nota = info_nf['@Id']
        empresa_emissora = info_nf['emit']["xNome"]
        nome_cliente = info_nf["dest"]["xNome"]
        endereco = info_nf["dest"]["enderDest"]
        peso = info_nf["transp"]["vol"]["pesoB"]
        print(f"Numero_nota {numero_nota}\nEmpresa_emissora {empresa_emissora}\nNome_cliente {nome_cliente}\nEndereco {endereco}\nPeso {peso}")
diretorio = os.path.abspath('Conversor xml em xmls')  # Diretório atual
arquivo = os.path.join(diretorio, 'nfs')
lista_arquivos = os.listdir(arquivo)


for arquivo in lista_arquivos:
    pegar_infos(arquivo)
    break
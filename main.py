import xmltodict
import os
import json
import pandas as pd



def pegar_infos(nome_arquivo, valores):
    print(f"PEGOU AS INFORMAÇÕES DE {nome_arquivo}")
    with open(f"Conversor xml em xmls/nfs/{arquivo}", "rb") as arquivo_xml:       # abrir o arquivo
        dic_arquivo = xmltodict.parse(arquivo_xml)      # transforma o arquivo xml em um dicionario em python
        # print(json.dumps(dic_arquivo, indent=4))     # facilitar a visualiação do código em xml e captar as informações essencias
       
        try:        # com as informações tratadas não ha mais necessidade do try except
            if "NFe" in dic_arquivo:
                info_nf = dic_arquivo["NFe"]['infNFe']
            else:    
                info_nf = dic_arquivo["nfeProc"]["NFe"]['infNFe']
            numero_nota = info_nf['@Id']
            empresa_emissora = info_nf['emit']["xNome"]
            nome_cliente = info_nf["dest"]["xNome"]
            endereco = info_nf["dest"]["enderDest"]
            if "vol" in info_nf["transp"]:
                peso = info_nf["transp"]["vol"]["pesoB"]
            else:
                peso = 'Não informado'
            # print(f"Numero_nota {numero_nota}\nEmpresa_emissora {empresa_emissora}\nNome_cliente {nome_cliente}\nEndereco {endereco}\nPeso {peso}\n")
            valores.append([numero_nota, empresa_emissora,nome_cliente, endereco, peso])
        except Exception as e:
            print(e)
            print(json.dumps(dic_arquivo, indent=4))
            
diretorio = os.path.abspath('Conversor xml em xmls')  # Diretório atual
arquivo = os.path.join(diretorio, 'nfs')
lista_arquivos = os.listdir(arquivo)       

colunas = ["Numero_nota", "empresa_emissora","nome_cliente", "endereco", "peso"]
valores = []
for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

tabela = pd.DataFrame(columns=colunas,data=valores)    
tabela.to_excel("NotasFiscais.xlsx", index=False)
# não gera a coluna com o numero do indice pois o excel ja gera isso
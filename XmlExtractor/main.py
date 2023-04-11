import csv
import os
import xml.etree.ElementTree as ET

# pasta onde estão os arquivos XML
pasta = 'xml'

# lista de nomes de arquivos XML
arquivos = os.listdir(pasta)

# criar as listas para armazenar os valores dos elementos XML
dhEmi = []
xFant = []
nNF = []
vProd = []
vNF = []
CFOP = []

# iterar sobre cada arquivo XML na pasta
for arquivo in arquivos:
    if arquivo.endswith('.xml'):
        # obter do arquivo
        caminho_arquivo = os.path.join(pasta, arquivo)

        # abrir o arquivo XML
        tree = ET.parse(caminho_arquivo)

        # obter a raiz do arquivo XML
        root = tree.getroot()

        # iterar sobre os elementos XML e adicionar os valores solicitados em cada lista
        adicionou_xFant = False
        for elem in root.iter():
            if elem.tag.endswith('dhEmi'):
                dhEmi.append(str(elem.text)[:10])
            elif elem.tag.endswith('xFant'):
                if not adicionou_xFant:
                    xFant.append(str(elem.text)[:20])
                    adicionou_xFant = True
            elif elem.tag.endswith('xNome'):
                if len(xFant) < len(nNF):  # verificar se xFant já foi adicionado para essa nota
                    if not adicionou_xFant:
                        xFant.append(str(elem.text)[:20])
                        adicionou_xFant = True
            elif elem.tag.endswith('nNF'):
                nNF.append(elem.text)
                adicionou_xFant = False
            elif elem.tag.endswith('vProd'):
                vProd.append(elem.text)
            elif elem.tag.endswith('vNF'):
                vNF.append(elem.text)
            elif elem.tag.endswith('CFOP'):
                CFOP.append(elem.text)

# abrir o arquivo CSV para escrita
with open('dados.csv', mode='w', newline='') as arquivo_csv:
    # criar o objeto escritor para o arquivo CSV
    writer = csv.writer(arquivo_csv)

    # escrever o cabeçalho do arquivo CSV
    writer.writerow(['dhEmi', 'xFant', 'nNF', 'vProd', 'vNF', 'CFOP'])

    # escrever os dados no arquivo CSV
    for i in range(len(dhEmi)):
        linha = [dhEmi[i], xFant[i], nNF[i], vProd[i], vNF[i], CFOP[i]]  # acessar o primeiro item da lista xFant
        writer.writerow(linha)
        print(linha)

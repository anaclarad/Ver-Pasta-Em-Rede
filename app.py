import os

size = 0 
caminho_pasta1= 'C:/Users/anacl/OneDrive/Área de Trabalho/desafios_codigo'
caminho_pasta2= 'C:/Users/anacl/OneDrive/Área de Trabalho/Exemplos'
caminho_pasta3= 'C:/Users/anacl/OneDrive/Área de Trabalho/exercicios_python'

caminhos = [caminho_pasta1,caminho_pasta2,caminho_pasta3]

def obter_tamanho_diretorio(caminho):
    tamanho_total_arquivo = 0
    with os.scandir(caminho) as arquivos:
        for arquivo in arquivos:
            if arquivo.is_file():
                tamanho_total_arquivo += arquivo.stat().st_size
            elif arquivo.is_dir():
                tamanho_total_arquivo += obter_tamanho_diretorio(arquivo.path)
    return tamanho_total_arquivo

for caminho in caminhos:
    tamanho_arquivo = obter_tamanho_diretorio(caminho)   
    print(f"Arquivo: {caminho} - Tamanho: {tamanho_arquivo}")


            
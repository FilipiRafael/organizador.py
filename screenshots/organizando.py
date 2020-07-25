import os

# 1. Criar pastas para imagens, vídeos, audios, documentos e outros
# 2. Pegar o nome dos arquivos
# 3. Pegar a extensão do arquivo para determinar o tipo
# 4. Mover arquivos para as pastas correspondentes

# Listas para cada tipo

audios_ext = ['.mp3', '.wav']
videos_ext = ['.mp4', '.mov', '.avi']
imagens_ext = ['.jpg', '.jpeg', '.png']
documentos_ext = ['.txt', '.log', '.doc', '.pdf']

def pegar_extensao(nome):
    indice = nome.rfind('.')
    return nome[indice:]

def organizar(diretório):
    AUDIO_DIR = os.path.join(diretório, "audios")
    IMAGENS_DIR = os.path.join(diretório, "imagens")
    DOCS_DIR = os.path.join(diretório, "documentos")
    VIDEOS_DIR = os.path.join(diretório, "vídeos")
    OUTROS_DIR = os.path.join(diretório, "outros")

    if not os.path.isdir(AUDIO_DIR):
        os.mkdir(AUDIO_DIR)
    elif not os.path.isdir(IMAGENS_DIR):
        os.mkdir(IMAGENS_DIR)
    elif not os.path.isdir(DOCS_DIR):
        os.mkdir(DOCS_DIR)
    elif not os.path.isdir(VIDEOS_DIR):
        os.mkdir(VIDEOS_DIR)
    elif not os.path.isdir(OUTROS_DIR):
        os.mkdir(OUTROS_DIR)

    nomes_arquivos = os.listdir(diretório)
    nova_pasta = ''

    for arquivo in nomes_arquivos:
        if os.path.isfile(os.path.join(diretório, arquivo)):
            # Extensão dos arquivos para letras minúsculas
            extensao = str.lower(pegar_extensao(arquivo))
            if extensao in audios_ext:
                nova_pasta = AUDIO_DIR
            elif extensao in videos_ext:
                nova_pasta = VIDEOS_DIR
            elif extensao in imagens_ext:
                nova_pasta = IMAGENS_DIR
            elif extensao in documentos_ext:
                nova_pasta = DOCS_DIR
            else:
                nova_pasta = OUTROS_DIR
            
            # Move o arquivo para a pasta correspondente
            arquivo_antigo = os.path.join(diretório, arquivo)
            arquivo_novo = os.path.join(nova_pasta, arquivo)
            os.rename(arquivo_antigo, arquivo_novo)
            print(f'{arquivo_antigo} movido com sucesso para {arquivo_novo}!')


if __name__ == '__main__':
    organizar("downloads")

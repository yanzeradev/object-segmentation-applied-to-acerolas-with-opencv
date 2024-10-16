import cv2
import numpy as np
import os

def mascara01(imagem):
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    lim_inf = np.array([0, 110, 95])    
    lim_sup = np.array([15, 255, 255])
    return cv2.inRange(imagem_hsv, lim_inf, lim_sup)

def mascara02(imagem):
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    lim_inf = np.array([0, 90, 70])
    lim_sup = np.array([15, 255, 255])
    return cv2.inRange(imagem_hsv, lim_inf, lim_sup)

def carregar_imagem(caminho_imagem):

    extensao_valida = caminho_imagem.lower().endswith(('.jpg', '.jpeg', '.png'))
    tamanho_arquivo = os.path.getsize(caminho_imagem) / (1024 * 1024)

    if not extensao_valida:
        print("Formato de arquivo inválido. Por favor, carregue uma imagem .jpg, .jpeg ou .png.")
        return None
    elif tamanho_arquivo > 20:
        print(f"Tamanho do arquivo ({tamanho_arquivo:.2f} MB) excede o limite de 20MB.")
        return None
    else:
        return cv2.imread(caminho_imagem)

def exibir_imagem(nome_janela, imagem):
    resize_imagem = cv2.resize(imagem, (600, 400))
    cv2.imshow(nome_janela, resize_imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def solicitar_escolha():
    while True:
        try:
            escolha = int(input("Escolha uma mascara:\nMascara01 - 1\nMascara02 - 2\nSair - 0\nOpcao: "))
            if escolha in [0, 1, 2]:
                return escolha
            else:
                print("Opção inválida. Por favor, escolha 0, 1 ou 2.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro válido.")

caminho_imagem = 'acerola1.jpg'
imagem = carregar_imagem(caminho_imagem)
if imagem is not None:
    escolha = solicitar_escolha()

    while escolha != 0:
        if escolha == 1:
            mascara = mascara01(imagem)
            segmentacao_vermelha = cv2.bitwise_and(imagem, imagem, mask=mascara)

            exibir_imagem('Imagem Original', imagem)
            exibir_imagem('Imagem Segmentada', segmentacao_vermelha)
            exibir_imagem('Mascara binaria', mascara)
        
        elif escolha == 2:
            mascara = mascara02(imagem)
            segmentacao_vermelha = cv2.bitwise_and(imagem, imagem, mask=mascara)

            exibir_imagem('Imagem Original', imagem)
            exibir_imagem('Imagem Segmentada', segmentacao_vermelha)
            exibir_imagem('Mascara binaria', mascara)

        escolha = solicitar_escolha()
else:
    print("Erro ao carregar a imagem. Verifique o caminho do arquivo.")

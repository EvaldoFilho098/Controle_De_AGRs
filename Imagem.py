"""
TRATAMENTO DE IMAGENS 
"""

from tkinter import *
from PIL import Image, ImageTk


def redimensionar(diretorio,x,y):
    
    image = Image.open(diretorio)
    image = image.resize((x,y))
    return ImageTk.PhotoImage(image)

#def redimensionar(img, x, y):
#
#    aux = img.resize((x, y), Image.ANTIALIAS)
#    nova_imagem = ImageTk.PhotoImage(aux)
#    return nova_imagem

#Img_Local = PhotoImage(file="Icons\\Logo.png")

# if type(Img_Local) == PhotoImage:
    # print("Sim")

'''
img_add_original = (Image.open("Icons\\botao-adicionar.png"))

img_edi_original = (Image.open("Icons\\editar.png"))

img_rem_original = (Image.open("Icons\\lixeira-de-reciclagem.png"))

img_sim_original = (Image.open("Icons\\confirmacao.png"))

img_nao_original = (Image.open("Icons\\fechar.png"))

img_sav_original = (Image.open("Icons\\salve-.png"))

img_inf_original = (Image.open("Icons\\contato.png"))

#img_atu_original= (Image.open("Icons\\atualizar.png"))

Logo_original = (Image.open("Icons\\Logo.png"))

Logo_STexto_original = (Image.open("Icons\\Logo_STexto.png"))
'''
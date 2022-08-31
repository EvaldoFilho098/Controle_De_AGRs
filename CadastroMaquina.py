from tkinter import font
from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_CadastroMaquina(Tela):

    def __init__(self, master):
        super().__init__(master, "cadastro")

        self.criar_Campos()
        self.adicionar_Campos()

        self.root.mainloop()

    def criar_Campos(self):

        self.titulo = Texto_Imagem(self.root, 'Nova Máquina','maquina.png',bg=cor_fundo, font=fonte_Destaques_24)
        self.nome = Texto_Entrada(self.root, 'Nome: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.marca = Texto_Entrada(self.root, 'Marca: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.modelo = Texto_Entrada(self.root, 'Modelo: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.Ip = Texto_Entrada(self.root, 'IP: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.MAC = Texto_Entrada(self.root, 'MAC: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.bitlocker = Texto_Entrada(self.root, 'Bitlocker: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.termo_doacao = Texto_Entrada(self.root, 'Termo Doação: ', bg=cor_fundo,font=fonte_Textos_12,font_entr=fonte_Textos_11)
        self.botao_cadastrar = Botao(self.root, 'Cadastrar')

    def adicionar_Campos(self):

        self.titulo.Frame.pack(side=TOP, pady=30, anchor='center')
        self.lista_widgets.append(self.titulo)

        self.nome.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.nome)

        self.marca.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.marca)

        self.modelo.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.modelo)

        self.Ip.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.Ip)

        self.MAC.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.MAC)

        self.bitlocker.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.bitlocker)

        self.termo_doacao.Frame.pack(side=TOP, pady=15, anchor='center')
        self.lista_widgets.append(self.termo_doacao)

        self.botao_cadastrar.pack(side=BOTTOM, pady=20, anchor='center')
        self.lista_widgets.append(self.botao_cadastrar)


root = Tk()
tela_CadastroMaquina(root)

from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_LoginADM(Tela):

    def __init__(self, master):
        super().__init__(master, "pequena")
        
        self.criar_Campos()
        self.adicionar_Campos()
        
        self.root.mainloop()
        
    def criar_Campos(self):
        
        self.titulo = Texto(self.root,'Login de Administrador',bg=cor_fundo,font=fonte_Destaques_24)
        self.login = Texto_Entrada(self.root,'Login: ',bg=cor_fundo)
        self.senha = Texto_Entrada(self.root,'Senha: ',bg=cor_fundo,show='*')
        self.botao_entrar = Botao(self.root,'Entrar',bg=cor_frames,fg=cor_fontes_entradas)
        
    def adicionar_Campos(self):
        
        self.titulo.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.titulo)
        
        self.login.Frame.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.login)
        
        self.senha.Frame.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.senha)
        
        self.botao_entrar.pack(side=TOP,pady=25,anchor='center')
        self.lista_widgets.append(self.botao_entrar)

root = Tk()
tela_LoginADM(root)

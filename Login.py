from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD

class tela_Login(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.Menus()
        self.nova_opcao("Cadastrar Funcionário",'')
        
        self.criar_Frames()
        self.adicionar_Frames()
        
        self.criar_Campos()
        self.adicionar_Campos()
        
        self.root.mainloop()
    
    def criar_Frames(self):
        
        self.Frame_campos = Frame(self.root)
        self.Frame_campos.configure(
            width=500,
            height=500,
            bg=cor_contraste_fundo
        )
        
    def adicionar_Frames(self):
        
        self.Frame_campos.place(relx=0.25,rely=0.25,relwidth=0.5,relheight=0.5)
        self.lista_widgets.append(self.Frame_campos)
        
    def criar_Campos(self):
        
        self.titulo = Texto(self.Frame_campos,'LOGIN',bg=cor_contraste_fundo,fg=cor_fonte_contraste_fundo,font=fonte_Titulos_32)
        self.espaco = Texto(self.Frame_campos,'',bg=cor_contraste_fundo,font=fonte_Mediana_18)
        self.espaco2 = Texto(self.Frame_campos,'',bg=cor_contraste_fundo,font=fonte_Mediana_18)
        self.login = Texto_Entrada(self.Frame_campos,'Login: ',bg=cor_contraste_fundo)
        self.senha = Texto_Entrada(self.Frame_campos,'Senha: ',bg=cor_contraste_fundo,show='*')
        self.botao_entrar = Botao(self.Frame_campos,'Entrar',bg=cor_entradas,fg=cor_fontes_entradas)
        
    def adicionar_Campos(self):
        
        self.titulo.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.titulo)
        
        self.espaco.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.espaco)
        
        self.login.Frame.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.login)
        
        self.senha.Frame.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.senha)
        
        self.espaco2.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.espaco2)
        
        self.botao_entrar.pack(side=TOP,pady=25,anchor='center')
        self.lista_widgets.append(self.botao_entrar)
        
        
root = Tk()
tela_Login(root)
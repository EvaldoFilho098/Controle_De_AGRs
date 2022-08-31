from tkinter import font
from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_CadastroFuncionario(Tela):

    def __init__(self, master):
        super().__init__(master, "cadastro")

        self.criar_Campos()
        self.adicionar_Campos()

        self.root.mainloop()

    def criar_Campos(self):
        
        self.lista_cargos = ['Suporte Técnico','Intermediador','Treinador','Desenvolvedor']
        self.varPriv = IntVar()
        
        self.titulo = Texto_Imagem(self.root,'Novo Funcionário','editar.png',bg=cor_fundo,font=fonte_Destaques_24)
        self.nome = Texto_Entrada(self.root,'Nome: ',bg=cor_fundo)
        self.email = Texto_Entrada(self.root,'E-mail: ',bg=cor_fundo)
        self.login = Texto_Entrada(self.root,'Login: ',bg=cor_fundo)
        self.senha = Texto_Entrada(self.root,'Senha: ',bg=cor_fundo,show='*')
        self.confirmar_senha = Texto_Entrada(self.root,'Confirmar Senha: ',bg=cor_fundo,show='*',font=fonte_Textos_9)
        self.cargo = Texto_Seleciona(self.root,'Cargo: ',self.lista_cargos)
        self.espaco = Texto(self.root,'',font=fonte_Mediana_14)
        self.privADM = Botao_Radio(self.root,'Administrador',self.varPriv,1)
        self.privFUNC = Botao_Radio(self.root,'Funcionário',self.varPriv,0)
        self.botao_cadastrar = Botao(self.root,'Cadastrar')
        
    def adicionar_Campos(self):
        
        self.titulo.Frame.pack(side=TOP,pady=30,anchor='center')
        self.lista_widgets.append(self.titulo)
        
        self.nome.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.nome)
        
        self.email.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.email)
        
        self.login.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.login)
        
        self.senha.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.senha)
        
        self.confirmar_senha.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.confirmar_senha)
        
        self.cargo.Frame.pack(side=TOP,pady=10,anchor='center')
        self.lista_widgets.append(self.cargo)
        
        self.espaco.pack(side=TOP,pady=5,anchor='center')
        self.lista_widgets.append(self.espaco)
        
        self.privADM.pack(side=TOP,padx=95,anchor='w')
        self.lista_widgets.append(self.privADM)
        
        self.privFUNC.pack(side=TOP,padx=95,anchor='w')
        self.lista_widgets.append(self.privFUNC)
        
        self.botao_cadastrar.pack(side=BOTTOM,pady=20,anchor='center')
        self.lista_widgets.append(self.botao_cadastrar)

root = Tk()
tela_CadastroFuncionario(root)

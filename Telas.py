from tkinter import *
from tkinter import ttk
from turtle import width
from PIL import Image
from Mensagens import *
from Cores import *
from Widgets import *

class Tela():       
    
    def __init__(self,master,tipo,titulo=''):    
        
        self.root = master
        self.Tela(tipo,titulo)
    
    def Tela(self,tipo="comum",titulo=''):
        
        #### Titulo da Pagina
        if titulo == '':
            self.root.title("Meta Certificado Digital - Controle de AGR's")
        else:
            self.root.title(titulo)
            
        #### Tamanho da Pagina
        if tipo == "comum":
            self.width = "1224"
            self.height = "700"
            
            self.root.minsize(width = int(self.width), height= int(self.height))
            
            #Nao redimensionar
            self.root.resizable(width = True, height = True)
            
        elif tipo == "cadastro":
            self.width = "400"
            self.height = "600"
            
            #Nao redimensionar
            self.root.resizable(width = False, height = False)
            
        elif tipo == "pequena":
            self.width = "500"
            self.height = "250"
            
            #Nao redimensionar
            self.root.resizable(width = False, height = False)
            
        #Tamanho da tela
        self.root.geometry(self.width + "x" + self.height)
        
        #Cor de Fundo
        self.root.configure(background = cor_fundo)
        
        #Transparencia
        self.root.attributes("-alpha",0.995)
        
        #Icone
        self.root.iconbitmap(default="Icones/icon.ico")
        
        self.lista_widgets = []
        
    def Menus(self):
        
        self.Menu_bar = Menu(self.root)
        
        self.root.config(menu=self.Menu_bar)
        
        self.Menu_Opcoes = Menu(self.Menu_bar, tearoff=0)
        
        self.Menu_bar.add_cascade(label='Opções',menu=self.Menu_Opcoes)
    
    def nova_opcao(self,nome,comando):
        self.Menu_Opcoes.add_command(label=nome,command=comando)
        
    def limpar_tela(self):

        for item in self.lista_widgets:
            item.grid_forget()
            item.pack_forget()
            item.place_forget()
            
        self.lista_widgets = []
            
    def cabecalho_padrao(self,titulo,funcionario):
        
        self.frame_cabecalho = Frame(self.root)
        self.frame_cabecalho.configure(
            bg=cor_fundo,
            width=1024,
            height=25
        )
        self.frame_cabecalho.pack(side=TOP,fill='x')
        
        self.Logo_Meta = PhotoImage(file="Imagens\\Logo_.png")
        self.Logo = Label(self.frame_cabecalho,image=self.Logo_Meta,bg=cor_fundo)
        self.Logo.place(relx=0.0,rely=0.0)
        
        self.titulo_cabecalho = Texto(self.frame_cabecalho,titulo,font=fonte_Titulos_30)
        self.titulo_cabecalho.pack(side=TOP,padx=25,pady=20,anchor="center")
        
        self.lbl_bem_vindo = Texto(self.frame_cabecalho,"Bem Vindo,")
        self.lbl_bem_vindo.place(relx=0.85,rely=0.2)
        
        self.lbl_funcionario = Texto(self.frame_cabecalho,funcionario)
        self.lbl_funcionario.place(relx=0.85,rely=0.5)
    
                
    
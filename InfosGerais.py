from textwrap import fill
from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD

class tela_InfosGerais(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.Menus()
        self.nova_opcao("Gerar Relatório",'')
        
        self.cabecalho_padrao('Informaçoes Gerais','Evaldo')
        
        self.criar_Frames()
        self.adicionar_Frames()
        self.criar_Infos()
        self.adicionar_Infos()
        
        self.root.mainloop()
    
    def criar_Frames(self):
        self.Frame1 = Frame(self.root)
        self.Frame1.configure(
            bg=cor_fundo,
            height=250,
        )
        
        self.Frame2 = Frame(self.root)
        self.Frame2.configure(
            bg=cor_fundo,
            height=250,
            width=400,
        )
        
        self.Frame3 = Frame(self.root)
        self.Frame3.configure(
            bg=cor_fundo,
            height=250,
            width=400,
        )
        
    def adicionar_Frames(self):
        self.Frame1.pack(side=TOP,anchor='center',fill=X,pady=50)
        self.lista_widgets.append(self.Frame1)
        
        self.Frame2.pack(side=TOP,anchor='center',pady=50)
        self.lista_widgets.append(self.Frame2)
        
        self.Frame3.pack(side=TOP,anchor='center',pady=50)
        self.lista_widgets.append(self.Frame3)
    
    def criar_Infos(self):
        
        self.cadastrados = Texto_Infos(self.Frame1,'76','CADASTRADOS',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        
        self.ativos = Texto_Infos(self.Frame2,'52','ATIVOS',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        self.pendentes = Texto_Infos(self.Frame2,'13','PENDENTES',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        self.inativos = Texto_Infos(self.Frame2,'5','INATIVOS',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        
        self.acmeta = Texto_Infos(self.Frame3,'5','AC META',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        self.acsoluti = Texto_Infos(self.Frame3,'5','AC SOLUTI',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        self.acdigital = Texto_Infos(self.Frame3,'5','AC DIGITAL',formato='centro',fg_1=cor_laranja,fg_2=cor_fonte_contraste_fundo,font_1=fonte_Titulos_34,font_2=fonte_Mediana_16)
        
    
    def adicionar_Infos(self):
        
        self.cadastrados.Frame.pack(side=TOP)
        self.lista_widgets.append(self.cadastrados)
        
        self.ativos.Frame.pack(side=LEFT,padx=50)
        self.lista_widgets.append(self.ativos)
        
        self.pendentes.Frame.pack(side=LEFT,padx=50)
        self.lista_widgets.append(self.pendentes)
        
        self.inativos.Frame.pack(side=LEFT,padx=50)
        self.lista_widgets.append(self.inativos)
        
        self.acmeta.Frame.pack(side=LEFT,padx=30)
        self.lista_widgets.append(self.acmeta)
        
        self.acsoluti.Frame.pack(side=LEFT,padx=30)
        self.lista_widgets.append(self.acsoluti)
        
        self.acdigital.Frame.pack(side=LEFT,padx=30)
        self.lista_widgets.append(self.acdigital)

root = Tk()
tela_InfosGerais(root)
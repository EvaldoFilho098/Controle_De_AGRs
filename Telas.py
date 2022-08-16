from tkinter import *
from tkinter import ttk
from PIL import Image

class Tela():       
    
    def __init__(self,master):    
        
        self.root = master
        self.Tela()
        self.Menus()
    
    def Tela(self):
         
        self.root.title("Meta Certificado Digital - Controle de AGR's")
        #Tamanho da self.rootela
        self.root.geometry("1024x600")
        #self.root.resizable(True,True)
        #self.root.maxsize(width=900,height=700)
        #self.root.minsize("1024x600")
        
        #Cor de Fundo
        self.root.configure(background = "#0F0F0F")
        #Nao redimensionar
        self.root.resizable(width = True, height = True)
        #Transparencia
        self.root.attributes("-alpha",0.99)
        #Icone
        self.root.iconbitmap(default="Icones/icon.ico")
        #Logo
        #self.logo = PhotoImage(file="icons/Logo.png")
        
    def Menus(self):
        self.Menu_bar = Menu(self.root)
        self.root.config(menu=self.Menu_bar)
        
        self.Menu_Opcoes = Menu(self.Menu_bar, tearoff=0)
        
        self.Menu_bar.add_cascade(label='Opções',menu=self.Menu_Opcoes)
        
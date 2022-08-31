from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *
from tkinter import DISABLED,NORMAL
import Banco_De_Dados as BD
from ibge.localidades import Estados

class tela_VisualizarAGRs(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.cabecalho_padrao("Visualizar AGRs","Evaldo")
        
        self.criar_frames_da_tela()
        self.adicionar_frames_da_tela()
        
        self.criar_campos()
        self.adicionar_campos()
        
        
        self.root.mainloop()
    
    def criar_frames_da_tela(self):
        
        self.frame_titulo_filtros = Frame(self.root)
        self.frame_titulo_filtros.configure(
            bg=cor_fundo
        )
        
        self.frame_filtros = Frame(self.root)
        self.frame_filtros.configure(
            bg = cor_fundo,
            highlightbackground=cor_laranja, 
            highlightthickness=4,
            highlightcolor=cor_laranja,
            #border=cor_laranja,
        )
        
        self.frame_botoes = Frame(self.root)
        self.frame_botoes.configure(
            bg = cor_fundo,    
        )
        
        self.frame_tabela = Frame(self.root)
        self.frame_tabela.configure(
            bg = cor_fundo,    
        )
    
    def adicionar_frames_da_tela(self):
        
        self.frame_titulo_filtros.place(relx=0.07,rely=0.15,relheight=0.05,relwidth=0.86)
        self.lista_widgets.append(self.frame_titulo_filtros)
        
        self.frame_filtros.place(relx=0.07,rely=0.21,relheight=0.22,relwidth=0.86)
        self.lista_widgets.append(self.frame_filtros)
        
        self.frame_botoes.place(relx=0.07,rely=0.45,relheight=0.06,relwidth=0.86)
        self.lista_widgets.append(self.frame_botoes)
        
        self.frame_tabela.place(relx=0.07,rely=0.53,relheight=0.38,relwidth=0.86)
        self.lista_widgets.append(self.frame_tabela)
    
    def criar_campos(self):
        
        self.titulo_filtros = Texto_Imagem(self.frame_titulo_filtros,'Filtros','filtro.png',font=fonte_Destaques_24)

        self.botao_voltar = Botao_Imagem(self.frame_titulo_filtros,'Voltar','voltar2.png',bg=cor_fundo)
        self.botao_voltar.configure(
            width=65
        )
        
        self.entrada_nome = Texto_Entrada(self.frame_filtros,'Nome: ',width=250,font_entr=fonte_Textos_12,bg_entr=cor_fonte_contraste_fundo)
        
        #self.entrada_cidade = Texto_Entrada(self.frame_filtros,'Cidade: ',width=250,font_entr=fonte_Textos_12,bg_entr=cor_fonte_contraste_fundo)
        self.lista_cidades = BD.Selecionar_Diferentes('cidade_agr','agrs')
        self.entrada_cidade = Texto_Seleciona(self.frame_filtros,'Cidade: ',self.lista_cidades,width=250,font_lista=fonte_Textos_12,bg_lista=cor_fonte_contraste_fundo)
        
        self.estados = Estados()
        self.lista_estados = self.estados.getSigla()
        #self.entrada_uf = Texto_Entrada(self.frame_filtros,'UF: ',width=250,font_entr=fonte_Textos_12,bg_entr=cor_fonte_contraste_fundo)
        self.entrada_uf = Texto_Seleciona(self.frame_filtros,'UF: ',self.lista_estados,width=250,font_lista=fonte_Textos_12,bg_lista=cor_fonte_contraste_fundo)
        
        self.lista_status = ['ATIVO','INATIVO','PENDENTE']
        self.entrada_status = Texto_Seleciona(self.frame_filtros,'Status: ',self.lista_status,width=250,font_lista=fonte_Textos_12)
        
        self.lista_termo = ['Não Possui Termo','Possui Termo']
        self.entrada_termo = Texto_Seleciona(self.frame_filtros,'Termo: ',self.lista_termo,width=250,font_lista=fonte_Textos_12)
        
        self.var_acmeta = BooleanVar()
        self.var_acmeta.set(False)
        self.ac_meta = Botao_Check(self.frame_filtros,'AC META',self.var_acmeta,font=fonte_Textos_11)
        
        self.var_acsoluti = BooleanVar()
        self.var_acsoluti.set(False)
        self.ac_soluti = Botao_Check(self.frame_filtros,'AC SOLUTI',self.var_acsoluti,font=fonte_Textos_11)
        
        self.var_acdigital = BooleanVar()
        self.var_acdigital.set(False)
        self.ac_digital = Botao_Check(self.frame_filtros,'AC DIGITAL',self.var_acdigital,font=fonte_Textos_11)
        
        self.botao_pesquisar = Botao(self.frame_botoes,'Pesquisar')
        
        self.botao_limpar = Botao(self.frame_botoes,'Limpar')
        
        self.colunas = ['ID','NOME','LOCAL','STATUS','AC META','AC SOLUTI','AC DIGITAL','TERMO']
        self.tabela_agrs = Tabela(self.frame_tabela,self.colunas,20,100,100)
        
        self.botao_selecionar = Botao(self.root,'Selecionar')
        
    
    def adicionar_campos(self):
        
        self.titulo_filtros.Frame.pack(side=LEFT,anchor='w')
        self.lista_widgets.append(self.titulo_filtros)
        
        self.botao_voltar.pack(side=RIGHT,anchor='e')
        self.lista_widgets.append(self.botao_voltar)
        
        self.entrada_nome.Frame.place(relx=0.05,rely=0.2)
        self.lista_widgets.append(self.entrada_nome)
        
        self.entrada_cidade.Frame.place(relx=0.05,rely=0.6)
        self.lista_widgets.append(self.entrada_cidade)
       
        self.entrada_uf.Frame.place(relx=0.35,rely=0.2)
        self.lista_widgets.append(self.entrada_uf)
        
        self.entrada_status.Frame.place(relx=0.35,rely=0.6)
        self.lista_widgets.append(self.entrada_status)
       
        self.entrada_termo.Frame.place(relx=0.65,rely=0.2)
        self.lista_widgets.append(self.entrada_termo)
        
        self.ac_meta.place(relx=0.65,rely=0.6)
        self.lista_widgets.append(self.ac_meta)

        self.ac_soluti.place(relx=0.76,rely=0.6)
        self.lista_widgets.append(self.ac_soluti)

        self.ac_digital.place(relx=0.88,rely=0.6)
        self.lista_widgets.append(self.ac_digital)
        
        self.botao_pesquisar.place(relx=0.20,rely=0.0,relwidth=0.25)
        self.lista_widgets.append(self.botao_pesquisar)
        
        self.botao_limpar.place(relx=0.55,rely=0.0,relwidth=0.25)
        self.lista_widgets.append(self.botao_limpar)
        
        self.tabela_agrs.Listagem.pack(side=TOP,anchor='center',fill=BOTH)
        self.lista_widgets.append(self.tabela_agrs)
        
        self.tabela_agrs.Barra_Y.place(relx=0.988,rely=0,relheight=1)
        self.lista_widgets.append(self.tabela_agrs.Barra_Y)
    
        #self.botao_selecionar.pack(side=BOTTOM,anchor='center',pady=5)
        self.lista_widgets.append(self.botao_selecionar)

root = Tk()
tela_VisualizarAGRs(root)
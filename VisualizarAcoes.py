from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
from tkinter import DISABLED, NORMAL
import Banco_De_Dados as BD


class tela_VisualizarAcoes(Tela):

    def __init__(self, master):
        super().__init__(master, "comum")

        self.cabecalho_padrao("Ações", "Evaldo")

        self.criar_frames_da_tela()
        self.adicionar_frames_da_tela()

        self.criar_campos()
        self.adicionar_campos()
        
        #self.criar_opcoes()
        #self.adicionar_opcoes()
        
        self.criar_camposInfos()
        self.adicionar_camposInfos()

        self.root.mainloop()

    def criar_frames_da_tela(self):

        self.frame_titulo_filtros = Frame(self.root)
        self.frame_titulo_filtros.configure(
            bg=cor_fundo
        )

        self.frame_filtros = Frame(self.root)
        self.frame_filtros.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )

        self.frame_botoes = Frame(self.root)
        self.frame_botoes.configure(
            bg=cor_fundo,
        )
        
        self.frame_opcoes = Frame(self.root)
        self.frame_opcoes.configure(
            bg=cor_fundo,
        )

        self.frame_tabela = Frame(self.root)
        self.frame_tabela.configure(
            bg=cor_fundo,
        )
        
        self.frame_infos = Frame(self.root)
        self.frame_infos.configure(
            bg=cor_contraste_fundo
        )

    def adicionar_frames_da_tela(self):

        self.frame_titulo_filtros.place(relx=0.07, rely=0.15,relheight=0.05, relwidth=0.86)
        self.lista_widgets.append(self.frame_titulo_filtros)

        self.frame_filtros.place(relx=0.07, rely=0.21,relheight=0.18, relwidth=0.86)
        self.lista_widgets.append(self.frame_filtros)

        self.frame_botoes.place(relx=0.07, rely=0.4,relheight=0.05, relwidth=0.86)
        self.lista_widgets.append(self.frame_botoes)
        
        self.frame_opcoes.place(relx=0.03, rely=0.47,relheight=0.05, relwidth=0.90)
        self.lista_widgets.append(self.frame_opcoes)

        self.frame_tabela.place(relx=0.03, rely=0.53,relheight=0.45, relwidth=0.63)
        self.lista_widgets.append(self.frame_tabela)
        
        self.frame_infos.place(relx=0.69, rely=0.53,relheight=0.45, relwidth=0.28)
        self.lista_widgets.append(self.frame_infos)

    def criar_campos(self):

        self.titulo_filtros = Texto_Imagem(self.frame_titulo_filtros, 'Filtros', 'filtro.png', font=fonte_Destaques_24)

        self.botao_voltar = Botao_Imagem(self.frame_titulo_filtros,'Voltar','voltar2.png',bg=cor_fundo)
        self.botao_voltar.configure(
            width=65,
        )

        self.entrada_Funcionario = Texto_Entrada(self.frame_filtros, 'Funcionário: ', width=320, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)

        self.entrada_data = Texto_Entrada(self.frame_filtros, 'Data: ', width=170, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)
        
        self.tipo_acao = ['ALTERAÇÃO','CADASTRO','PARAMETRIZAÇÃO','TREINAMENTO']
        self.entrada_tipo = Texto_Seleciona(self.frame_filtros, 'Tipo de Ação: ', self.tipo_acao, width=320, font_lista=fonte_Textos_12)
        
        self.botao_pesquisar = Botao(self.frame_botoes, 'Pesquisar')

        self.bota_limpar = Botao(self.frame_botoes, 'Limpar')

        self.colunas = ['ID','FUNCIONARIO','ACAO','DATA']
        self.tabela_acoes = Tabela(self.frame_tabela, self.colunas, 20, 150, 100)

    def adicionar_campos(self):

        self.titulo_filtros.Frame.pack(side=LEFT, anchor='w')
        self.lista_widgets.append(self.titulo_filtros)

        self.botao_voltar.pack(side=RIGHT, anchor='e')
        self.lista_widgets.append(self.botao_voltar)

        self.entrada_Funcionario.Frame.place(relx=0.05, rely=0.20)
        self.lista_widgets.append(self.entrada_Funcionario)

        self.entrada_data.Frame.place(relx=0.4, rely=0.20)
        self.lista_widgets.append(self.entrada_data)
        
        self.entrada_tipo.Frame.place(relx=0.6, rely=0.20)
        self.lista_widgets.append(self.entrada_tipo)

        self.botao_pesquisar.place(relx=0.20, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.botao_pesquisar)

        self.bota_limpar.place(relx=0.55, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.bota_limpar)

        self.tabela_acoes.Listagem.pack(side=TOP, anchor='center', fill=BOTH)
        self.lista_widgets.append(self.tabela_acoes)

        self.tabela_acoes.Barra_Y.place(relx=0.98, rely=0, relheight=1)
        self.lista_widgets.append(self.tabela_acoes.Barra_Y)

    def criar_camposInfos(self):
        
        self.frame_nomeFunc = Frame(self.frame_infos)
        self.frame_nomeFunc.configure(
            bg=cor_contraste_fundo,
            height=70,
            width=340,
        )
        
        self.frame_feitoAcao = Frame(self.frame_infos)
        self.frame_feitoAcao.configure(
            bg=cor_contraste_fundo,
            height=140,
            width=340,
        )
        
        self.frame_dataAcao = Frame(self.frame_infos)
        self.frame_dataAcao.configure(
            bg=cor_contraste_fundo,
            height=70,
            width=340,
        )
        
        self.nomeFunc = Texto_Infos(self.frame_nomeFunc,'Evaldo Filho','Funcionário','',bg=cor_contraste_fundo,fg_2=cor_frames,font_2=fonte_Textos_11,formato='centro')
        self.feitoAcao = Texto_Infos(self.frame_feitoAcao,'Cadastro do Funcionário Kevin Luiz Borges','Realizou','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Mediana_14,font_2=fonte_Textos_11,formato='centro')
        self.feitoAcao.Texto_Principal.configure(
            wraplength=300
        )
        self.dataAcao = Texto_Infos(self.frame_dataAcao,'29/08/2022 às 16:25','Data e Hora','',bg=cor_contraste_fundo,fg_2=cor_frames,font_2=fonte_Textos_11,formato='centro')
    
    def adicionar_camposInfos(self):
        
        self.frame_nomeFunc.pack(side=TOP,pady=5)
        self.lista_widgets.append(self.frame_nomeFunc)

        self.frame_feitoAcao.pack(side=TOP,pady=5)
        self.lista_widgets.append(self.frame_feitoAcao)

        self.frame_dataAcao.pack(side=TOP,pady=5)
        self.lista_widgets.append(self.frame_dataAcao)
        
        self.nomeFunc.Frame.pack(side=TOP,pady=10)
        self.lista_widgets.append(self.nomeFunc)

        self.feitoAcao.Frame.pack(side=TOP,pady=10)
        self.lista_widgets.append(self.feitoAcao)

        self.dataAcao.Frame.pack(side=TOP,pady=10)
        self.lista_widgets.append(self.dataAcao)


root = Tk()
tela_VisualizarAcoes(root)

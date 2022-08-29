from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
from tkinter import DISABLED, NORMAL
import Banco_De_Dados as BD


class tela_VisualizarFuncionarios(Tela):

    def __init__(self, master):
        super().__init__(master, "comum")

        self.cabecalho_padrao("Funcionários", "Evaldo")

        self.criar_frames_da_tela()
        self.adicionar_frames_da_tela()

        self.criar_campos()
        self.adicionar_campos()

        self.criar_opcoes()
        self.adicionar_opcoes()

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

        self.frame_titulo_filtros.place(
            relx=0.07, rely=0.15, relheight=0.05, relwidth=0.86)
        self.lista_widgets.append(self.frame_titulo_filtros)

        self.frame_filtros.place(relx=0.07, rely=0.21,
                                 relheight=0.18, relwidth=0.86)
        self.lista_widgets.append(self.frame_filtros)

        self.frame_botoes.place(relx=0.07, rely=0.4,
                                relheight=0.05, relwidth=0.86)
        self.lista_widgets.append(self.frame_botoes)

        self.frame_opcoes.place(relx=0.03, rely=0.47,
                                relheight=0.05, relwidth=0.90)
        self.lista_widgets.append(self.frame_opcoes)

        self.frame_tabela.place(relx=0.03, rely=0.53,
                                relheight=0.45, relwidth=0.63)
        self.lista_widgets.append(self.frame_tabela)

        self.frame_infos.place(relx=0.69, rely=0.53,
                               relheight=0.45, relwidth=0.28)
        self.lista_widgets.append(self.frame_infos)

    def criar_campos(self):

        self.titulo_filtros = Texto_Imagem(
            self.frame_titulo_filtros, 'Filtros', 'filtro.png', font=fonte_Destaques_24)

        self.botao_voltar = Botao_Imagem(self.frame_titulo_filtros,'Voltar','voltar2.png',bg=cor_fundo)
        self.botao_voltar.configure(
            width=65,
        )

        self.entrada_Nome = Texto_Entrada(
            self.frame_filtros, 'Nome: ', width=250, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)

        self.lista_privilegios = ['ADMINISTRADOR','PADRÃO']
        self.entrada_privilegios = Texto_Seleciona(
            self.frame_filtros, 'Privilégio: ', self.lista_privilegios, width=250, font_lista=fonte_Textos_12)

        self.lista_cargos = ['DESENVOLVEDOR', 'INTERMEDIADOR', 'TREINADOR','SUPORTE TÉCNICO']
        self.entrada_cargos = Texto_Seleciona(
            self.frame_filtros, 'Cargo: ', self.lista_cargos, width=250, font_lista=fonte_Textos_12)


        self.botao_pesquisar = Botao(self.frame_botoes, 'Pesquisar')

        self.bota_limpar = Botao(self.frame_botoes, 'Limpar')

        self.colunas = ['ID', 'NOME','LOGIN','EMAIL','CARGO','PRIVILEGIO']
        self.tabela_funcionarios = Tabela(
            self.frame_tabela, self.colunas, 20, 150, 100)

    def adicionar_campos(self):

        self.titulo_filtros.Frame.pack(side=LEFT, anchor='w')
        self.lista_widgets.append(self.titulo_filtros)

        self.botao_voltar.pack(side=RIGHT, anchor='e')
        self.lista_widgets.append(self.botao_voltar)

        self.entrada_Nome.Frame.place(relx=0.05, rely=0.40)
        self.lista_widgets.append(self.entrada_Nome)

        self.entrada_privilegios.Frame.place(relx=0.35, rely=0.40)
        self.lista_widgets.append(self.entrada_privilegios)

        self.entrada_cargos.Frame.place(relx=0.65, rely=0.40)
        self.lista_widgets.append(self.entrada_cargos)

        self.botao_pesquisar.place(relx=0.20, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.botao_pesquisar)

        self.bota_limpar.place(relx=0.55, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.bota_limpar)

        self.tabela_funcionarios.Listagem.pack(side=TOP, anchor='center', fill=BOTH)
        self.lista_widgets.append(self.tabela_funcionarios)

        self.tabela_funcionarios.Barra_Y.place(relx=0.98, rely=0, relheight=1)
        self.lista_widgets.append(self.tabela_funcionarios.Barra_Y)

    def criar_opcoes(self):

        self.botao_novoFunc = Botao_Imagem(
            self.frame_opcoes, '', 'adicionar.png')
        self.botao_novoFunc.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_editarFunc = Botao_Imagem(
            self.frame_opcoes, '', 'editar.png')
        self.botao_editarFunc.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_apagarFunc = Botao_Imagem(
            self.frame_opcoes, '', 'lixo.png')
        self.botao_apagarFunc.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_atualizar = Botao_Imagem(
            self.frame_opcoes, '', 'atualizar.png')
        self.botao_atualizar.configure(
            width=30,
            bg=cor_fundo
        )

    def adicionar_opcoes(self):

        self.botao_novoFunc.pack(side=LEFT)
        self.lista_widgets.append(self.botao_novoFunc)

        self.botao_editarFunc.pack(side=LEFT, padx=5)
        self.lista_widgets.append(self.botao_editarFunc)

        self.botao_apagarFunc.pack(side=LEFT, padx=5)
        self.lista_widgets.append(self.botao_apagarFunc)

        self.botao_atualizar.pack(side=LEFT, padx=5)
        self.lista_widgets.append(self.botao_atualizar)

    def criar_camposInfos(self):

        self.frame_nomeFunc = Frame(self.frame_infos)
        self.frame_nomeFunc.configure(
            bg=cor_contraste_fundo,
            height=70,
            width=340,
        )

        self.frame_cargoFunc = Frame(self.frame_infos)
        self.frame_cargoFunc.configure(
            bg=cor_contraste_fundo,
            height=70,
            width=340,
        )

        self.frame_privilegioFunc = Frame(self.frame_infos)
        self.frame_privilegioFunc.configure(
            bg=cor_contraste_fundo,
            height=70,
            width=340,
        )

        self.nomeFunc = Texto_Infos(self.frame_nomeFunc, 'KEVIN LUIS', 'Nome',
                                       '', bg=cor_contraste_fundo, fg_2=cor_frames, font_2=fonte_Textos_11, formato='centro')
        self.cargoFunc = Texto_Infos(self.frame_cargoFunc, 'SUPORTE TÉCNICO', 'Cargo', '', bg=cor_contraste_fundo,
                                   fg_2=cor_frames, font_2=fonte_Textos_11, formato='centro')
        self.privilegioFunc = Texto_Infos(self.frame_privilegioFunc, 'PADRÃO', 'Privilégio',
                                         '', bg=cor_contraste_fundo, fg_2=cor_frames, font_2=fonte_Textos_11, formato='centro')
        
    def adicionar_camposInfos(self):

        self.frame_nomeFunc.pack(side=TOP, pady=15)
        self.lista_widgets.append(self.frame_nomeFunc)

        self.frame_cargoFunc.pack(side=TOP, pady=15)
        self.lista_widgets.append(self.frame_cargoFunc)

        self.frame_privilegioFunc.pack(side=TOP, pady=15)
        self.lista_widgets.append(self.frame_privilegioFunc)

        self.nomeFunc.Frame.pack(side=TOP, pady=10)
        self.lista_widgets.append(self.nomeFunc)

        self.cargoFunc.Frame.pack(side=LEFT, pady=10, padx=5)
        self.lista_widgets.append(self.cargoFunc)

        self.privilegioFunc.Frame.pack(side=TOP)
        self.lista_widgets.append(self.privilegioFunc)


root = Tk()
tela_VisualizarFuncionarios(root)

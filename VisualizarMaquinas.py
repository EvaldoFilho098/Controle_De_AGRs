from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
from tkinter import DISABLED, NORMAL
import Banco_De_Dados as BD


class tela_VisualizarMaquinas(Tela):

    def __init__(self, master):
        super().__init__(master, "comum")

        self.cabecalho_padrao("Máquinas", "Evaldo")

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
            # border=cor_laranja,
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
        
        self.frame_opcoes.place(relx=0.03, rely=0.47,relheight=0.05, relwidth=0.87)
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

        self.entrada_AGR = Texto_Entrada(self.frame_filtros, 'AGR: ', width=250, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)

        self.entrada_maquina = Texto_Entrada(self.frame_filtros, 'Máquina: ', width=250, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)
        
        self.lista_status = ['PARAMETRIZADA','PENDENTE','DESPARAMETRIZADA']
        self.entrada_status = Texto_Seleciona(self.frame_filtros, 'Status: ', self.lista_status, width=250, font_lista=fonte_Textos_12)
        
        self.entrada_modelo = Texto_Entrada(self.frame_filtros, 'Modelo: ', width=250, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)
        
        self.entrada_marca = Texto_Entrada(self.frame_filtros, 'Marca: ', width=250, font_entr=fonte_Textos_12, bg_entr=cor_fonte_contraste_fundo)

        self.botao_pesquisar = Botao(self.frame_botoes, 'Pesquisar')

        self.bota_limpar = Botao(self.frame_botoes, 'Limpar')

        self.colunas = ['ID','NOME AGR','MAQUINA','MODELO','MARCA','STATUS']
        self.tabela_agrs = Tabela(self.frame_tabela, self.colunas, 20, 150, 100)

    def adicionar_campos(self):

        self.titulo_filtros.Frame.pack(side=LEFT, anchor='w')
        self.lista_widgets.append(self.titulo_filtros)

        self.botao_voltar.pack(side=RIGHT, anchor='e')
        self.lista_widgets.append(self.botao_voltar)

        self.entrada_AGR.Frame.place(relx=0.05, rely=0.20)
        self.lista_widgets.append(self.entrada_AGR)

        self.entrada_maquina.Frame.place(relx=0.35, rely=0.20)
        self.lista_widgets.append(self.entrada_maquina)

        self.entrada_modelo.Frame.place(relx=0.05, rely=0.60)
        self.lista_widgets.append(self.entrada_modelo)

        self.entrada_marca.Frame.place(relx=0.35, rely=0.60)
        self.lista_widgets.append(self.entrada_marca)

        self.entrada_status.Frame.place(relx=0.65, rely=0.20)
        self.lista_widgets.append(self.entrada_status)

        self.botao_pesquisar.place(relx=0.20, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.botao_pesquisar)

        self.bota_limpar.place(relx=0.55, rely=0.0, relwidth=0.25)
        self.lista_widgets.append(self.bota_limpar)

        self.tabela_agrs.Listagem.pack(side=TOP, anchor='center', fill=BOTH)
        self.lista_widgets.append(self.tabela_agrs)

        self.tabela_agrs.Barra_Y.place(relx=0.98, rely=0, relheight=1)
        self.lista_widgets.append(self.tabela_agrs.Barra_Y)

    def criar_opcoes(self):
        
        self.botao_novaMaquina = Botao_Imagem(self.frame_opcoes,'','adicionar.png')
        self.botao_novaMaquina.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_editarMaquina = Botao_Imagem(self.frame_opcoes,'','editar.png')
        self.botao_editarMaquina.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_parametrizarMaquina = Botao_Imagem(self.frame_opcoes,'','maquina+.png')
        self.botao_parametrizarMaquina.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_apagarMaquina = Botao_Imagem(self.frame_opcoes,'','lixo.png')
        self.botao_apagarMaquina.configure(
            width=30,
            bg=cor_fundo
        )
        self.botao_atualizar = Botao_Imagem(self.frame_opcoes,'','atualizar.png')
        self.botao_atualizar.configure(
            width=30,
            bg=cor_fundo
        )
        

        
    def adicionar_opcoes(self):
        
        self.botao_novaMaquina.pack(side=LEFT)
        self.lista_widgets.append(self.botao_novaMaquina)

        self.botao_editarMaquina.pack(side=LEFT,padx=5)
        self.lista_widgets.append(self.botao_editarMaquina)

        self.botao_parametrizarMaquina.pack(side=LEFT,padx=5)
        self.lista_widgets.append(self.botao_parametrizarMaquina)

        self.botao_apagarMaquina.pack(side=LEFT,padx=5)
        self.lista_widgets.append(self.botao_apagarMaquina)

        self.botao_atualizar.pack(side=LEFT,padx=5)
        self.lista_widgets.append(self.botao_atualizar)
        
    
    def criar_camposInfos(self):
        
        self.frame_nomeMaquina = Frame(self.frame_infos)
        self.frame_nomeMaquina.configure(
            bg=cor_contraste_fundo,
            )
        
        self.frame_infosMarcaMaquina = Frame(self.frame_infos)
        self.frame_infosMarcaMaquina.configure(
            bg=cor_contraste_fundo,
            )
        
        self.frame_infosMaquina = Frame(self.frame_infos)
        self.frame_infosMaquina.configure(
            bg=cor_contraste_fundo,
            )
        
        self.frame_statusMaquina = Frame(self.frame_infos)
        self.frame_statusMaquina.configure(
            bg=cor_contraste_fundo,
            )
        
        self.frame_agrAssinante = Frame(self.frame_infos)
        self.frame_agrAssinante.configure(
            bg=cor_contraste_fundo,
            )
        
        self.nomeMaquina = Texto_Infos(self.frame_nomeMaquina,'DESKTOP-564','Nome da Máquina','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_11,formato='padrao')
        self.marcaMaquina = Texto_Infos(self.frame_infosMarcaMaquina,'Samsung','Marca','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_9,formato='padrao')
        self.modeloMaquina = Texto_Infos(self.frame_infosMarcaMaquina,'Galaxy S2','Modelo','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_9,formato='padrao')
        self.infosIP = Texto_Infos(self.frame_infosMaquina,'123.655.123.321','IP','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_9,formato='padrao')
        self.infosMAC = Texto_Infos(self.frame_infosMaquina,'12-5C-8E-9C-30','MAC','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_9,formato='padrao')
        self.statusMaquina = Texto_Infos(self.frame_statusMaquina,'PARAMETRIZADA','Status','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_11,formato='padrao')
        self.agrAssinante = Texto_Infos(self.frame_agrAssinante,'Evaldo Filho','Assinada Por','',bg=cor_contraste_fundo,fg_2=cor_frames,font_1=fonte_Textos_12,font_2=fonte_Textos_11,formato='padrao')
    
    def adicionar_camposInfos(self):
        
        self.frame_nomeMaquina.place(relx=0.0,rely=0.0,relheight=0.2,relwidth=1)
        self.lista_widgets.append(self.frame_nomeMaquina)

        self.frame_infosMarcaMaquina.place(relx=0.0,rely=0.22,relheight=0.2,relwidth=1)
        self.lista_widgets.append(self.frame_infosMarcaMaquina)
        
        self.frame_infosMaquina.place(relx=0.0,rely=0.42,relheight=0.2,relwidth=1)
        self.lista_widgets.append(self.frame_infosMaquina)

        self.frame_statusMaquina.place(relx=0.0,rely=0.6,relheight=0.2,relwidth=1)
        self.lista_widgets.append(self.frame_statusMaquina)

        self.frame_agrAssinante.place(relx=0.0,rely=0.8,relheight=0.2,relwidth=1)
        self.lista_widgets.append(self.frame_agrAssinante)
        
        
        self.nomeMaquina.Frame.pack(side=LEFT,padx=20,pady=10)
        self.lista_widgets.append(self.nomeMaquina)

        self.marcaMaquina.Frame.place(relx=0.05,rely=0.0)
        self.lista_widgets.append(self.marcaMaquina)

        self.modeloMaquina.Frame.place(relx=0.5,rely=0.0)
        self.lista_widgets.append(self.modeloMaquina)
        
        self.infosIP.Frame.place(relx=0.05,rely=0.0)
        self.lista_widgets.append(self.infosIP)

        self.infosMAC.Frame.place(relx=0.5,rely=0.0)
        self.lista_widgets.append(self.infosMAC)

        self.statusMaquina.Frame.pack(side=LEFT,padx=20)
        self.lista_widgets.append(self.statusMaquina)

        self.agrAssinante.Frame.pack(side=LEFT,padx=20)
        self.lista_widgets.append(self.agrAssinante)


root = Tk()
tela_VisualizarMaquinas(root)

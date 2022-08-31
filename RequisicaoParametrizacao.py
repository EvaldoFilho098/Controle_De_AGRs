from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_ReqParametrizacao(Tela):

    def __init__(self, master):
        super().__init__(master, "cadastro")

        self.criar_frames()
        self.adicionar_frames()
        
        self.criar_campos()
        self.adicionar_campos()

        self.root.mainloop()
    
    def criar_frames(self):

        self.frame_titulo = Frame(self.root)
        self.frame_titulo.configure(
            bg=cor_fundo,
        )

        self.frame_agr = Frame(self.root)
        self.frame_agr.configure(
            bg=cor_fundo,
        )

        self.frame_obs = Frame(self.root)
        self.frame_obs.configure(
            bg=cor_fundo,
        )


    def adicionar_frames(self):

        self.frame_titulo.pack(side=TOP, anchor='center', fill=X, pady=30)
        self.lista_widgets.append(self.frame_titulo)

        self.frame_agr.place(relx=0.0, rely=0.35, relwidth=1, relheight=0.17)
        self.lista_widgets.append(self.frame_agr)

        self.frame_obs.place(relx=0.0, rely=0.55, relwidth=1, relheight=0.17)
        self.lista_widgets.append(self.frame_obs)


    def criar_campos(self):

        self.titulo = Texto_Imagem(self.frame_titulo,
                                   'Solicitar Parametrização', 'maquina+.png', font=fonte_Destaques_24)
        self.titulo.txt.config(
            wraplength=300
        )

        self.lbl_agr = Texto(self.frame_agr, 'AGR: ')

        self.lbl_nomeAGR = Texto(
            self.frame_agr, '', font=fonte_Textos_12_sublinhado)
        self.lbl_nomeAGR.config(
            wraplength=250
        )
        self.botao_selAGR = Botao(
            self.frame_agr, 'Procurar AGR', width=150, font=fonte_Textos_11)

        self.lbl_obs = Texto(self.frame_obs,"Observações:")
        self.entrada_obs = Text(self.frame_obs, font=fonte_Textos_11,height=300)
        self.entrada_obs.config(
            wrap='word'
        )

        self.botao_Requisitar = Botao(
            self.root, 'Solicitar')

    def adicionar_campos(self):

        # TITULO
        self.titulo.Frame.pack(side=TOP, anchor='center')
        self.lista_widgets.append(self.titulo)

        # SELECIONAR AGR
        self.lbl_agr.pack(side=TOP, anchor='w', padx=110)
        self.lista_widgets.append(self.lbl_agr)

        self.lbl_nomeAGR.place(relx=0.45, rely=0.0)
        self.lista_widgets.append(self.lbl_nomeAGR)

        if self.lbl_nomeAGR["text"] == '':
            self.botao_selAGR.place(relx=0.45, rely=0.0)
        else: 
            self.botao_selAGR.place(relx=0.45, rely=0.35)
            
        self.lista_widgets.append(self.botao_selAGR)

        # OBSERVACOES
        self.lbl_obs.pack(side=TOP, anchor='w', padx=30)
        self.lista_widgets.append(self.lbl_obs)

        self.entrada_obs.place(relx=0.45, rely=0.0, relwidth=0.45, relheight=1)
        self.lista_widgets.append(self.entrada_obs)


        # CONCLUIR
        self.botao_Requisitar.pack(side=BOTTOM, anchor='center', pady=25)
        self.lista_widgets.append(self.botao_Requisitar)

root = Tk()
tela_ReqParametrizacao(root)
from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_ReqTreinamento(Tela):

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

        self.frame_ac = Frame(self.root)
        self.frame_ac.configure(
            bg=cor_fundo,
        )

        self.frame_sistema = Frame(self.root)
        self.frame_sistema.configure(
            bg=cor_fundo,
        )

    def adicionar_frames(self):

        self.frame_titulo.pack(side=TOP, anchor='center', fill=X, pady=30)
        self.lista_widgets.append(self.frame_titulo)

        self.frame_agr.place(relx=0.0, rely=0.25, relwidth=1, relheight=0.17)
        self.lista_widgets.append(self.frame_agr)

        self.frame_ac.place(relx=0.0, rely=0.45, relwidth=1, relheight=0.17)
        self.lista_widgets.append(self.frame_ac)

        self.frame_sistema.place(
            relx=0.0, rely=0.65, relwidth=1, relheight=0.17)
        self.lista_widgets.append(self.frame_sistema)

    def criar_campos(self):

        self.titulo = Texto_Imagem(self.frame_titulo,'Solicitar Treinamento', 'treino+.png', font=fonte_Destaques_24)
        self.titulo.txt.config(
            wraplength=300
        )

        self.lbl_agr = Texto(self.frame_agr, 'AGR: ')

        self.lbl_nomeAGR = Texto(self.frame_agr, '', font=fonte_Textos_12_sublinhado)
        self.lbl_nomeAGR.config(
            wraplength=250
        )
        self.botao_selAGR = Botao(self.frame_agr, 'Procurar AGR', width=150, font=fonte_Textos_11)

        self.lbl_ac = Texto(self.frame_ac, 'Selecionar AC:')
        self.varAC = IntVar()
        self.botao_acmeta = Botao_Radio(self.frame_ac, 'AC META', self.varAC, 1, font=fonte_Textos_11)
        self.botao_acsoluti = Botao_Radio(self.frame_ac, 'AC SOLUTI', self.varAC, 2, font=fonte_Textos_11)
        self.botao_acdigital = Botao_Radio(self.frame_ac, 'AC DIGITAL', self.varAC, 3, font=fonte_Textos_11)

        self.lbl_sistema = Texto(self.frame_sistema, 'Sistema:')
        self.varsiteCompras = BooleanVar()
        self.botao_siteCompras = Botao_Check(self.frame_sistema, 'Site de Compras', self.varsiteCompras, font=fonte_Textos_11)
        self.varPresencial = BooleanVar()
        self.botao_Presencial = Botao_Check(self.frame_sistema, 'Presencial', self.varPresencial, font=fonte_Textos_11)
        self.varVideo = BooleanVar()
        self.botao_Video = Botao_Check(self.frame_sistema, 'Videoconferencia', self.varVideo, font=fonte_Textos_11)

        self.botao_Requisitar = Botao(self.root, 'Solicitar')

    def adicionar_campos(self):

        # TITULO
        self.titulo.Frame.pack(side=TOP, anchor='center')
        self.lista_widgets.append(self.titulo)

        # SELECIONAR AGR
        self.lbl_agr.pack(side=TOP, anchor='w', padx=70)
        self.lista_widgets.append(self.lbl_agr)

        self.lbl_nomeAGR.place(relx=0.35, rely=0.0)
        self.lista_widgets.append(self.lbl_nomeAGR)

        if self.lbl_nomeAGR["text"] == '':
            self.botao_selAGR.place(relx=0.35, rely=0.0)
        else: 
            self.botao_selAGR.place(relx=0.35, rely=0.35)
            
        self.lista_widgets.append(self.botao_selAGR)

        # SELECIONAR AC
        self.lbl_ac.pack(side=TOP, anchor='w', padx=70)
        self.lista_widgets.append(self.lbl_ac)

        self.botao_acmeta.place(relx=0.55, rely=0.0)
        self.lista_widgets.append(self.botao_acmeta)

        self.botao_acsoluti.place(relx=0.55, rely=0.27)
        self.lista_widgets.append(self.botao_acsoluti)

        self.botao_acdigital.place(relx=0.55, rely=0.54)
        self.lista_widgets.append(self.botao_acdigital)

        # SELECIONAR SISTEMA
        self.lbl_sistema.pack(side=TOP, anchor='w', padx=70)
        self.lista_widgets.append(self.lbl_sistema)

        self.botao_siteCompras.place(relx=0.48, rely=0.0)
        self.lista_widgets.append(self.botao_siteCompras)

        self.botao_Presencial.place(relx=0.48, rely=0.27)
        self.lista_widgets.append(self.botao_Presencial)

        self.botao_Video.place(relx=0.48, rely=0.54)
        self.lista_widgets.append(self.botao_Video)

        # CONCLUIR
        self.botao_Requisitar.pack(side=BOTTOM, anchor='center', pady=25)
        self.lista_widgets.append(self.botao_Requisitar)


root = Tk()
tela_ReqTreinamento(root)

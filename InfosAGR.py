from textwrap import fill
from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD


class tela_InfosAGR(Tela):

    def __init__(self, master):
        super().__init__(master, "comum")

        self.cabecalho()

        self.criar_Abas()
        self.adicionar_Frames()
        self.criar_Infos()
        self.adicionar_Infos()

        self.root.mainloop()

    def cabecalho(self):

        # CRIACAO
        self.frame_cabecalho = Frame(self.root)
        self.frame_cabecalho.configure(
            bg=cor_fundo
        )

        self.nome_agr = "EVALDO ARÊDES MORAIS FILHO"
        self.lbl_nome_agr = Texto_Imagem(
            self.frame_cabecalho, self.nome_agr, 'agr.png', font=fonte_Destaques_24)
        self.botao_sair = Botao_Imagem(
            self.frame_cabecalho, '', 'sair.png', width=30, bg=cor_fundo)

        # ADICIONAR A TELA

        self.frame_cabecalho.place(
            relx=0.0, rely=0.0, relheight=0.15, relwidth=1)
        self.lista_widgets.append(self.frame_cabecalho)

        self.lbl_nome_agr.Frame.pack(side=LEFT, padx=20)
        self.lista_widgets.append(self.lbl_nome_agr)

        self.botao_sair.pack(side=RIGHT, padx=20)
        self.lista_widgets.append(self.botao_sair)

    def criar_Abas(self):

        self.frame_Infos = Frame(self.root)
        self.frame_Infos.configure(
            bg=cor_fundo
        )
        self.frame_Infos.place(relx=0.02, rely=0.15,
                               relheight=0.80, relwidth=0.96)
        self.lista_widgets.append(self.frame_Infos)

        # Cria Notebook
        self.NotebookAbas = Abas(self.frame_Infos)

        # Cria cada Aba
        self.Config_AbaInformacoes()
        self.Config_AbaDocumentacao()
        self.Config_AbaMaquinas()
        self.Config_AbaTreinamentos()
        self.Config_AbaTabelaPrecos()
        self.Config_AbaACs()

        # Adiciona cada Aba ao Notebook
        self.NotebookAbas.add(self.abaInformacoes, text="Informações")
        self.NotebookAbas.add(self.abaDocumentacao, text="Documentação")
        self.NotebookAbas.add(self.abaMaquinas, text="Máquinas")
        self.NotebookAbas.add(self.abaTreinamentos, text="Treinamentos")
        self.NotebookAbas.add(self.abaTabelaPrecos, text="Tabela de Preços")
        self.NotebookAbas.add(self.abaACs, text="ACs")

        # Adiciona ao frame
        self.NotebookAbas.place(relx=0.0, rely=0.0, relwidth=1, relheight=1)
        self.lista_widgets.append(self.NotebookAbas)

    # Tela Pronta
    def Config_AbaInformacoes(self):

        # FRAME PRINCIPAL DA ABA
        self.abaInformacoes = Frame(self.NotebookAbas)
        self.abaInformacoes.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloInfosPessoais = Frame(self.abaInformacoes)
        self.frame_tituloInfosPessoais.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloInfosPessoais.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_infosPessoais = Frame(self.abaInformacoes)
        self.frame_infosPessoais.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_infosPessoais.place(
            relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_InfosPessoais = Texto_Imagem(
            self.frame_tituloInfosPessoais, 'Informações Pessoais', 'infos.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarInfos = Botao_Imagem(
            self.frame_tituloInfosPessoais, '', 'editar-branco.png', width=30)

        self.titulo_InfosPessoais.Frame.pack(side=LEFT)
        self.botao_EditarInfos.pack(side=RIGHT)

        # INFOS

        self.cidade = 'Ponta Porã'
        self.email = 'evaldo@email.com'
        self.termo = 'NÃO POSSUI TERMO'
        self.cpf = '108.222.689-25'
        self.telefone = '+55 67 99215-7224'

        self.lbl_cidade = Texto_Infos(self.frame_infosPessoais, self.cidade, 'Cidade', 'local.png',
                                      fg_2=cor_cabecalho_tabelas, font_1=fonte_Destaques_20, font_2=fonte_Mediana_14)
        self.lbl_email = Texto_Infos(self.frame_infosPessoais, self.email, 'E-mail', 'email.png',
                                     fg_2=cor_cabecalho_tabelas, font_1=fonte_Destaques_20, font_2=fonte_Mediana_14)
        self.lbl_termo = Texto_Infos(self.frame_infosPessoais, self.termo, 'Termo de Responsabilidade',
                                     'editar.png', fg_2=cor_cabecalho_tabelas, font_1=fonte_Destaques_20, font_2=fonte_Mediana_14)
        self.lbl_cpf = Texto_Infos(self.frame_infosPessoais, self.cpf, 'CPF', 'id.png',
                                   fg_2=cor_cabecalho_tabelas, font_1=fonte_Destaques_20, font_2=fonte_Mediana_14)
        self.lbl_telefone = Texto_Infos(self.frame_infosPessoais, self.telefone, 'Telefone', 'telefone.png',
                                        fg_2=cor_cabecalho_tabelas, font_1=fonte_Destaques_20, font_2=fonte_Mediana_14)

        self.lbl_cidade.Frame.place(relx=0.1, rely=0.1)
        self.lbl_email.Frame.place(relx=0.1, rely=0.4)
        self.lbl_termo.Frame.place(relx=0.1, rely=0.7)
        self.lbl_cpf.Frame.place(relx=0.6, rely=0.1)
        self.lbl_telefone.Frame.place(relx=0.6, rely=0.4)

    # Tela Pronta
    def Config_AbaDocumentacao(self):

        # FRAME PRINCIPAL DA ABA
        self.abaDocumentacao = Frame(self.NotebookAbas)
        self.abaDocumentacao.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloDocumentacao = Frame(self.abaDocumentacao)
        self.frame_tituloDocumentacao.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloDocumentacao.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_documentacao = Frame(self.abaDocumentacao)
        self.frame_documentacao.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_documentacao.place(
            relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_Documentacao = Texto_Imagem(
            self.frame_tituloDocumentacao, 'Documentação', 'docs.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarDoc = Botao_Imagem(
            self.frame_tituloDocumentacao, '', 'editar-branco.png', width=30)

        self.titulo_Documentacao.Frame.pack(side=LEFT)
        self.botao_EditarDoc.pack(side=RIGHT)

        # ELEMENTOS

        def sel_img(status):
            if status.upper() == 'OK':
                return 'check-ok.png'
            else:
                return 'check-not.png'

        self.copia_rg_cpf = 'PENDENTE'
        self.copia_cnh = 'PENDENTE'
        self.ctps = 'PENDENTE'
        self.titulo = 'PENDENTE'
        self.curriculo = 'OK'
        self.escolaridade = 'OK'
        self.decl_endereco = 'OK'
        self.rot_entr = 'OK'
        self.cert_digital = 'PENDENTE'
        self.curso_agr = 'OK'
        self.cer = 'PENDENTE'
        self.cadastro_sist = 'OK'

        self.lbl_copia_rg_cpf = Texto_Infos(self.frame_documentacao, 'RG E CPF', 'Cópia', sel_img(
            self.copia_rg_cpf), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_copia_cnh = Texto_Infos(self.frame_documentacao, 'CNH', 'Cópia', sel_img(
            self.copia_cnh), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_ctps = Texto_Infos(self.frame_documentacao, 'CTPS', 'Cópia', sel_img(
            self.ctps), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_titulo = Texto_Infos(self.frame_documentacao, 'Título', 'Cópia', sel_img(
            self.titulo), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_curriculo = Texto_Infos(self.frame_documentacao, 'Currículo', 'Cópia', sel_img(
            self.curriculo), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_escolaridade = Texto_Infos(self.frame_documentacao, 'Escolaridade', 'Cópia', sel_img(
            self.escolaridade), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_decl_endereco = Texto_Infos(self.frame_documentacao, 'Declaração de Endereço', 'Assinado', sel_img(
            self.decl_endereco), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_rot_entr = Texto_Infos(self.frame_documentacao, 'Roteiro de Entrevista', 'Assinado', sel_img(
            self.rot_entr), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_cert_digital = Texto_Infos(self.frame_documentacao, 'Certificado Digital', 'Modelo A3', sel_img(
            self.cert_digital), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_curso_agr = Texto_Infos(self.frame_documentacao, 'Curso de AGR', 'Certificado', sel_img(
            self.curso_agr), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_cer = Texto_Infos(self.frame_documentacao, '.CER', 'Arquivo', sel_img(
            self.cer), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)
        self.lbl_cadastro_sist = Texto_Infos(self.frame_documentacao, 'Cadastro', 'Site de Compras', sel_img(
            self.cadastro_sist), font_1=fonte_Mediana_18, font_2=fonte_Textos_11, fg_2=cor_cabecalho_tabelas, x=40, y=40)

        # PRIMEIRA COLUNA
        self.lbl_copia_rg_cpf.Frame.place(relx=0.05, rely=0.08)
        self.lbl_copia_cnh.Frame.place(relx=0.05, rely=0.3)
        self.lbl_ctps.Frame.place(relx=0.05, rely=0.53)
        self.lbl_titulo.Frame.place(relx=0.05, rely=0.77)

        # SEGUNDA COLUNA
        self.lbl_curriculo.Frame.place(relx=0.32, rely=0.08)
        self.lbl_escolaridade.Frame.place(relx=0.32, rely=0.3)
        self.lbl_decl_endereco.Frame.place(relx=0.32, rely=0.53)
        self.lbl_rot_entr.Frame.place(relx=0.32, rely=0.77)

        # TERCEIRA COLUNA
        self.lbl_cert_digital.Frame.place(relx=0.70, rely=0.08)
        self.lbl_curso_agr.Frame.place(relx=0.70, rely=0.3)
        self.lbl_cer.Frame.place(relx=0.70, rely=0.53)
        self.lbl_cadastro_sist.Frame.place(relx=0.70, rely=0.77)

    def Config_AbaMaquinas(self):

        # FRAME PRINCIPAL DA ABA
        self.abaMaquinas = Frame(self.NotebookAbas)
        self.abaMaquinas.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloMaquinas = Frame(self.abaMaquinas)
        self.frame_tituloMaquinas.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloMaquinas.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_Maquinas = Frame(self.abaMaquinas)
        self.frame_Maquinas.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_Maquinas.place(
            relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_Maquinas = Texto_Imagem(
            self.frame_tituloMaquinas, 'Máquinas', 'maquina.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarMaquinas = Botao_Imagem(
            self.frame_tituloMaquinas, '', 'editar-branco.png', width=30)

        self.titulo_Maquinas.Frame.pack(side=LEFT)
        self.botao_EditarMaquinas.pack(side=RIGHT)

    def Config_AbaTreinamentos(self):

        # FRAME PRINCIPAL DA ABA
        self.abaTreinamentos = Frame(self.NotebookAbas)
        self.abaTreinamentos.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloTreinamentos = Frame(self.abaTreinamentos)
        self.frame_tituloTreinamentos.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloTreinamentos.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_Treinamentos = Frame(self.abaTreinamentos)
        self.frame_Treinamentos.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_Treinamentos.place(
            relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_Treinamento = Texto_Imagem(
            self.frame_tituloTreinamentos, 'Treinamentos', 'treino.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarTreinamentos = Botao_Imagem(
            self.frame_tituloTreinamentos, '', 'editar-branco.png', width=30)

        self.titulo_Treinamento.Frame.pack(side=LEFT)
        self.botao_EditarTreinamentos.pack(side=RIGHT)

    def Config_AbaTabelaPrecos(self):

        # FRAME PRINCIPAL DA ABA
        self.abaTabelaPrecos = Frame(self.NotebookAbas)
        self.abaTabelaPrecos.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloTabelaPrecos = Frame(self.abaTabelaPrecos)
        self.frame_tituloTabelaPrecos.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloTabelaPrecos.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_TabelaPrecos = Frame(self.abaTabelaPrecos)
        self.frame_TabelaPrecos.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_TabelaPrecos.place(
            relx=0.02, rely=0.18, relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_TabelaPrecos = Texto_Imagem(
            self.frame_tituloTabelaPrecos, 'Tabela de Preços', 'dollar.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarTabelaPrecos = Botao_Imagem(
            self.frame_tituloTabelaPrecos, '', 'editar-branco.png', width=30)

        self.titulo_TabelaPrecos.Frame.pack(side=LEFT)
        self.botao_EditarTabelaPrecos.pack(side=RIGHT)

        self.frame_inTabelaPrecos = Frame(self.frame_TabelaPrecos)
        self.frame_inTabelaPrecos.place(
            relx=0.2, rely=0.05, relheight=0.9, relwidth=0.6)
        # self.frame_inTabelaPrecos.pack(side=TOP)

        self.colunas_tabela_precos = ["Produto", "Preço"]
        self.tabela_precos = Tabela(self.frame_inTabelaPrecos, self.colunas_tabela_precos, 20, 300, 300)
        style_tabela = ttk.Style()
        
        style_tabela.configure("myStyle.Treeview",
                fieldbackground=cor_fundo_tabela,
                foreground=cor_fonte_tabela,
                background=cor_fundo_tabela,
                font=fonte_Mediana_14,
                rowheight=37,
                relief="flat",
                )
        
        style_tabela.configure("myStyle.Treeview.Heading",
                        foreground=cor_fonte_cabecalho_tabela,
                        background=cor_cabecalho_tabelas,
                        font=fonte_Mediana_16
                        )
        self.tabela_precos.Barra_Y.pack(side=RIGHT, fill=Y, anchor='e')
        self.tabela_precos.Listagem.pack(side=TOP, fill=BOTH, anchor='center')
        
        lista_tp = BD.Tabela_De_Precos(17)
        self.tabela_precos.Inserir(lista_tp)

    # Tela Pronta
    def Config_AbaACs(self):

        # FRAME PRINCIPAL DA ABA
        self.abaACs = Frame(self.NotebookAbas)
        self.abaACs.configure(
            bg=cor_contraste_fundo
        )

        # ELEMENTOS DA ABA

        # FRAMES
        self.frame_tituloACs = Frame(self.abaACs)
        self.frame_tituloACs.configure(
            bg=cor_contraste_fundo,
        )
        self.frame_tituloACs.place(
            relx=0.02, rely=0.02, relheight=0.15, relwidth=0.96)

        self.frame_ACs = Frame(self.abaACs)
        self.frame_ACs.configure(
            bg=cor_fundo,
            highlightbackground=cor_laranja,
            highlightthickness=4,
            highlightcolor=cor_laranja,
        )
        self.frame_ACs.place(relx=0.02, rely=0.18,
                             relheight=0.80, relwidth=0.96)

        # TITULO
        self.titulo_ACs = Texto_Imagem(self.frame_tituloACs, 'Informações de ACs',
                                       'termo.png', font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.botao_EditarACs = Botao_Imagem(
            self.frame_tituloACs, '', 'editar-branco.png', width=30)

        self.titulo_ACs.Frame.pack(side=LEFT)
        self.botao_EditarACs.pack(side=RIGHT)

        # ELEMENTOS
        def sel_img(status):
            if status == 'ATIVO':
                return 'ativo.png'
            elif status == 'INATIVO':
                return 'inativo.png'
            elif status == 'PENDENTE':
                return 'pendente.png'

        # AC META
        self.frame_acmeta = Frame(self.frame_ACs)
        self.frame_acmeta.configure(
            bg=cor_contraste_fundo,
            highlightbackground=cor_fundo,
            highlightthickness=5,
            highlightcolor=cor_fundo
        )
        # self.frame_acmeta.place(relx=0.005,rely=0.0,relheight=1,relwidth=0.33)
        self.frame_acmeta.place(relx=0.05, rely=0.2,
                                relheight=0.55, relwidth=0.25)

        self.acmeta = "ATIVO"

        self.lbl_acmeta = Texto(
            self.frame_acmeta, "AC META", font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.lbl_acmeta.pack(side=TOP, pady=10, anchor='center')

        self.img_pendencia_acmeta = Texto_Imagem(self.frame_acmeta, '', sel_img(
            self.acmeta), x=70, y=70, bg=cor_contraste_fundo)
        self.img_pendencia_acmeta.Frame.pack(
            side=TOP, pady=10, anchor='center')

        self.lbl_pendencia_acmeta = Texto(
            self.frame_acmeta, self.acmeta, font=fonte_Destaques_24, bg=cor_contraste_fundo)
        self.lbl_pendencia_acmeta.pack(side=TOP, pady=10, anchor='center')

        # AC SOLUTI
        self.frame_acsoluti = Frame(self.frame_ACs)
        self.frame_acsoluti.configure(
            bg=cor_contraste_fundo,
            highlightbackground=cor_fundo,
            highlightthickness=5,
            highlightcolor=cor_fundo
        )
        # self.frame_acsoluti.place(relx=0.335,rely=0.0,relheight=1,relwidth=0.33)
        self.frame_acsoluti.place(
            relx=0.375, rely=0.2, relheight=0.55, relwidth=0.25)

        self.acsoluti = "INATIVO"

        self.lbl_acsoluti = Texto(
            self.frame_acsoluti, "AC SOLUTI", font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.lbl_acsoluti.pack(side=TOP, pady=10, anchor='center')

        self.img_pendencia_acsoluti = Texto_Imagem(self.frame_acsoluti, '', sel_img(
            self.acsoluti), x=70, y=70, bg=cor_contraste_fundo)
        self.img_pendencia_acsoluti.Frame.pack(
            side=TOP, pady=10, anchor='center')

        self.lbl_pendencia_acsoluti = Texto(
            self.frame_acsoluti, self.acsoluti, font=fonte_Destaques_24, bg=cor_contraste_fundo)
        self.lbl_pendencia_acsoluti.pack(side=TOP, pady=10, anchor='center')

        # AC DIGITAL
        self.frame_acdigital = Frame(self.frame_ACs)
        self.frame_acdigital.configure(
            bg=cor_contraste_fundo,
            highlightbackground=cor_fundo,
            highlightthickness=5,
            highlightcolor=cor_fundo
        )
        # self.frame_acdigital.place(relx=0.665,rely=0.0,relheight=1,relwidth=0.33)
        self.frame_acdigital.place(
            relx=0.70, rely=0.2, relheight=0.55, relwidth=0.25)

        self.acdigital = "PENDENTE"

        self.lbl_acdigital = Texto(
            self.frame_acdigital, "AC DIGITAL", font=fonte_Destaques_20, bg=cor_contraste_fundo)
        self.lbl_acdigital.pack(side=TOP, pady=10, anchor='center')

        self.img_pendencia_acdigital = Texto_Imagem(self.frame_acdigital, '', sel_img(
            self.acdigital), x=70, y=70, bg=cor_contraste_fundo)
        self.img_pendencia_acdigital.Frame.pack(
            side=TOP, pady=10, anchor='center')

        self.lbl_pendencia_acdigital = Texto(
            self.frame_acdigital, self.acdigital, font=fonte_Destaques_24, bg=cor_contraste_fundo)
        self.lbl_pendencia_acdigital.pack(side=TOP, pady=10, anchor='center')

    def adicionar_Frames(self):
        ...

    def criar_Infos(self):
        ...

    def adicionar_Infos(self):
        ...


root = Tk()
tela_InfosAGR(root)

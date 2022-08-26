from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD

class tela_Inicio(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.cabecalho_padrao("Controle de AGRs","Evaldo")
        
        self.criar_frames_da_tela()
        self.adicionar_frames_da_tela()
        
        self.criar_botoes()
        self.adicionar_botoes()
        
        self.criar_tabelas()
        self.adicionar_tabelas()
        
        self.root.mainloop()
    
    def criar_frames_da_tela(self):
        
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(
            bg = cor_fundo
        )
        
        self.frame_botoes = Frame(self.frame_1)
        self.frame_botoes.configure(
            bg = cor_fundo
        )
        
        self.frame_tabela_doc = Frame(self.frame_1)
        self.frame_tabela_doc.configure(
            bg = cor_fundo
        )
        
        self.frame_tabela_tre = Frame(self.frame_1)
        self.frame_tabela_tre.configure(
            bg = cor_fundo
        )
        
        self.frame_tabela_par = Frame(self.frame_1)
        self.frame_tabela_par.configure(
            bg = cor_fundo
        )
    
    def adicionar_frames_da_tela(self):
        
        self.frame_1.place(relx=0.0000,rely=0.15,relwidth=1,relheight=0.85)
        self.lista_widgets.append(self.frame_1)
        
        self.frame_botoes.place(relx=0.01,rely=0.01,relwidth=0.26,relheight=0.98)
        self.lista_widgets.append(self.frame_botoes)
        
        self.frame_tabela_doc.place(relx=0.28,rely=0.01,relwidth=0.70,relheight=0.315)
        self.lista_widgets.append(self.frame_tabela_doc)
        
        self.frame_tabela_tre.place(relx=0.28,rely=0.34,relwidth=0.70,relheight=0.315)
        self.lista_widgets.append(self.frame_tabela_tre)
        
        self.frame_tabela_par.place(relx=0.28,rely=0.67,relwidth=0.70,relheight=0.315)
        self.lista_widgets.append(self.frame_tabela_par)
        
    def criar_botoes(self):
        
        self.frame_acima = Frame(self.frame_botoes)
        self.frame_acima.configure(
            bg = cor_fundo
        )
        
        self.atualizar = Botao_Imagem(self.frame_acima,'','atualizar.png',width=30)
        self.atualizar.configure(
            command=self.atualiza_listas,
            bg=cor_fundo
        )
        
        self.testar_conec = Botao_Imagem(self.frame_acima,'','conexao.png',width=30)
        self.testar_conec.configure(
            command=BD.Testar_Conexao,
            bg=cor_fundo
        )
        
        self.Novo_AGR = Botao_Imagem(self.frame_botoes,'Novo AGR','novo-agr.png')
        self.Novo_AGR.configure(

        )

        self.Todos_AGRs = Botao_Imagem(self.frame_botoes,'Visualizar AGRs','agrs.png')
        self.Todos_AGRs.configure(

        )

        self.Infos_Gerais = Botao_Imagem(self.frame_botoes,'Informações Gerais','infos_gerais.png')
        self.Infos_Gerais.configure(

        )

        self.Sol_Par = Botao_Imagem(self.frame_botoes,'Solicitar Parametrização','maquina+.png')
        self.Sol_Par.configure(

        )

        self.Sol_Tre = Botao_Imagem(self.frame_botoes,'Solicitar Treinamento','treino+.png')
        self.Sol_Tre.configure(

        )

        self.Vis_Maquinas = Botao_Imagem(self.frame_botoes,'Visualizar Máquinas','maquina.png')
        self.Vis_Maquinas.configure(

        )

        self.Gerenciamento = Botao_Imagem(self.frame_botoes,'Gerenciamento','gerenciamento.png')
        self.Gerenciamento.configure(

        )

    def adicionar_botoes(self):
        
        self.frame_acima.pack(side=TOP,fill=X,pady=10)
        self.lista_widgets.append(self.frame_acima)
        
        self.atualizar.pack(side=LEFT,pady=10,padx=25)
        self.lista_widgets.append(self.atualizar)
        
        self.testar_conec.pack(side=RIGHT,pady=10,padx=25)
        self.lista_widgets.append(self.testar_conec)
        
        self.Novo_AGR.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Novo_AGR)
        
        self.Todos_AGRs.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Todos_AGRs)
        
        self.Infos_Gerais.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Infos_Gerais)
        
        self.Sol_Par.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Sol_Par)
        
        self.Sol_Tre.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Sol_Tre)
        
        self.Vis_Maquinas.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Vis_Maquinas)
        
        self.Gerenciamento.pack(side=TOP,anchor='center',pady=16,fill=X)
        self.lista_widgets.append(self.Gerenciamento)
    
    def criar_tabelas(self):
        
        ################ PENDENCIA DE DOCUMENTOS
        self.nome_pend_doc = Label(self.frame_tabela_doc)
        self.nome_pend_doc.configure(
            text='Pendentes de Documentação',
            fg = cor_fonte_contraste_fundo,
            bg = cor_contraste_fundo,
            font = fonte_Mediana_14
        )
        
        COLUNAS_doc = ['AGR','NOME','CIDADE','TELEFONE']
        self.tabela_doc = Tabela(self.frame_tabela_doc,COLUNAS_doc,10,100,100)
        
        ################ PENDENCIA DE TREINAMENTOS
        self.nome_pend_tre = Label(self.frame_tabela_tre)
        self.nome_pend_tre.configure(
            text='Pendentes de Treinamento',
            fg = cor_fonte_contraste_fundo,
            bg = cor_contraste_fundo,
            font = fonte_Mediana_14
        )
        
        
        COLUNAS_tre = ['ID','AGR','NOME','CIDADE','TELEFONE','AC','SISTEMA']
        self.tabela_tre = Tabela(self.frame_tabela_tre,COLUNAS_tre,10,100,100)
        
        ################ PENDENCIA DE PARAMETRIAZCAO
        self.nome_pend_par = Label(self.frame_tabela_par)
        self.nome_pend_par.configure(
            text='Pendentes de Parametrização',
            fg = cor_fonte_contraste_fundo,
            bg = cor_contraste_fundo,
            font = fonte_Mediana_14
        )
        
        COLUNAS_par = ['ID','AGR','NOME','CIDADE','TELEFONE']
        self.tabela_par = Tabela(self.frame_tabela_par,COLUNAS_par,10,100,100)
    
        self.atualiza_listas()
        
    def atualiza_listas(self):
        
        self.tabela_doc.atualizar_itens()
        self.lista_pen_doc = BD.Mostrar_Pendentes_Documentacao()
        self.tabela_doc.Inserir(self.lista_pen_doc)
        
        self.tabela_tre.atualizar_itens()
        self.lista_pen_tre = BD.Mostrar_Pendentes_Treinamento()
        self.tabela_tre.Inserir(self.lista_pen_tre)
        
        self.tabela_par.atualizar_itens()
        self.lista_pen_par = BD.Mostrar_Pendentes_Parametrizacao()
        self.tabela_par.Inserir(self.lista_pen_par)
        
    def adicionar_tabelas(self):
        self.nome_pend_doc.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.nome_pend_doc)
        
        self.tabela_doc.Barra_Y.pack(side=RIGHT,fill=Y)
        self.tabela_doc.Listagem.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.tabela_doc)

        self.nome_pend_tre.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.nome_pend_tre)
       
        self.tabela_tre.Barra_Y.pack(side=RIGHT,fill=Y)
        self.tabela_tre.Listagem.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.tabela_tre)
        
        self.nome_pend_par.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.nome_pend_par)
        
        self.tabela_par.Barra_Y.pack(side=RIGHT,fill=Y)
        self.tabela_par.Listagem.pack(side=TOP,anchor='center',fill=X)
        self.lista_widgets.append(self.tabela_par)
        
        
root = Tk()
tela_Inicio(root)
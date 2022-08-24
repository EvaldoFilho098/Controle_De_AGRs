from Telas import *
from Fontes import * 
from Widgets import *
from Imagem import *

class JanelaInicio(Tela):
    
    def __init__(self, master):
        super().__init__(master,"comum")
        
        self.cabecalho_padrao("Controle de AGRs","Evaldo")
        
        self.frames_da_tela()
        self.inserir_botoes()
        self.inserir_tabela_1()
        self.inserir_tabela_2()
        self.inserir_tabela_3()
        
        self.root.mainloop()
    
    def frames_da_tela(self):
        
        self.frame_1 = Frame(self.root)
        self.frame_1.configure(
            bg = cor_fundo
        )
        self.frame_1.place(relx=0.0000,rely=0.15,relwidth=1,relheight=0.85)
        
        self.frame_botoes = Frame(self.frame_1)
        self.frame_botoes.configure(
            bg = cor_fundo
        )
        self.frame_botoes.place(relx=0.01,rely=0.01,relwidth=0.3,relheight=0.98)
        
        self.frame_tabela1 = Frame(self.frame_1)
        self.frame_tabela1.configure(
            bg = cor_fundo
        )
        self.frame_tabela1.place(relx=0.28,rely=0.01,relwidth=0.70,relheight=0.315)
        
        self.frame_tabela2 = Frame(self.frame_1)
        self.frame_tabela2.configure(
            bg = cor_fundo
        )
        self.frame_tabela2.place(relx=0.28,rely=0.34,relwidth=0.70,relheight=0.315)
        
        self.frame_tabela3 = Frame(self.frame_1)
        self.frame_tabela3.configure(
            bg = cor_fundo
        )
        self.frame_tabela3.place(relx=0.28,rely=0.67,relwidth=0.70,relheight=0.315)
    
    def inserir_botoes(self):
        
        self.frame_acima = Frame(self.frame_botoes)
        self.frame_acima.configure(
            bg = cor_fundo
        )
        self.frame_acima.pack(side=TOP,fill=X,pady=10)
        
        self.atualizar = Botao_Imagem(self.frame_acima,'','atualizar.png',width=30)
        self.atualizar.pack(side=LEFT,anchor='w',pady=10,padx=50)
        
        self.testar_conec = Botao_Imagem(self.frame_acima,'','conexao.png',width=30)
        self.testar_conec.pack(side=LEFT,anchor='w',pady=10,padx=50)
        
        self.Novo_AGR = Botao_Imagem(self.frame_botoes,'Novo AGR','novo-agr.png')
        self.Novo_AGR.pack(side=TOP,anchor='w',pady=10)
        
        self.Todos_AGRs = Botao_Imagem(self.frame_botoes,'Visualizar AGRs','agrs.png')
        self.Todos_AGRs.pack(side=TOP,anchor='w',pady=10)

        self.Infos_Gerais = Botao_Imagem(self.frame_botoes,'Informações Gerais','infos_gerais.png')
        self.Infos_Gerais.pack(side=TOP,anchor='w',pady=10)

        self.Sol_Par = Botao_Imagem(self.frame_botoes,'Solicitar Parametrização','maquina+.png')
        self.Sol_Par.pack(side=TOP,anchor='w',pady=10)

        self.Sol_Tre = Botao_Imagem(self.frame_botoes,'Solicitar Treinamento','treino+.png')
        self.Sol_Tre.pack(side=TOP,anchor='w',pady=10)

        self.Vis_Maquinas = Botao_Imagem(self.frame_botoes,'Visualizar Máquinas','maquina.png')
        self.Vis_Maquinas.pack(side=TOP,anchor='w',pady=10)

        self.Gerenciamento = Botao_Imagem(self.frame_botoes,'Gerenciamento','gerenciamento.png')
        self.Gerenciamento.pack(side=TOP,anchor='w',pady=10)

    def inserir_tabela_1(self):
        
        self.nome_pend_doc = Label(self.frame_tabela1)
        self.nome_pend_doc.configure(
            text='Pendentes de Documentação',
            fg = cor_fontes_escuras,
            bg = cor_laranja,
            font = fonte_Mediana_14
        )
        self.nome_pend_doc.pack(side=TOP,anchor='center',fill=X)
        
        COLUNAS1 = ['ID','NOME','CIDADE','UF','STATUS','TELEFONE']
        self.tabela1 = Tabela(self.frame_tabela1,COLUNAS1,10,100,100)
        self.tabela1.Listagem.pack(side=TOP,anchor='center',fill=X)
        
    def inserir_tabela_2(self):
        
        self.nome_pend_doc = Label(self.frame_tabela2)
        self.nome_pend_doc.configure(
            text='Pendentes de Parametrização',
            fg = cor_fontes_escuras,
            bg = cor_laranja,
            font = fonte_Mediana_14
        )
        self.nome_pend_doc.pack(side=TOP,anchor='center',fill=X)
        
        COLUNAS2 = ['ID','NOME','CIDADE','UF','STATUS','TELEFONE']
        self.tabela2 = Tabela(self.frame_tabela2,COLUNAS2,10,100,100)
        self.tabela2.Listagem.pack(side=TOP,anchor='center',fill=X)
        
    def inserir_tabela_3(self):
        
        self.nome_pend_doc = Label(self.frame_tabela3)
        self.nome_pend_doc.configure(
            text='Pendentes de Treinamento',
            fg = cor_fontes_escuras,
            bg = cor_laranja,
            font = fonte_Mediana_14
        )
        self.nome_pend_doc.pack(side=TOP,anchor='center',fill=X)
        
        COLUNAS3 = ['ID','NOME','CIDADE','UF','STATUS','TELEFONE']
        self.tabela3 = Tabela(self.frame_tabela3,COLUNAS3,10,100,100)
        self.tabela3.Listagem.pack(side=TOP,anchor='center',fill=X)
        
        
root = Tk()
JanelaInicio(root)
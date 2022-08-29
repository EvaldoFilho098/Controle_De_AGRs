from doctest import master
from Telas import *
from Fontes import *
from Widgets import *
from Imagem import *
import Banco_De_Dados as BD
from ibge.localidades import Estados, MunicipioPorUF


class tela_CadastroAGR(Tela):

    def __init__(self, master):
        super().__init__(master, "cadastro")

        self.criar_campos_infos()
        self.adicionar_campos_infos()

        self.root.mainloop()

    def cidades(self,event):
        
        self.resultado_content = self.uf.Lista.get()
        
        if self.resultado_content != '':
            dic_estados = self.estados.json()

            for info in dic_estados:
                if info['sigla'] == self.resultado_content:
                    id_estado_selecionado = info['id']
            
            municipios = MunicipioPorUF(id_estado_selecionado)

            self.lista_municipios = municipios.getNome()
            self.lista_municipios.sort()
            
            self.cidade.Lista.set_completion_list(self.lista_municipios)
            self.cidade.Lista.update()
            
        else:
            self.lista_municipios = []
            
    def criar_campos_infos(self):
        
        self.estados = Estados()
        self.lista_estados = self.estados.getSigla()

        self.resultado_content = StringVar()
        
        self.lista_municipios = []
        
        self.varTerm = BooleanVar()
        self.varTerm.set(False)
        
        self.frame_infos = Frame(self.root)
        self.frame_infos.configure( bg=cor_fundo, highlightbackground=cor_frames, highlightthickness=2)
        
        self.titulo_infos = Texto_Imagem(self.frame_infos,'Novo AGR','agrs.png',font=fonte_Destaques_24)
        self.nome = Texto_Entrada(self.frame_infos,'Nome: ')
        self.cpf = Texto_Entrada(self.frame_infos,'CPF: ')
        self.email = Texto_Entrada(self.frame_infos,'E-mail: ')
        self.telefone = Texto_Entrada(self.frame_infos,'Telefone: ',show='*')
        self.uf = Texto_Seleciona(self.frame_infos,'UF: ',self.lista_estados)
        self.cidade = Texto_Seleciona(self.frame_infos,'Cidade: ',self.lista_municipios)
        self.cidade.Lista.bind("<Button-1>", self.cidades)
        self.espaco = Texto(self.frame_infos,'',font=fonte_Mediana_14)
        self.termo = Botao_Check(self.frame_infos,'Possui Termo de Responsabilidade',self.varTerm,font=fonte_Textos_12,width=400)
        self.botao = Botao(self.frame_infos,'Próximo')
        self.botao.config(
            command=self.criar_campos_doc
        )
        
    def adicionar_campos_infos(self):
        
        self.frame_infos.place(x=0,y=0,width=400,height=600)
        self.lista_widgets.append(self.frame_infos)
        
        self.titulo_infos.Frame.pack(side=TOP,pady=30,anchor='center')
        self.lista_widgets.append(self.titulo_infos)
        
        self.nome.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.nome)
        
        self.email.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.email)
        
        self.cpf.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.cpf)
        
        self.telefone.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.telefone)
        
        self.uf.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.uf)
        
        self.cidade.Frame.pack(side=TOP,pady=20,anchor='center')
        self.lista_widgets.append(self.cidade)
        
        self.botao.pack(side=BOTTOM,pady=20,anchor='center')
        self.lista_widgets.append(self.botao)

    def criar_campos_doc(self):
        
        self.botao.forget()
        self.root.geometry("800x" + self.height)
        
        self.frame_doc = Frame(self.root)
        self.frame_doc.configure( bg=cor_fundo, highlightbackground=cor_frames, highlightthickness=2)
        
        self.titulo_doc = Texto_Imagem(self.frame_doc,'Documentação','docs.png',font=fonte_Destaques_24)
        
        self.var_selecionar_todos_docs = BooleanVar()
        self.var_selecionar_todos_docs.set(False)
        self.selTodos = Botao_Check(self.frame_doc,'Documentação Completa',self.var_selecionar_todos_docs,font=fonte_Textos_12,width=400)
        self.selTodos.bind("<Button-1>", self.selecionar_todos_docs)
        
        self.varCPF = BooleanVar()
        self.varCPF.set(False)
        self.CPF = Botao_Check(self.frame_doc,'Cópia CPF',self.varCPF,font=fonte_Textos_12,width=400)
        
        self.varRG = BooleanVar()
        self.varRG.set(False)
        self.RG = Botao_Check(self.frame_doc,'Cópia RG',self.varRG,font=fonte_Textos_12,width=400)
        
        self.varCTPS = BooleanVar()
        self.varCTPS.set(False)
        self.CTPS = Botao_Check(self.frame_doc,'Cópia CTPS',self.varCTPS,font=fonte_Textos_12,width=400)
        
        self.varTitulo = BooleanVar()
        self.varTitulo.set(False)
        self.Titulo = Botao_Check(self.frame_doc,'Cópia Título',self.varTitulo,font=fonte_Textos_12,width=400)
        
        self.varEscolaridade = BooleanVar()
        self.varEscolaridade.set(False)
        self.Escolaridade = Botao_Check(self.frame_doc,'Escolaridade',self.varEscolaridade,font=fonte_Textos_12,width=400)
        
        self.varCurriculo = BooleanVar()
        self.varCurriculo.set(False)
        self.Curriculo = Botao_Check(self.frame_doc,'Currículo',self.varCurriculo,font=fonte_Textos_12,width=400)
        
        self.varDeclEnd = BooleanVar()
        self.varDeclEnd.set(False)
        self.DeclEnd = Botao_Check(self.frame_doc,'Declaração de Endereço',self.varDeclEnd,font=fonte_Textos_12,width=400)
        
        self.varRotEntr = BooleanVar()
        self.varRotEntr.set(False)
        self.RotEntr = Botao_Check(self.frame_doc,'Roteiro da Entrevista',self.varRotEntr,font=fonte_Textos_12,width=400)
        
        self.varCursoAGR = BooleanVar()
        self.varCursoAGR.set(False)
        self.CursoAGR = Botao_Check(self.frame_doc,'Certificado do Curso de AGR ',self.varCursoAGR,font=fonte_Textos_12,width=400)
        
        self.varCertificado = BooleanVar()
        self.varCertificado.set(False)
        self.Certificado = Botao_Check(self.frame_doc,'Certificado Digital A3',self.varCertificado,font=fonte_Textos_12,width=400)
        
        self.varCER = BooleanVar()
        self.varCER.set(False)
        self.CER = Botao_Check(self.frame_doc,'Arquivo .CER',self.varCER,font=fonte_Textos_12,width=400)
        
        self.varCadastroSistema = BooleanVar()
        self.varCadastroSistema.set(False)
        self.CadastroSistema = Botao_Check(self.frame_doc,'Cadastro no Site de Compras',self.varCadastroSistema,font=fonte_Textos_12,width=400)
        
        self.botao = Botao(self.frame_doc,'Próximo')
        self.botao.configure(
            command=self.criar_campos_finais
        )
        
        self.adicionar_campos_doc()

    def selecionar_todos_docs(self,event):
        
        if self.var_selecionar_todos_docs.get() == False:
            
            self.CPF.select()
            self.CPF.update()
            self.varCPF.set(True)

            self.RG.select()
            self.RG.update()
            self.varRG.set(True)

            self.CTPS.select()
            self.CTPS.update()
            self.varCTPS.set(True)

            self.Titulo.select()
            self.Titulo.update()
            self.varTitulo.set(True)

            self.Escolaridade.select()
            self.Escolaridade.update()
            self.varEscolaridade.set(True)

            self.Curriculo.select()
            self.Curriculo.update()
            self.varCurriculo.set(True)

            self.DeclEnd.select()
            self.DeclEnd.update()
            self.varDeclEnd.set(True)

            self.RotEntr.select()
            self.RotEntr.update()
            self.varRotEntr.set(True)

            self.CursoAGR.select()
            self.CursoAGR.update()
            self.varCursoAGR.set(True)

            self.Certificado.select()
            self.Certificado.update()
            self.varCertificado.set(True)

            self.CER.select()
            self.CER.update()
            self.varCER.set(True)

            self.CadastroSistema.select()
            self.CadastroSistema.update()
            self.varCadastroSistema.set(True)
        
        else:
            
            self.CPF.deselect()
            self.CPF.update()
            self.varCPF.set(False)

            self.RG.deselect()
            self.RG.update()
            self.varRG.set(False)

            self.CTPS.deselect()
            self.CTPS.update()
            self.varCTPS.set(False)

            self.Titulo.deselect()
            self.Titulo.update()
            self.varTitulo.set(False)

            self.Escolaridade.deselect()
            self.Escolaridade.update()
            self.varEscolaridade.set(False)

            self.Curriculo.deselect()
            self.Curriculo.update()
            self.varCurriculo.set(False)

            self.DeclEnd.deselect()
            self.DeclEnd.update()
            self.varDeclEnd.set(False)

            self.RotEntr.deselect()
            self.RotEntr.update()
            self.varRotEntr.set(False)

            self.CursoAGR.deselect()
            self.CursoAGR.update()
            self.varCursoAGR.set(False)

            self.Certificado.deselect()
            self.Certificado.update()
            self.varCertificado.set(False)

            self.CER.deselect()
            self.CER.update()
            self.varCER.set(False)

            self.CadastroSistema.deselect()
            self.CadastroSistema.update()
            self.varCadastroSistema.set(False)
            
    def adicionar_campos_doc(self):
        
        self.frame_doc.place(x=400,y=0,width=400,height=600)
        self.lista_widgets.append(self.frame_doc)
        
        self.titulo_doc.Frame.pack(side=TOP,anchor='center',pady=30)
        self.lista_widgets.append(self.titulo_doc)
        
        self.selTodos.pack(side=TOP,anchor='w',padx=20,pady=10)
        self.lista_widgets.append(self.selTodos)
        
        self.CPF.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.CPF)

        self.RG.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.RG)

        self.CTPS.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.CTPS)

        self.Titulo.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Titulo)

        self.Escolaridade.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Escolaridade)

        self.Curriculo.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Curriculo)

        self.DeclEnd.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.DeclEnd)

        self.RotEntr.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.RotEntr)

        self.CursoAGR.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.CursoAGR)

        self.Certificado.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Certificado)

        self.CER.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.CER)

        self.CadastroSistema.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.CadastroSistema)
        
        self.botao.pack(side=BOTTOM,pady=20,anchor='center')
        self.lista_widgets.append(self.botao)

    def criar_campos_finais(self):
        
        self.root.geometry("1200x" + self.height)
        
        ################# PARAMETRIZACAO
        self.frame_1 = Frame(self.root)
        self.frame_1.configure( bg=cor_fundo, highlightbackground=cor_frames, highlightthickness=2)
        
        self.titulo_par = Texto_Imagem(self.frame_1,'Parametrização','maquina+.png',font=fonte_Destaques_24)
        
        self.varSolPar = BooleanVar()
        self.varSolPar.set(False)
        self.SolPar = Botao_Check(self.frame_1,'Requisitar Parametrização',self.varSolPar)
        
        ################# TREINAMENTOS
        self.frame_2 = Frame(self.root)
        self.frame_2.configure( bg=cor_fundo, highlightbackground=cor_frames, highlightthickness=2)
        
        self.titulo_trei = Texto_Imagem(self.frame_2,'Treinamentos','treino+.png',font=fonte_Destaques_24)
        
        self.lista_acs = ['AC META','AC SOLUTI','AC DIGITAL']
        self.Selecionar_AC = Texto_Seleciona(self.frame_2,'Selecione a AC:',self.lista_acs,width=100)
        
        self.varSiteCompras = BooleanVar()
        self.varSiteCompras.set(False)
        self.SiteCompras = Botao_Check(self.frame_2,'Site de Compras',self.varSiteCompras)
        
        self.varPresencial = BooleanVar()
        self.varPresencial.set(False)
        self.Presencial = Botao_Check(self.frame_2,'Atendimento Presencial',self.varPresencial)
        
        self.varVideo = BooleanVar()
        self.varVideo.set(False)
        self.Video = Botao_Check(self.frame_2,'Atendimento VideoConferência',self.varVideo)
        
        self.varTodosTrein = BooleanVar()
        self.varTodosTrein.set(False)
        self.TodosTrein = Botao_Check(self.frame_2,'Treinamento Completo',self.varTodosTrein)
        self.TodosTrein.bind("<Button-1>", self.selecionar_todos_trein)
        
        self.adicionar_campos_finais()
        
    def adicionar_campos_finais(self):
        
        ################# PARAMETRIZACAO
        self.frame_1.place(x=800,y=0,width=400,height=200)
        self.lista_widgets.append(self.frame_1)
        
        self.titulo_par.Frame.pack(side=TOP,anchor='center',pady=30)
        self.lista_widgets.append(self.titulo_par)
        
        self.SolPar.pack(side=TOP,anchor='w',padx=20,pady=10)
        self.lista_widgets.append(self.SolPar)
        
        ################# TREINAMENTOS
        self.frame_2.place(x=800,y=199,width=400,height=400)
        self.lista_widgets.append(self.frame_2)
        
        self.titulo_trei.Frame.pack(side=TOP,anchor='center',pady=30)
        self.lista_widgets.append(self.titulo_trei)
        
        self.Selecionar_AC.Frame.pack(side=TOP,anchor='w',padx=20,pady=15,fill=X)
        self.lista_widgets.append(self.Selecionar_AC)

        self.SiteCompras.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.SiteCompras)

        self.Presencial.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Presencial)

        self.Video.pack(side=TOP,anchor='w',padx=20)
        self.lista_widgets.append(self.Video)

        self.TodosTrein.pack(side=TOP,anchor='w',padx=20,pady=18)
        self.lista_widgets.append(self.TodosTrein)

        self.botao.configure(
            command=self.concluir,
            text='Concluir'
        )
        self.botao.update()
        
    def selecionar_todos_trein(self,event):
        if self.varTodosTrein.get() == False:
            
            self.SiteCompras.select()
            self.SiteCompras.update()
            self.varSiteCompras.set(True)

            self.Presencial.select()
            self.Presencial.update()
            self.varPresencial.set(True)

            self.Video.select()
            self.Video.update()
            self.varVideo.set(True)
        
        else:
            
            self.SiteCompras.deselect()
            self.SiteCompras.update()
            self.varSiteCompras.set(False)

            self.Presencial.deselect()
            self.Presencial.update()
            self.varPresencial.set(False)

            self.Video.deselect()
            self.Video.update()
            self.varVideo.set(False)
            
    def concluir(self):
        pass
        
root = Tk()
tela_CadastroAGR(root)

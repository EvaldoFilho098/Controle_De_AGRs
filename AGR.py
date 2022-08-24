import Banco_De_Dados as BD

class AGR:
    def __init__(self, id_agr):
        self.ID_agr = id_agr
        
        #id_agr,nome_agr,cpf_agr,status_agrs,telefone_agr,e_mail_agr,cidade_agr,uf_agr,termo_responsabilidade_agr
        #id,nome,cpf,status,telefone,email,cidade,uf,termo
        
        self.Infos = BD.Selecionar_Filtros('agrs','*',{'id_agr':self.ID_agr})
        self.Nome = self.Infos[0][1]
        self.CPF = self.Infos[0][2]
        self.Status = self.Infos[0][3]
        self.Telefone = self.Infos[0][4]
        self.Email = self.Infos[0][5]
        self.Cidade = self.Infos[0][6]
        self.UF = self.Infos[0][7]
        self.Termo = self.Infos[0][8]
        
        
        
        #maquinas associadas a ele
        BD.Maquinas_do_AGR(self.ID_agr)
        
        #maquinas assinadas por ele
        BD.AGR_Assinou(self.ID_agr)
        
        #treinamentos recebidos
        BD.Buscar_Treinamentos_Recebidos(self.ID_agr)
        
        #parametrizações em suas máquinas
        BD.Buscar_Parametrizacoes_Recebidas()
        
        #possibilidade de deletar
        BD.Deletar_AGR(self.ID_agr)
        
        #visualizar a situação em cada AC
        BD.Situacoes_ACs(self.ID_agr)
        
        #visualizar sua Tabela de Preços
        BD.Selecionar_Coluna_Unica('*','tabela_precos','id_agr',self.ID_agr) # -------------- ver nome da tabela e atributo
        
        #visualizar documentos
        BD.Selecionar_Coluna_Unica('*','documentos','id_agr',self.ID_agr) # -------------- ver nome da tabela e atributo
        
        #alterar situação em AC
        BD.Alterar('acs','','','id_agr',self.ID_agr) # -------------- ver nome da tabela e atributo
        
        #alterar tabela de precos
        BD.Alterar('tabela_precos','','','id_agr',self.ID_agr) # -------------- ver nome da tabela e atributo
        
        #alterar qualquer informaçao do AGR
        BD.Alterar('agrs','','','id_agr',self.ID_agr) # -------------- ver nome da tabela e atributo
        
        #Assinar termo de alguma máquina ****
        BD.Assinar_Termo_Doacao()
        
        
    def mostrar(self):
        print(self.Infos)
        

x = AGR(17)
x.mostrar()
"""
BANCO DE DADOS DO PROGRAMA
"""
from datetime import datetime
from turtle import Terminator
import mysql.connector

    
def Conectar(host='192.168.99.254',usuario='Evaldo',senha='@meta123!',database='controle_agrs'):
    """Conectar
    Criar conexão com o Banco de Dados instanciado

    Args:
        host (str, optional): IP onde estará hospedado o Banco de Dados. Defaults to '192.168.99.254';
        usuario (str, optional): Usuário para uso do Banco de Dados. Defaults to 'Evaldo';
        senha (str, optional): Senha para autenticação do Usuário. Defaults to '@meta123!';
        bd (str, optional): Nome do Banco de Dados hospedado. Defaults to 'BD';
        
    Returns:
        Tupla: (conn,cursor)
                | conn -> Conexão estabelecida;
                | cursor -> cursor para executar comandos SQL;
    """
    conn = mysql.connector.connect(
        host=host,
        user=usuario,
        password=senha,
        database=database
    )
    cursor = conn.cursor()
    return conn,cursor

################### INSERT #########################
def Inserir_Documentacao(id_agr):
    """Inserir a Documentação Padrão
    Todos Os Itens iniciarão Como "PENDENTE"

    Args:
        id_agr (int): ID do AGR correspondente
    """
    conn,cursor = Conectar()
    
    comando = "INSERT INTO documentacao (fk_id_agr_doc) \
        VALUES ({})".format(id_agr)
    
    cursor.execute(comando)
    
    conn.commit()
    conn.close()   

def Inserir_Tabela_Precos(id_agr):
    """Insere Nova Tabela de Precos no Banco de dados
    Todos Os Itens iniciarão com 0
    
    Args:
        id_agr (int): ID do AGR correspondente
    """
    
    conn,cursor = Conectar()
    
    comando = "INSERT INTO tabela_precos (fk_id_agr_tp)\
        VALUES ({})".format(id_agr)
    
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

def Inserir_ACs(id_agr):
    """Inserir a Situação das ACs
    Todos Os Itens iniciarão Como "INATIVO"

    Args:
        id_agr (int): ID do AGR Correspondente
    """
    conn,cursor = Conectar()
    
    comando = "INSERT INTO acs (fk_id_agr_ac)\
        VALUES ({})".format(id_agr)
    
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

def Inserir_AGR(nome,cpf,email,telefone,termo,status='PENDENTE'):
    """Inserir novo AGR no Banco de Dados

    Args:
        nome (String): Nome completo do AGR;
        cpf (String): Número de CPF do AGR, com formatação;
        email (String): E-mail do AGR;
        telefone (String): Telefone do AGR, com formatação;
        termo (String): Confimação ou Negação sobre o AGR possuir termo de responsabilidade;
        status (str, optional): Status do AGR, inicialmente marcado como "PENDENTE";

    Returns:
        int: Retorna a ID do AGR inserido;
    """
    conn,cursor = Conectar()
    
    comando = "INSERT INTO agrs ( nome_agr, cpf_agr, e_mail_agr, telefone_agr, termo_responsabilidade_agr, status_agr ) \
    VALUES ('{}','{}','{}','{}','{}','{}')".format(nome,cpf,email,telefone,termo,status)
    
    cursor.execute(comando)
    id_agr = cursor.lastrowid
    
    conn.commit()
    conn.close()
    
    Inserir_Documentacao(id_agr)
    Inserir_Tabela_Precos(id_agr)
    Inserir_ACs(id_agr)
    
    return id_agr

def Nova_Maquina(nome_maquina,termo_doacao='',bitlocker=''):
    """Adiciona uma Nova máquina no Banco de Dados

    Args:
        nome_maquina (str): Nome da máquina ;
        termo_doacao (str, optional): Arquivo do Termo de Doação. Defaults to '';
        bitlocker (str, optional): Arquivo de Bitlocker. Defaults to '';
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO maquinas (nome_maquina, termo_doacao_maquina, bitlocker_maquina)\
        VALUES ('{}','{}','{}')".format(nome_maquina,termo_doacao,bitlocker)
    cursor.execute(comando)
    conn.commit()
    conn.close()

def Atribuir_Maquina_AGR(id_agr,id_maquina):
    """Atribui Determinada Máquina a um AGR

    Args:
        id_agr (int): ID do AGR em questão;
        id_maquina (int): ID da Máquina em questão;
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO agrs_possui_maquinas (fk_id_agr,fk_id_maquina)\
        VALUES ('{}','{}')".format(id_agr,id_maquina)
    cursor.execute(comando)
    conn.commit()
    conn.close()

def Assinar_Termo_Doacao(id_agr,id_maquina,termo_doacao=''):
    """Vincular um termo de doação assinado por um AGR à uma máquina

    Args:
        id_agr (int): ID do AGR em questão;
        id_maquina (int): ID da Máquina em questão;
        termo_doacao (str, optional): Arquivo do termo de doação. Defaults to '';
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO agrs_assina_termos_doacao (fk_id_agr,fk_id_maquina,documento_termo_doacao)\
        VALUES ('{}','{}','{}')".format(id_agr,id_maquina,termo_doacao)
    cursor.execute(comando)
    conn.commit()
    conn.close()

#REVISAR
def Parametrizacao(id_agr,id_maquina,id_funcionario,data,situacao,observacao=''):
    """Adiciona nova Parametrização ao Banco de Dados
    A parametrização é feita em determinado dia, por determinado funcionario para uma máquina vinculada à um AGR
    Args:
        id_agr (int): ID do AGR em questão;
        id_maquina (int): ID da máquina em questão;
        id_funcionario (int): ID do funcionário que realizou a parametrização;
        data (str): Data em que foi realizada a Parametrização;
        situacao (str): Situação em que se encontra a Parametrização (Realizada,Desfeita);
        observacao (str,opicional): Qualquer observação feita pelo funcionario ao realizar a Parametrização. Padrão definid como vazio;
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO parametrizacoes (fk_id_agr,fk_id_maquina,fk_id_funcionario,data_parametrizacao,status_parametrizacao,_observacoes_parametrizacao)\
        VALUES ('{}','{}','{}','{}','{}','{}')".format(id_agr,id_maquina,id_funcionario,data,situacao,observacao)
    cursor.execute(comando)
    conn.commit()
    conn.close()

def Treinar(id_agr,id_funcionario,data_treinamento,ac_treinamento,sistema_treinamento):
    """Adicionar novo Treinamento ao Banco de Dados.
    Todo treinamento é feito por um Funcionário, para um AGR

    Args:
        id_agr (int): ID do AGR a ser treinado;
        id_funcionario (int): ID do funcionario Treinador;
        data_treinamento (str): Data em que foi realizado o Treinamento;
        ac_treinamento (str): AC que fornece o sistema;
        sistema_treinamento (str): Qual sistema foi ensinado;
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO treinamentos (fk_id_agr,fk_id_funcionario,data_treinamento,ac_treinamento,sistema_treinamento)\
        VALUES ('{}','{}','{}','{}','{}')".format(id_agr,id_funcionario,data_treinamento,ac_treinamento,sistema_treinamento)
    cursor.execute(comando)
    conn.commit()
    conn.close()

def Inserir_Funcionario(nome,login,senha,email,cargo,privilegio):
    """Inserir novo Funcionario que poderá utilizar o sistema

    Args:
        nome (str): Nome completo do funcionário;
        login (str): Login do funcionario;
        senha (str): Senha do funcionario;
        email (str): Email do funcionario;
        cargo (str): Cargo que o funcionario executa, o que possibilitará determinado tipo de funções dentro do sistema;
        privilegio (str): Privilegio Administrador ou Funcionario, o que possibilitará determinado tipo de ações dentro do sistema;
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO funcionarios (nome_funcionario,login_funcionario,senha_funcionario,email_funcionario,cargo_funcionario,privilegio_funcionario)\
        VALUES ('{}','{}','{}','{}','{}','{}')".format(nome,login,senha,email,cargo,privilegio)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

def Inserir_Acoes(id_funcionario,data_acao,acao):
    """Inserir nova ação realizada por algum funcionário

    Args:
        id_funcionario (int): ID do funcionário que realizou a ação;
        data_acao (str): Data em que a ação foi realizada;
        acao (str): Descrição da ação realizada;
    """
    conn,cursor = Conectar()
    comando = "INSERT INTO acoes (fk_id_funcionario,data_acao,acao)\
        VALUES ('{}','{}','{}')".format(id_funcionario,data_acao,acao)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()
    
    
    
#DELETE FROM `controle_agrs`.`agrs` WHERE (`id_agr` = '3');
#######################################################################

def Situacoes_ACs(id):
    conn,cursor = Conectar()
    comando = "SELECT ACMETA,SOLUTI FROM AGR WHERE ID_AGR = {}".format(id)
    cursor.execute(comando)
    result = cursor.fetchall()
    conn.close()
    
    return result

# lendo os dados
def Select_Where(item = '*',coluna = '',result = '',tabela='AGR'):
    conn,cursor = Conectar()

    #cursor.execute(""" 
    #SELECT '%s' FROM AGR;
    #""" % coluna)
    if str(result) != '':
        comando = "SELECT " + item + " FROM " + tabela + " WHERE " + coluna + "='" + str(result) + "'"
    else: 
        #cursor.execute("SELECT * FROM AGR ")
        comando = "SELECT * FROM " + tabela
        
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista

def Select_Columns(colunas,tabela='AGR',filtros={}):
    conn,cursor = Conectar()
    comando = "SELECT "
    for coluna in colunas:
        comando += coluna + ","
    
    comando = comando[:len(comando)-1] + " FROM " + tabela
    #print(comando)
    if filtros != {}:
        comando += " WHERE "
    
        for f in filtros.items():
            if f[0] == "NOME":
                comando += "NOME LIKE '%{}%' AND ".format(f[1])
            else: 
                comando += str(f[0]) + " = '" + str(f[1]) + "' AND "
        
        comando = comando[:-5]
        
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista
    
###################################################################
def Select_Distinct(item,tabela='AGR'):
    conn,cursor = Conectar()
    comando = "SELECT DISTINCT " + item + " FROM " + tabela
    
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha[0])

    conn.close()
    return lista

# alterando os dados da tabela
def Alterar(tabela,coluna,novo, id):
    conn,cursor = Conectar()

    comando = "UPDATE " + tabela + " SET " + coluna + "='" + novo + "' WHERE ID_AGR=" + str(id)
    #print(comando)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()

###################################################################

def Deletar_AGR(id):
    conn,cursor = Conectar()
    comando = "DELETE FROM AGR WHERE ID=" + str(id)
    cursor.execute(comando)
    comando = "DELETE FROM DOCUMENTOS WHERE ID_AGR=" + str(id)
    cursor.execute(comando)
    comando = "DELETE FROM PARAMETRIZACAO WHERE ID_AGR=" + str(id)
    cursor.execute(comando)
    comando = "DELETE FROM TREINAMENTOS WHERE ID_AGR=" + str(id)
    cursor.execute(comando)
    conn.commit()
    conn.close()

def Deletar(tabela,coluna,item):
    conn,cursor = Conectar()
    comando = "DELETE FROM" + str(tabela) + "WHERE" + coluna + "=" + str(item)
    conn.commit()
    conn.close()

################################################################

def Contagem(Cnt='',Whr='',tabela='AGR'):
    conn,cursor = Conectar()

    if Cnt == '' and Whr == '':
        comando = "SELECT COUNT(*) FROM " + tabela
    else:
        comando = "SELECT COUNT(*) FROM " + tabela + " WHERE " + Cnt + "='" + Whr + "'"

    cursor.execute(comando)

    x = int(cursor.fetchall()[0][0])

    conn.close()

    return x

def Ultima_ID():
    conn,cursor = Conectar()
    comando = "SELECT * FROM AGR WHERE ID=(SELECT max(ID) FROM AGR)"
    cursor.execute(comando)
    x = str(cursor.fetchall()[0][0])
    conn.close()

    return x

def Autenticacao_ADMIN(login,senha):
    conn,cursor = Conectar()
    comando = "SELECT * FROM FUNCIONARIOS WHERE " 
    comando += "LOGIN_funcionario = '" + login + "' "
    
        
    cursor.execute(comando)
    
    x = cursor.fetchone()
    conn.close()

    
    if x != None:
        if x[4] == 'ADMIN':
            return True
        else: 
            return "Este Usuário Não É Administrador!\n"
    else: 
        return "Login ou Senha Incorreto!\n"
    
def Autenticacao(login,senha,privilegio=''):
    conn,cursor = Conectar()
    comando = "SELECT * FROM FUNCIONARIOS WHERE " 
    comando += "LOGIN_funcionario = '" + login + "' "
    comando += "AND SENHA_funcionario = '" + senha + "' " 
    if privilegio != '':
        comando += "AND PRIVILEGIO_funcionario = '" + privilegio + "'"
        
    cursor.execute(comando)
    
    x = cursor.fetchone()
    conn.close()

    if x != None:
        return (True,x[1],x[4])
    else: 
        return False
    
def Registrar_Acao(acao,usuario):
    """
    FEITO_acao,USUARIO_acao,DATA_acao
    """
    data = datetime.now().strftime("[Realizado Dia %d/%m/%y às %H:%M]")
    conn,cursor = Conectar()
    comando = "INSERT INTO ACOES (FEITO_acao,USUARIO_acao,DATA_acao)\
        VALUES ('{}','{}','{}')".format(acao,usuario,data)
    cursor.execute(comando)
    
    conn.commit()
    conn.close()




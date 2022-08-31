"""
BANCO DE DADOS DO PROGRAMA
"""
from datetime import datetime
from re import A
from turtle import Terminator
from unittest import result
import mysql.connector

from Mensagens import Mensagem_Concluida, Mensagem_Erro

########################### CONEXAO ##################################


def Conectar(host='192.168.99.254', usuario='Evaldo', senha='@meta123!', database='controle_agrs'):
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
    try:
        conn = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=database
        )
        cursor = conn.cursor()
        return conn, cursor
    except:
        Mensagem_Erro(
            "Não Foi Possivel Estabelecer Conexão com o Banco de Dados!!")
        return False, False


def Testar_Conexao(host='192.168.99.254', usuario='Evaldo', senha='@meta123!', database='controle_agrs'):
    """Testar
    Testar conexão com o Banco de Dados instanciado

    Args:
        host (str, optional): IP onde estará hospedado o Banco de Dados. Defaults to '192.168.99.254';
        usuario (str, optional): Usuário para uso do Banco de Dados. Defaults to 'Evaldo';
        senha (str, optional): Senha para autenticação do Usuário. Defaults to '@meta123!';
        bd (str, optional): Nome do Banco de Dados hospedado. Defaults to 'BD';
    """
    try:
        conn = mysql.connector.connect(
            host=host,
            user=usuario,
            password=senha,
            database=database
        )

        if conn:
            Mensagem_Concluida("Banco De Dados Conectado Corretamente!!")
        else:
            Mensagem_Erro(
                "Não Foi Possivel Estabelecer Conexão com o Banco de Dados!!")

    except:
        Mensagem_Erro(
            "Não Foi Possivel Estabelecer Conexão com o Banco de Dados!!")


########################### SELECTS ##################################

def Situacoes_ACs(id_agr):
    """Busca a situação do AGR perante cada AC

    Args:
        id_agr (int): Id do AGR em questão

    Returns:
        (tupla): Tupla com as situações
    """
    conn, cursor = Conectar()
    comando = "SELECT ac_meta,ac_soluti,ac_digital FROM acs WHERE fk_id_agr_ac = '{}' ".format(
        str(id_agr))
    cursor.execute(comando)
    saida = cursor.fetchone()
    conn.close()

    return saida


def Maquinas_do_AGR(id_agr):
    """Busca quais máquinas foram atribuidas a um AGR

    Args:
        id_agr (int): ID do AGR em questão

    Returns:
        (lista): Lista de tuplas com ID e nome das máquinas  respectivamente
    """
    conn, cursor = Conectar()
    comando = "SELECT fk_id_maquina FROM agrs_possui_maquinas WHERE fk_id_agr = '{}' ".format(
        str(id_agr))
    cursor.execute(comando)
    maquinas = cursor.fetchall()

    lista = []
    for s in maquinas:
        comando = "SELECT nome_maquina FROM maquinas WHERE id_maquina = '{}'".format(
            s[0])
        cursor.execute(comando)
        nome = cursor.fetchone()
        lista.append((s[0], nome[0]))

    conn.close()

    return lista


def Maquina_Assinada_Por(id_maquina):
    """Busca os AGRs que assinaram o termo de uma determinada Máquina

    Args:
        id_maquina (int): ID da máquina em questão;

    Returns:
        (lista): Caso exista um termo assinado para a máquina, 
                retornará uma lista que contem uma tupla com o nome e a ID de todos os AGRs que assinaram.
                Caso Não exista, retorna False;
    """
    conn, cursor = Conectar()
    comando = "SELECT fk_id_agr FROM agrs_assina_termos_doacao WHERE fk_id_maquina = '{}' ".format(
        str(id_maquina))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    lista = []
    if resultado:
        for item in resultado:
            id_agr = item[0]
            nome_agr = Selecionar_Coluna_Unica(
                'nome_agr', 'agrs', 'id_agr', id_agr)
            lista.append((id_agr, nome_agr))

    return lista


def Maquina_Usada_Por(id_maquina):
    """Busca os AGRs que usam determinada Máquina

    Args:
        id_maquina (int): ID da máquina em questão;

    Returns:
        (lista): Lista que contem uma tupla com o ID e Nome (respectivamente) de todos os AGRs que usam a máquina.
    """
    conn, cursor = Conectar()
    comando = "SELECT fk_id_agr FROM agrs_possui_maquinas WHERE fk_id_maquina = '{}' ".format(
        str(id_maquina))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    if resultado:
        lista = []
        for item in resultado:
            id_agr = item[0]
            nome_agr = Selecionar_Coluna_Unica(
                'nome_agr', 'agrs', 'id_agr', id_agr)
            lista.append((id_agr, nome_agr))

        return lista
    else:
        return False


def AGR_Assinou(id_agr):
    """Busca todas as Máquinas para as quais o AGR assinou o termo

    Args:
        id_agr (int): ID do AGR em questão

    Returns:
        lista: Caso ele tenha assinado algum termo, retorna uma lista com a ID e o Nome das máquinas.
                Caso não tenha, rertorna False
    """
    conn, cursor = Conectar()
    comando = "SELECT fk_id_maquina FROM agrs_assina_termos_doacao WHERE fk_id_agr = '{}' ".format(
        str(id_agr))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    if resultado:
        lista = []
        for item in resultado:

            id_maquina = item[0]
            nome_maquina = Selecionar_Coluna_Unica(
                'nome_maquina', 'maquinas', 'id_maquina', id_maquina)
            lista.append((id_maquina, nome_maquina))

        return lista
    else:
        return False


def Selecionar_Coluna_Unica(coluna, tabela, coluna_condicao, valor_condicao):
    """Selecionar coluna específica de uma tabela, que satsfaça uma condição
    Exemplo:
    SELECT coluna FROM tabela WHERE coluna_condicao = valor_condicao

    Args:
        coluna (str,int,float): Coluna que deseja selecionar
        tabela (str,int,float): Tabela onde a Coluna está
        coluna_condicao (str,int,float): Coluna que deseja usar como condicao
        valor_condicao (str,int,float): valor condicao que deseja para o atributo condicao

    Returns:
        str: Resultado selecionado, caso exista. Retorna False caso não exista
    """
    conn, cursor = Conectar()

    comando = "SELECT {} FROM {} WHERE {} = '{}'".format(str(coluna), str(tabela), str(coluna_condicao), str(valor_condicao))
    cursor.execute(comando)
    saida = cursor.fetchone()

    conn.close()
    if saida:
        if type(saida) == tuple or type(saida) == list:
            return saida[0]
        else:
            return saida
    else:
        return False


def Selecionar_Tabela_Completa(tabela):
    """Seleciona todas as linhas de uma tabela específica

    Args:
        tabela (str): Nome da Tabela

    Returns:
        lista: Lista com todas as linhas da tabela
    """

    conn, cursor = Conectar()
    comando = "SELECT * FROM {}".format(str(tabela))
    cursor.execute(comando)

    lista = []
    for linha in cursor.fetchall():
        lista.append(linha)

    conn.close()
    return lista


def Selecionar_Filtros(tabela, colunas, filtros={}, qtd='todos'):
    """Criar um comando Select usando filtros

    Args:
        tabela (str): Tabela a ser selecionada
        colunas (str): Colunas a serem selecionadas
        filtros (dict, optional): Filtros para serem usados. A chave representa a coluna e o seu valor representa o valor que procura.
                                Defaults to {}.

    Returns:
        lista: Lista com todos os resultados encontrados
    """
    conn, cursor = Conectar()

    comando = "SELECT "

    for coluna in colunas:
        comando += coluna + ","
    comando = comando[:len(comando)-1] + " FROM " + tabela

    if filtros != {}:
        comando += " WHERE "

        for item in filtros.items():
            if item[0] == "NOME":
                comando += "NOME LIKE '%{}%' AND ".format(item[1])
            else:
                comando += str(item[0]) + " = '" + str(item[1]) + "' AND "

        comando = comando[:-5]

    cursor.execute(comando)

    if qtd == 'todos':
        lista = []
        for linha in cursor.fetchall():
            lista.append(linha)

        conn.close()

        return lista

    elif qtd == 'um':

        result = cursor.fetchone()
        conn.close()

        return result


def Selecionar_Diferentes(coluna, tabela):
    """Criar um comando Select para selecionar itens distintos

    Args:
        coluna (str): Coluna para procurar itens dinstintos
        tabela (str): Tabela seleconada

    Returns:
        lista: Lista com os resultados encontrados
    """
    conn, cursor = Conectar()
    comando = "SELECT DISTINCT " + coluna + " FROM " + tabela

    cursor.execute(comando)
    resultado = cursor.fetchall()

    lista = []
    for linha in resultado:
        lista.append(linha[0])

    conn.close()
    return lista


def Buscar_Parametrizacoes_Recebidas(id_maquina):
    """Buscar todas as Parametrizações feitas em uma determinada Máquina

    Args:
        id_maquina (int): ID da máquina em questão;

    Returns:
        (lista): Lista com as Linhas de registros de parametrizações
    """
    conn, cursor = Conectar()
    comando = "SELECT * FROM parametrizacoes WHERE fk_id_maquina = '{}' ".format(
        str(id_maquina))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    return resultado


def Buscar_Parametrizacoes_Feitas(id_funcionario):
    """Buscar todas as Parametrizações feitas por determinado funcionario

    Args:
        id_funcionario (int): ID da máquina em questão;

    Returns:
        (lista): Lista com as Linhas de registros de parametrizações
    """
    conn, cursor = Conectar()
    comando = "SELECT * FROM parametrizacoes WHERE fk_id_funcionario = '{}' ".format(
        str(id_funcionario))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    if resultado:
        return resultado
    else:
        return False


def Buscar_Treinamentos_Recebidos(id_agr):
    """Buscar todas os Treinamentos recebidos pelo AGR

    Args:
        id_agr (int): ID do AGR em questão;

    Returns:
        (lista): Lista com as Linhas de registros de treinamentos
    """
    conn, cursor = Conectar()
    comando = "SELECT * FROM treinamentos WHERE fk_id_agr = '{}' ".format(
        str(id_agr))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    if resultado:
        return resultado
    else:
        return False


def Buscar_Treinamentos_Feitos(id_funcionario):
    """Buscar todos os Treinamentos feitos por determinado Funcionario

    Args:
        id_funcionario (int): ID do Funcionario que fez o treinamento;

    Returns:
        (lista): Lista com as Linhas de registros de treinamentos
    """
    conn, cursor = Conectar()
    comando = "SELECT * FROM treinamentos WHERE fk_id_funcionario = '{}' ".format(
        str(id_funcionario))
    cursor.execute(comando)
    resultado = cursor.fetchall()
    conn.close()

    if resultado:
        return resultado
    else:
        return False


def Mostrar_Pendentes_Treinamento():
    """Mostrar os AGRs que estão pendentes de Treinamento

    Returns:
        list: Retorna uma lista de tuplas com os agrs que estão pendentes de treinamento.
             ('id_Requisicao','id_agr','Nome_agr','Local_agr','Telefone_agr','AC','Sistema')
    """

    lista_ids = Selecionar_Tabela_Completa('requisicoes_treinamentos')

    lista_agrs = []
    for item in lista_ids:

        agr_infos = Selecionar_Filtros('agrs', [
                                       'nome_agr', 'cidade_agr', 'uf_agr', 'telefone_agr'], {'id_agr': item[1]}, 'um')

        lista_agrs.append((item[0], item[1], agr_infos[0], agr_infos[1] +
                          ' - '+agr_infos[2], agr_infos[3], item[2], item[3]))

    #colunas = ['ID Requisicao','id_agr','Nome','Local','Telefone','AC','Sistema']

    return lista_agrs


def Mostrar_Pendentes_Parametrizacao():
    """Mostrar os AGRs que estão pendentes de parametrização

    Returns:
        list: Retorna uma lista de tuplas com os agrs que estão pendentes de parametrização.
             ('id_Requisicao','id_agr','Nome_agr','Local_agr','Telefone_agr')

    """
    lista_ids = Selecionar_Tabela_Completa('requisicoes_parametrizacoes')

    lista_agrs = []
    for item in lista_ids:

        agr_infos = Selecionar_Filtros('agrs', [
                                       'nome_agr', 'cidade_agr', 'uf_agr', 'telefone_agr'], {'id_agr': item[1]}, 'um')

        lista_agrs.append((item[0], item[1], agr_infos[0],
                          agr_infos[1]+' - '+agr_infos[2], agr_infos[3]))

    #colunas = ['ID Requisicao', 'id_agr','Nome','Local','Telefone']

    return lista_agrs


def Mostrar_Pendentes_Documentacao():
    """Mostrar os AGRs que estão pendentes de documentação

    Returns:
        list: Retorna uma lista de tuplas com os agrs que estão pendentes de documentação.
             ('id_agr','Nome_agr','Local_agr','Telefone_agr')
    """
    lista_ids = Selecionar_Tabela_Completa('documentacao')

    lista_agrs = []
    for item in lista_ids:

        if 'PENDENTE' in item:
            agr_infos = Selecionar_Filtros('agrs', [
                                           'nome_agr', 'cidade_agr', 'uf_agr', 'telefone_agr'], {'id_agr': item[0]}, 'um')

            lista_agrs.append(
                (item[0], agr_infos[0], agr_infos[1]+' - '+agr_infos[2], agr_infos[3]))

    #colunas = ['ID AGR','Nome','Local','Telefone']

    return lista_agrs


def Tabela_De_Precos(id_agr):
    """Retorna a tabela de preços já formatada

    Args:
        id_agr (int): ID do agr cuja tabela deseja selecionar

    Returns:
        list: Lista de Tuplas com o nome do produto e o preço formatado
    """

    conn, cursor = Conectar()
    comando = "SELECT * FROM tabela_precos WHERE fk_id_agr_tp = {}".format(
        id_agr)
    cursor.execute(comando)

    result = cursor.fetchone()
    aux = []
    for r in result:
        aux.append(str("%.2f" % r))

    lista = [
        ("TOKEN", "R$ {}".format(aux[1])),
        ("CARTÃO", "R$ {}".format(aux[2])),
        ("PF A1", "R$ {}".format(aux[3])),
        ("PJ A1", "R$ {}".format(aux[4])),
        ("PF A3 SEM MÍDIA", "R$ {}".format(aux[5])),
        ("PJ A3 SEM MÍDIA", "R$ {}".format(aux[6])),
        ("PF A3 COM TOKEN", "R$ {}".format(aux[7])),
        ("PJ A3 COM TOKEN", "R$ {}".format(aux[8])),
        ("PF A3 COM CARTÃO", "R$ {}".format(aux[9])),
        ("PJ A3 COM CARTÃO", "R$ {}".format(aux[10])),
    ]

    conn.close()
    return lista


def Parametrizacoes(id_agr):
    """Retorna todas as Parametrizacoes feitas para determinado AGR

    Args:
        id_agr (int): ID do AGR em questão

    Returns:
        lista: lista de tuplas com: (ID_maquina, Nome_maquina, Data_Parametrização, Nome_Funcionario, Observação_Parametrização, Status_Parametrizaçao, Nome_AGR_Assinante)
    """

    maquinas = Maquinas_do_AGR(id_agr)  # (id_maquina,nome_maquina)

    lista = []
    for m in maquinas:
        # (id_par,data_par,obs_par,status_par,id_fun,id_maq)
        parametrizacoes = Buscar_Parametrizacoes_Recebidas(m[0])
        assinada_por = Maquina_Assinada_Por(m[0])
        if not assinada_por:
            assinada_por = 'Termo Não Assinado'
        else:
            txt = 'Termo Assinado Por '
            for agr in assinada_por:
                txt += agr[1] + ', '
            assinada_por = txt[:-2]
            
        if parametrizacoes:
            for p in parametrizacoes:
                nome_func = Selecionar_Coluna_Unica('nome_funcionario', 'funcionarios', 'id_funcionario', p[4])
                # (id_maquina,nome_maquina,data_par,nome_func,obs_par,status_par,nome_agr)
                lista.append((m[0], m[1], p[1], nome_func,p[2], p[3], assinada_por))
        else:
            lista.append((m[0],m[1],' - ',' - ',' - ','SEM PARAMETRIZAÇÃO',assinada_por))

    return lista


print(Parametrizacoes(17))
############################## ALTERAR #####################################


def Alterar(tabela, coluna, novo_valor, coluna_condicao, valor_condicao):
    """Criar um comando ALTER TABLE para alterar informações de determinada tabela

    Args:
        tabela (str): Tabela onde deseja fazer alteração
        coluna (str): Coluna que deseja fazer alteraçãp
        novo_valor (str): Valor que deseja inserir
        coluna_condicao (str): Coluna com condiçção para busca
        valor_condicao (str): Valor que deseja para fazer a busca
    """
    conn, cursor = Conectar()

    comando = "UPDATE {} SET {} = '{}' WHERE {} = '{}'".format(str(tabela), str(
        coluna), str(novo_valor), str(coluna_condicao), str(valor_condicao))
    cursor.execute(comando)

    conn.commit()
    conn.close()

############################## DELETAR #####################################


def Deletar_AGR(id_agr):
    """Deletar um AGR
    Remove as situações de ACs, Documentação, Tabela de Preços, Termos e Máquinas e atrelados ao AGR
    Caso o AGR em questão seja o único atrelado a uma máquina específica, todas as parametrizações dessa máquina serão excluídas também.

    Args:
        id_agr (int): ID do AGR em questão
    """
    maquinas = Maquinas_do_AGR(
        id_agr)  # Pega todas as máquinas atreladas ao AGR
    for maquina in maquinas:  # Para cada máquina
        id_maquina = maquina[0]
        # Pega todos os AGRs que usam a máquina
        agrs = Maquina_Usada_Por(id_maquina)
        if len(agrs) == 1:  # Se tiver Apenas ele usando:
            parametrizacoes = Buscar_Parametrizacoes_Recebidas(
                id_maquina)  # Busca todas as parametrizacoes
            for parametrizacao in parametrizacoes:  # Para cada uma delas, pega o id e deleta
                id_parametrizacao = parametrizacao[0]
                Deletar('parametrizacoes',
                        'id_parametrizacao', id_parametrizacao)

    conn, cursor = Conectar()
    comando = "DELETE FROM agrs WHERE id_agr = '{}'".format(str(id_agr))
    cursor.execute(comando)
    conn.commit()
    conn.close()


def Deletar(tabela, coluna_condicao, valor_condicao):
    """Criar um comando DELETE para deletar uma linha de determinada tabela

    Args:
        tabela (str): Tabela que contêm a linha
        coluna_condicao (str): Coluna para buscar a linha
        valor_condicao (str): Valor de condição para a busca
    """
    conn, cursor = Conectar()
    comando = "DELETE FROM {} WHERE {} = '{}'".format(
        str(tabela), str(coluna_condicao), str(valor_condicao))
    cursor.execute(comando)
    conn.commit()
    conn.close()

########################## AUXILIARES ######################################


def Contagem(tabela, coluna_condicao='', valor_condicao=''):
    """Contar a quantidade de itens em uma tabela dado determinada condição.
    Caso as condições estejam vazias procura a quantidade total de itens na tabela.

    Args:
        tabela (str): Nome da tabela
        coluna_condicao (str, optional): Coluna para usar Condição para fazer a contagem. Defaults to ''.
        valor_condicao (str, optional): Valor de condição para buscar os itens. Defaults to ''.

    Returns:
        int: Valor com a quantidade contada
    """
    conn, cursor = Conectar()

    if coluna_condicao == '' and valor_condicao == '':
        comando = "SELECT COUNT(*) FROM {}".format(str(tabela))
    else:
        comando = "SELECT COUNT(*) FROM {} WHERE {} = '{}'".format(
            str(tabela), str(coluna_condicao), str(valor_condicao))

    cursor.execute(comando)
    resultado = int(cursor.fetchall()[0][0])
    conn.close()

    return resultado


def Ultima_Linha(tabela, coluna):
    """Pega os valores da ultima linha de uma tabela

    Args:
        tabela (str): Nome da Tabela
        coluna (str): Coluna para filtro

    Returns:
        tupla: Tupla com as informações da última linha
    """

    conn, cursor = Conectar()
    comando = "SELECT * FROM {} WHERE {}=(SELECT max({}) FROM {})".format(
        str(tabela), str(coluna), str(coluna), str(tabela))
    cursor.execute(comando)
    resultado = cursor.fetchone()
    conn.close()

    return resultado


def Ultima_ID(tabela, coluna):
    """Pega a última ID de determinada tabela

    Args:
        tabela (str): Nome da Tabela
        coluna (str): Coluna para filtro

    Returns:
        int: Valor da ID da última linha
    """

    conn, cursor = Conectar()
    comando = "SELECT max({}) FROM {}".format(str(coluna), str(tabela))
    cursor.execute(comando)
    resultado = cursor.fetchone()[0]
    conn.close()

    return resultado


def Autenticar_ADM(login, senha):
    """Fazer a autenticação de usuário Administrador

    Args:
        login (str): Login do funcionario
        senha (str): Senha do funcionario

    Returns:
        str: Retorna True, se a autenticação for completa e o usuário for Adiminstrador. 
        Caso não encontre o usuário ou ele não seja administrador retorna mensagem informando.
    """
    conn, cursor = Conectar()
    comando = "SELECT privilegio_funcionario FROM funcionarios WHERE "
    comando += "login_funcionario = '{}' ".format(login)
    comando += "AND senha_funcionario = '{}'".format(senha)
    cursor.execute(comando)

    resultado = cursor.fetchone()
    conn.close()

    if resultado != None:
        if resultado == 'ADMINISTRADOR':
            return True
        else:
            return "Este Usuário Não É Administrador!"
    else:
        return "Login ou Senha Incorreto!"


def Autenticar(login, senha):
    """Realizar autenticação de Funcionário

    Args:
        login (str): Login do funcionario
        senha (str): Senha do funcionario

    Returns:
        tupla: Caso a autenticação seja completa, retorna tupla com True e as informações de Nome, Cargo e Privilégio, respectivamente
        Caso contrário retorna False.
    """
    conn, cursor = Conectar()
    comando = "SELECT nome_funcionario, cargo_funcionario, privilegio_funcionario FROM FUNCIONARIOS WHERE "
    comando += "login_funcionario = '{}' ".format(login)
    comando += "AND senha_funcionario = '{}' ".format(senha)

    cursor.execute(comando)

    resultado = cursor.fetchone()
    conn.close()

    if resultado:
        return (True, resultado)
    else:
        return False

################### INSERT #########################


def Inserir_Documentacao(id_agr):
    """Inserir a Documentação Padrão
    Todos Os Itens iniciarão Como "PENDENTE"

    Args:
        id_agr (int): ID do AGR correspondente
    """
    conn, cursor = Conectar()

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

    conn, cursor = Conectar()

    comando = "INSERT INTO tabela_precos (fk_id_agr_tp)\
        VALUES ('{}')".format(id_agr)

    cursor.execute(comando)

    conn.commit()
    conn.close()


def Inserir_ACs(id_agr):
    """Inserir a Situação das ACs
    Todos Os Itens iniciarão Como "INATIVO"

    Args:
        id_agr (int): ID do AGR Correspondente
    """
    conn, cursor = Conectar()

    comando = "INSERT INTO acs (fk_id_agr_ac)\
        VALUES ('{}')".format(id_agr)

    cursor.execute(comando)

    conn.commit()
    conn.close()


def Inserir_AGR(nome, cpf, email, telefone, cidade, uf, termo, status='PENDENTE'):
    """Inserir novo AGR no Banco de Dados

    Args:
        nome (str): Nome completo do AGR;
        cpf (str): Número de CPF do AGR, com formatação;
        email (str): E-mail do AGR;
        telefone (str): Telefone do AGR, com formatação;
        cidade(str): Cidade de atuação AGR;
        uf(str): União Federal de atuação do AGR;
        termo (str): Confimação ou Negação sobre o AGR possuir termo de responsabilidade;
        status (str, optional): Status do AGR, inicialmente marcado como "PENDENTE";

    Returns:
        int: Retorna a ID do AGR inserido;
    """
    conn, cursor = Conectar()

    comando = "INSERT INTO agrs ( nome_agr, cpf_agr, e_mail_agr, telefone_agr, cidade_agr, uf_agr, termo_responsabilidade_agr, status_agr ) \
    VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(nome, cpf, email, telefone, cidade, uf, termo, status)

    try:
        cursor.execute(comando)
        id_agr = cursor.lastrowid

        conn.commit()
        conn.close()

        Inserir_Documentacao(id_agr)
        Inserir_Tabela_Precos(id_agr)
        Inserir_ACs(id_agr)

    except mysql.connector.errors.IntegrityError as err:
        if err.errno == 1062:
            print("!ERRO!\nEste número de CPF já foi inserido!")
        else:
            print("!ERRO!\nDesconhecido!")

    return id_agr


def Inserir_Maquina(nome_maquina, marca, modelo, ip, mac, termo_doacao='', bitlocker=''):
    """Adiciona uma Nova máquina no Banco de Dados

    Args:
        nome_maquina (str): Nome da máquina ;
        termo_doacao (str, optional): Arquivo do Termo de Doação. Defaults to '';
        bitlocker (str, optional): Arquivo de Bitlocker. Defaults to '';
    """
    conn, cursor = Conectar()
    comando = "INSERT INTO maquinas (nome_maquina,mac_maquina,marca_maquina,modelo_maquina,ip_maquina,mac_maquina,termo_doacao_maquina, bitlocker_maquina)\
        VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(nome_maquina, marca, modelo, ip, mac, termo_doacao, bitlocker)
    cursor.execute(comando)
    id_maquina = cursor.lastrowid
    conn.commit()
    conn.close()

    return id_maquina


def Atribuir_Maquina_AGR(id_agr, id_maquina):
    """Atribui Determinada Máquina a um AGR

    Args:
        id_agr (int): ID do AGR em questão;
        id_maquina (int): ID da Máquina em questão;
    """
    conn, cursor = Conectar()

    nome_agr = Selecionar_Coluna_Unica('nome_agr', 'agrs', 'id_agr', id_agr)
    nome_maquina = Selecionar_Coluna_Unica(
        'nome_maquina', 'maquinas', 'id_maquina', id_maquina)

    comando = "INSERT INTO agrs_possui_maquinas (fk_id_agr,nome_agr,fk_id_maquina,nome_maquina)\
        VALUES ('{}','{}','{}','{}')".format(id_agr, nome_agr, id_maquina, nome_maquina)

    try:
        cursor.execute(comando)
        conn.commit()
        conn.close()

    except mysql.connector.errors.IntegrityError as err:
        if err.errno == 1062:
            print("!ERRO!\nCombinação AGR-Máquina já inserida!")
        elif err.errno == 1452:
            print("!ERRO!\nAGR e/ou Máquina não existe(m)!")


def Assinar_Termo_Doacao(id_agr, id_maquina, termo_doacao=''):
    """Vincular um termo de doação assinado por um AGR à uma máquina

    Args:
        id_agr (int): ID do AGR em questão;
        id_maquina (int): ID da Máquina em questão;
        termo_doacao (str, optional): Arquivo do termo de doação. Defaults to '';
    """
    conn, cursor = Conectar()

    comando = "INSERT INTO agrs_assina_termos_doacao (fk_id_agr,fk_id_maquina,documento_termo_doacao)\
        VALUES ('{}','{}','{}')".format(id_agr, id_maquina, termo_doacao)

    try:
        cursor.execute(comando)
        conn.commit()
        conn.close()
    except mysql.connector.errors.IntegrityError as err:
        if err.errno == 1062:
            print("!ERRO!\nMáquina com Termo Já assinado Por Este AGR!")
        elif err.errno == 1452:
            print("!ERRO!\nAGR e/ou Máquina não existe(m)!")


def Parametrizacao(id_maquina, id_funcionario, situacao, data='', observacao=''):
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
    if data == '':
        data = datetime.now().strftime("%d/%m/%Y")

    conn, cursor = Conectar()
    comando = "INSERT INTO parametrizacoes (fk_id_maquina,fk_id_funcionario,status_req_parametrizacao,data_parametrizacao,observacoes_parametrizacao)\
        VALUES ('{}','{}','{}','{}','{}')".format(id_maquina, id_funcionario, situacao, data, observacao)
    cursor.execute(comando)
    conn.commit()
    conn.close()


def Treinar(id_agr, id_funcionario, data_treinamento, ac_treinamento, sistema_treinamento):
    """Adicionar novo Treinamento ao Banco de Dados.
    Todo treinamento é feito por um Funcionário, para um AGR

    Args:
        id_agr (int): ID do AGR a ser treinado;
        id_funcionario (int): ID do funcionario Treinador;
        data_treinamento (str): Data em que foi realizado o Treinamento;
        ac_treinamento (str): AC que fornece o sistema;
        sistema_treinamento (str): Qual sistema foi ensinado;
    """
    conn, cursor = Conectar()
    comando = "INSERT INTO treinamentos (fk_id_agr,fk_id_funcionario,data_treinamento,ac_treinamento,sistema_treinamento)\
        VALUES ('{}','{}','{}','{}','{}')".format(id_agr, id_funcionario, data_treinamento, ac_treinamento, sistema_treinamento)
    cursor.execute(comando)
    conn.commit()
    conn.close()


def Inserir_Funcionario(nome, login, senha, email, cargo, privilegio):
    """Inserir novo Funcionario que poderá utilizar o sistema

    Args:
        nome (str): Nome completo do funcionário;
        login (str): Login do funcionario;
        senha (str): Senha do funcionario;
        email (str): Email do funcionario;
        cargo (str): Cargo que o funcionario executa, o que possibilitará determinado tipo de funções dentro do sistema;
        privilegio (str): Privilegio Administrador ou Funcionario, o que possibilitará determinado tipo de ações dentro do sistema;
    """
    conn, cursor = Conectar()
    comando = "INSERT INTO funcionarios (nome_funcionario,login_funcionario,senha_funcionario,e_mail_funcionario,cargo_funcionario,privilegio_funcionario)\
        VALUES ('{}','{}','{}','{}','{}','{}')".format(nome, login, senha, email, cargo, privilegio)
    cursor.execute(comando)
    id_funcionario = cursor.lastrowid
    conn.commit()
    conn.close()
    return id_funcionario


def Inserir_Acoes(id_funcionario, acao, data_acao=''):
    """Inserir nova ação realizada por algum funcionário

    Args:
        id_funcionario (int): ID do funcionário que realizou a ação;
        acao (str): Descrição da ação realizada;
        data_acao (str): Data em que a ação foi realizada. Defaults '';
    """
    if data_acao == '':
        data_acao = datetime.now().strftime("%d/%m/%y às %H:%M")

    conn, cursor = Conectar()
    comando = "INSERT INTO acoes (fk_id_funcionario,data_acao,acao)\
        VALUES ('{}','{}','{}')".format(id_funcionario, data_acao, acao)
    cursor.execute(comando)

    conn.commit()
    conn.close()


def Requisicao_Treinamento(id_agr, ac_req, sistema):
    """Solicitar Requisição de Treinamento para determinado AGR

    Args:
        id_agr (int): ID do AGR para o qual será solicitado treinamento
        ac_req (str): AC para qual o treinamento será feito
        sistema (str): Sistema que será treinad
    """
    conn, cursor = Conectar()

    comando = "INSERT INTO requisicoes_treinamentos (fk_id_agr_req_trein, ac_req_trein, sistema_req_trein) \
        VALUES ('{}','{}','{}')".format(str(id_agr), str(ac_req), str(sistema))

    cursor.execute(comando)

    conn.commit()
    conn.close()


def Requisicao_Parametrizacao(id_agr):
    """Solicitar Requisição de Treinamento para determinado AGR

    Args:
        id_agr (int): ID do AGR para o qual será solicitado treinamento
    """
    conn, cursor = Conectar()

    comando = "INSERT INTO requisicoes_parametrizacoes (fk_id_agr_req_par)\
        VALUES ({})".format(id_agr)

    cursor.execute(comando)

    conn.commit()
    conn.close()

################################ TESTES ##########################################

# Assinar_Termo_Doacao(15,8)
# Assinar_Termo_Doacao(16,8)
# print(Maquina_Assinada_Por(8))
# Parametrizacao(8,7,'Concluida')
# Parametrizacao(8,7,'Desfeita')
# Deletar_AGR(15)
#Inserir_AGR('Evaldo','12345','evaldo@meta','2222432','Ponta Pora','MS','Nao')
#Inserir_AGR('Kevin','12345123','kevin@meta','2222245522','Rio de Janeiro','RJ','Sim')
#Inserir_AGR('Gabriel','11232345','gabriel@meta','53455222','Pimenta Bueno','RO','Nao')
#Inserir_AGR('Luis','126689345','luis@meta','22266862','Ponta Pora','MS','Nao')

# Requisicao_Parametrizacao(18)
#Requisicao_Treinamento(19,'AC META','HOPE')
#Requisicao_Treinamento(20,'AC DIGITAL','Todos')
# Requisicao_Treinamento(21,'SOLUTI','Videoconferencia')

# print(Mostrar_Pendentes_Treinamento())
# print(Mostrar_Pendentes_Parametrizacao())
# print(Mostrar_Pendentes_Documentacao())

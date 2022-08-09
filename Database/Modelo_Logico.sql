/* Modelo_Logico: */

CREATE TABLE AGRs (
    CPF VARCHAR,
    Telefone VARCHAR,
    Id_agr INT PRIMARY KEY,
    e_mail VARCHAR,
    Nome_Completo VARCHAR,
    Status VARCHAR,
    Termo_Responsabilidade VARCHAR
);

CREATE TABLE DOCUMENTACAO (
    Copia_CPF VARCHAR,
    _CER VARCHAR,
    id_doc INT PRIMARY KEY,
    CTPS VARCHAR,
    Copia_RG VARCHAR,
    Titulo_Eleitor VARCHAR,
    Escolaridade VARCHAR,
    Curriculo VARCHAR,
    Declaracao_Endereco VARCHAR,
    Roteiro_Entrevista VARCHAR,
    Curso_AGR VARCHAR,
    Certificado_Digital VARCHAR,
    Cadastro_Sistema VARCHAR,
    Termo_Responsabilidade VARCHAR
);

CREATE TABLE TABELA_PRECOS (
    Cartao FLOAT,
    A3_PJ_Cartao FLOAT,
    A3_PJ_Token FLOAT,
    A3_PF_SM FLOAT,
    id_tabela INT PRIMARY KEY,
    Token FLOAT,
    A3_PF_Cartao FLOAT,
    A1_PF FLOAT,
    A3_PF_Token DOUBLE,
    A1_PJ FLOAT,
    A3_PJ_SM FLOAT
);

CREATE TABLE FUNCIONARIOS (
    e_mail VARCHAR,
    Id_funcionario INT PRIMARY KEY,
    Nome_Completo VARCHAR,
    Senha VARCHAR,
    Login VARCHAR,
    Privilegio VARCHAR,
    Cargo VARCHAR
);

CREATE TABLE ACs (
    id_ac INT PRIMARY KEY,
    AC_Digital VARCHAR,
    AC_Soluti VARCHAR,
    AC_Meta VARCHAR
);

CREATE TABLE Maquinas (
    Termo_Doacao VARCHAR,
    Nome_maquina VARCHAR,
    Id_maquina INT PRIMARY KEY
);

CREATE TABLE Parametrizacoes (
    Data VARCHAR,
    Bitlocker VARCHAR,
    Observacoes VARCHAR,
    id_parametrizacao INT PRIMARY KEY,
    fk_FUNCIONARIOS_Id_funcionario INT,
    fk_Maquinas_Id_maquina INT,
    fk_AGRs_Id_agr INT,
    Status_Parametrizacao VARCHAR
);

CREATE TABLE Treinamentos (
    Data_treinamento VARCHAR,
    Sistema VARCHAR,
    AC VARCHAR,
    id_treinamento INT PRIMARY KEY,
    fk_AGRs_Id_agr INT,
    fk_FUNCIONARIOS_Id_funcionario INT,
    fk_ACs_id_ac INT
);

CREATE TABLE Termos_Doacao_Assinar (
    id_termo INT PRIMARY KEY,
    fk_AGRs_Id_agr INT,
    fk_Maquinas_Id_maquina INT,
    Documento VARCHAR
);

CREATE TABLE AGRs_Maquinas (
    fk_AGRs_Id_agr INT,
    fk_Maquinas_Id_maquina INT,
    fk_AGRs_Id_agr_1 INT
);

CREATE TABLE AGRs_ACs (
    fk_ACs_id_ac INT,
    fk_AGRs_Id_agr INT,
    Status_AC VARCHAR
);

CREATE TABLE AGRs_TabelaPrecos (
    fk_TABELA_PRECOS_id_tabela INT,
    fk_AGRs_Id_agr INT
);

CREATE TABLE AGRs_Documentacao (
    fk_AGRs_Id_agr INT,
    fk_DOCUMENTACAO_id_doc INT
);

CREATE TABLE Acoes (
    id_acao INT PRIMARY KEY,
    id_funcionario INT,
    acao VARCHAR
);
 
ALTER TABLE Parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_2
    FOREIGN KEY (fk_FUNCIONARIOS_Id_funcionario)
    REFERENCES FUNCIONARIOS (Id_funcionario);
 
ALTER TABLE Parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_3
    FOREIGN KEY (fk_Maquinas_Id_maquina)
    REFERENCES Maquinas (Id_maquina);
 
ALTER TABLE Parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_4
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr);
 
ALTER TABLE Treinamentos ADD CONSTRAINT FK_Treinamentos_2
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr);
 
ALTER TABLE Treinamentos ADD CONSTRAINT FK_Treinamentos_3
    FOREIGN KEY (fk_FUNCIONARIOS_Id_funcionario)
    REFERENCES FUNCIONARIOS (Id_funcionario);
 
ALTER TABLE Treinamentos ADD CONSTRAINT FK_Treinamentos_4
    FOREIGN KEY (fk_ACs_id_ac)
    REFERENCES ACs (id_ac);
 
ALTER TABLE Termos_Doacao_Assinar ADD CONSTRAINT FK_Termos_Doacao_Assinar_2
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr);
 
ALTER TABLE Termos_Doacao_Assinar ADD CONSTRAINT FK_Termos_Doacao_Assinar_3
    FOREIGN KEY (fk_Maquinas_Id_maquina)
    REFERENCES Maquinas (Id_maquina);
 
ALTER TABLE AGRs_Maquinas ADD CONSTRAINT FK_AGRs_Maquinas_1
    FOREIGN KEY (fk_AGRs_Id_agr, fk_AGRs_Id_agr_1)
    REFERENCES AGRs (Id_agr, Id_agr)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_Maquinas ADD CONSTRAINT FK_AGRs_Maquinas_2
    FOREIGN KEY (fk_Maquinas_Id_maquina)
    REFERENCES Maquinas (Id_maquina)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_ACs ADD CONSTRAINT FK_AGRs_ACs_1
    FOREIGN KEY (fk_ACs_id_ac)
    REFERENCES ACs (id_ac)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_ACs ADD CONSTRAINT FK_AGRs_ACs_2
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_TabelaPrecos ADD CONSTRAINT FK_AGRs_TabelaPrecos_1
    FOREIGN KEY (fk_TABELA_PRECOS_id_tabela)
    REFERENCES TABELA_PRECOS (id_tabela)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_TabelaPrecos ADD CONSTRAINT FK_AGRs_TabelaPrecos_2
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_Documentacao ADD CONSTRAINT FK_AGRs_Documentacao_1
    FOREIGN KEY (fk_AGRs_Id_agr)
    REFERENCES AGRs (Id_agr)
    ON DELETE SET NULL;
 
ALTER TABLE AGRs_Documentacao ADD CONSTRAINT FK_AGRs_Documentacao_2
    FOREIGN KEY (fk_DOCUMENTACAO_id_doc)
    REFERENCES DOCUMENTACAO (id_doc)
    ON DELETE SET NULL;
 
ALTER TABLE Acoes ADD CONSTRAINT FK_Acoes_2
    FOREIGN KEY (id_agr???, id_funcionario???, Campo???)
    REFERENCES ??? (???);
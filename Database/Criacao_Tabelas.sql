/* Modelo_Logico: */

CREATE TABLE agrs (
	id_agr INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    cpf_agr VARCHAR(14) NOT NULL UNIQUE,
    telefone_agr VARCHAR(15) NOT NULL,
    e_mail_agr VARCHAR(120) NOT NULL,
    nome_agr VARCHAR(200) NOT NULL,
    status_agr VARCHAR(45) NOT NULL,
    termo_responsabilidade_agr VARCHAR(45) NOT NULL
);

CREATE TABLE documentacao (
	id_doc INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    copia_cpf_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    cer_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    ctps_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    copia_rg_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    titulo__doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    escolaridade_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    curriculo_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    decl_endereco_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    rot_entrevista_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    curso_agr_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    certificado_digital_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE',
    cadastro_sistema_doc VARCHAR(45) NOT NULL DEFAULT 'PENDENTE'
);

CREATE TABLE tabela_precos (
	id_tp INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    token_tp FLOAT NOT NULL DEFAULT 0,
    cartao_tp FLOAT NOT NULL DEFAULT 0,
    a1_pf_tp FLOAT NOT NULL DEFAULT 0,
    a1_pj_tp FLOAT NOT NULL DEFAULT 0,
    a3_pf_sm_tp FLOAT NOT NULL DEFAULT 0,
    a3_pj_sm_tp FLOAT NOT NULL DEFAULT 0,
    a3_pf_token_tp DOUBLE NOT NULL DEFAULT 0,
    a3_pj_token_tp FLOAT NOT NULL DEFAULT 0,
    a3_pf_cartao_tp FLOAT NOT NULL DEFAULT 0,
    a3_pj_cartao_tp FLOAT NOT NULL DEFAULT 0    
);

CREATE TABLE funcionarios (
	id_funcionario INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    e_mail_funcionario VARCHAR(120) NOT NULL,
    nome_funcionario VARCHAR(200) NOT NULL,
    senha_funcionario VARCHAR(45) NOT NULL,
    login_funcionario VARCHAR(45) NOT NULL,
    privilegio_funcionario VARCHAR(45) NOT NULL,
    cargo_funcionario VARCHAR(45) NOT NULL
);

CREATE TABLE acs (
    id_ac INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    AC_Digital VARCHAR(45) NOT NULL DEFAULT 'INATIVO',
    AC_Soluti VARCHAR(45) NOT NULL DEFAULT 'INATIVO',
    AC_Meta VARCHAR(45) NOT NULL DEFAULT 'INATIVO'
);

CREATE TABLE maquinas (
	id_maquina INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    nome_maquina VARCHAR(200) NOT NULL,
    termo_doacao_maquina VARCHAR(45) NOT NULL,
    bitlocker_maquina VARCHAR(45) NOT NULL
);

CREATE TABLE parametrizacoes (
	id_parametrizacao INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    data_parametrizacao VARCHAR(10) NOT NULL,
    observacoes_parametrizacao VARCHAR(350) NOT NULL,
    status_parametrizacao VARCHAR(45) NOT NULL,
    
    fk_id_funcionario INT NOT NULL,
    fk_id_maquina INT NOT NULL,
    fk_id_agr INT NOT NULL
    
);

CREATE TABLE treinamentos (
	id_treinamento INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    data_treinamento VARCHAR(10) NOT NULL,
    sistema_treinamento VARCHAR(45) NOT NULL,
    ac_treinamento VARCHAR(45) NOT NULL,
    
    fk_id_agr INT NOT NULL,
    fk_id_funcionario INT NOT NULL,
    fk_id_ac INT NOT NULL
);

CREATE TABLE agr_assina_termos_doacao (
    id_termo_doacao INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    documento_termo_doacao VARCHAR(45) NOT NULL,
    
    fk_id_agr INT NOT NULL,
    fk_id_maquina INT NOT NULL
    
);

CREATE TABLE agrs_possui_maquinas (
    fk_id_agr INT NOT NULL,
    fk_id_maquina INT NOT NULL
);

CREATE TABLE agrs_atua_acs (
	Status_AC VARCHAR(45) NOT NULL,
    
    fk_id_ac INT NOT NULL,
    fk_id_agr INT NOT NULL
);

CREATE TABLE agrs_tem_tabela_precos (
    fk_id_tp INT NOT NULL,
    fk_id_agr INT NOT NULL
);

CREATE TABLE agrs_tem_documentacao (
    fk_id_agr INT NOT NULL,
    fk_id_doc INT NOT NULL
);

CREATE TABLE acoes (
    id_acao INT PRIMARY KEY NOT NULL UNIQUE AUTO_INCREMENT,
    acao VARCHAR(500) NOT NULL,
    
    fk_id_funcionario INT NOT NULL
);
 
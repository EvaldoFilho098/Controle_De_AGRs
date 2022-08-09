ALTER TABLE Parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_2
    FOREIGN KEY (fk_id_funcionario)
    REFERENCES funcionarios (id_funcionario);
 
ALTER TABLE parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_3
    FOREIGN KEY (fk_id_maquina)
    REFERENCES maquinas (id_maquina);
 
ALTER TABLE parametrizacoes ADD CONSTRAINT FK_Parametrizacoes_4
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE treinamentos ADD CONSTRAINT FK_Treinamentos_2
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE treinamentos ADD CONSTRAINT FK_Treinamentos_3
    FOREIGN KEY (fk_id_funcionario)
    REFERENCES funcionarios (id_funcionario);
 
ALTER TABLE treinamentos ADD CONSTRAINT FK_Treinamentos_4
    FOREIGN KEY (fk_id_ac)
    REFERENCES acs (id_ac);
 
ALTER TABLE agr_assina_termos_doacao ADD CONSTRAINT FK_Termos_Doacao_Assinar_2
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE agr_assina_termos_doacao ADD CONSTRAINT FK_Termos_Doacao_Assinar_3
    FOREIGN KEY (fk_id_maquina)
    REFERENCES maquinas (id_maquina);
 
ALTER TABLE agrs_possui_maquinas ADD CONSTRAINT FK_AGRs_Maquinas_1
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
    
ALTER TABLE agrs_possui_maquinas ADD CONSTRAINT FK_AGRs_Maquinas_2
    FOREIGN KEY (fk_id_maquina)
    REFERENCES maquinas (id_maquina);
 
ALTER TABLE agrs_atua_acs ADD CONSTRAINT FK_AGRs_ACs_1
    FOREIGN KEY (fk_id_ac)
    REFERENCES acs (id_ac);
 
ALTER TABLE agrs_atua_acs ADD CONSTRAINT FK_AGRs_ACs_2
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE agrs_tem_tabela_precos ADD CONSTRAINT FK_AGRs_TabelaPrecos_1
    FOREIGN KEY (fk_id_tp)
    REFERENCES tabela_precos (id_tp);
 
ALTER TABLE agrs_tem_tabela_precos ADD CONSTRAINT FK_AGRs_TabelaPrecos_2
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE agrs_tem_documentacao ADD CONSTRAINT FK_AGRs_Documentacao_1
    FOREIGN KEY (fk_id_agr)
    REFERENCES agrs (id_agr);
 
ALTER TABLE agrs_tem_documentacao ADD CONSTRAINT FK_AGRs_Documentacao_2
    FOREIGN KEY (fk_id_doc)
    REFERENCES documentacao (id_doc);

ALTER TABLE acoes ADD CONSTRAINT FK_Funcionarios_Aoes_1
    FOREIGN KEY (fk_id_funcionario)
    REFERENCES funcionarios (id_funcionario);
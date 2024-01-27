-- Inserir dados do banco_corrigido_1
INSERT INTO dados_gerais (data, id_marca, vendas, valor_do_veiculo, nome, marca)
SELECT data, id_marca_, vendas, valor_do_veiculo, nome, '' FROM banco_corrigido_1;
-- Atualizar a coluna 'marca' com os valores de banco_corrigido_2
UPDATE dados_gerais
SET marca = (SELECT banco_corrigido_2.marca
             FROM banco_corrigido_2
             WHERE dados_gerais.id_marca = banco_corrigido_2.id_marca);

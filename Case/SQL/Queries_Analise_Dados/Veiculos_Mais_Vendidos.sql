-- Existe alguma relação entre os veículos mais vendidos?
SELECT nome, marca, SUM(vendas) AS total_de_vendas
FROM dados_gerais
GROUP BY nome, marca
ORDER BY total_de_vendas DESC;
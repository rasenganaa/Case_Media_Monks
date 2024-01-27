-- Qual a média de vendas do ano por marca?
SELECT marca, AVG(vendas) AS media_de_vendas_por_ano
FROM dados_gerais
GROUP BY marca;

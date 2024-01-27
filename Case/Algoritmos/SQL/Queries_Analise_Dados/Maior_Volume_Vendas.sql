--Qual marca teve o maior volume de vendas?
SELECT marca, SUM(vendas) AS volume_de_vendas
FROM dados_gerais
GROUP BY marca
ORDER BY volume_de_vendas DESC
LIMIT 1;

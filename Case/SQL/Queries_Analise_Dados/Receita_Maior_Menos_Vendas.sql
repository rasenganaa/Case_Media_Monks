-- Quais marcas geraram uma receita maior com número menor de vendas? 
SELECT marca, SUM(valor_do_veiculo) AS receita_total, SUM(vendas) AS total_de_vendas
FROM dados_gerais
GROUP BY marca
ORDER BY receita_total DESC, total_de_vendas ASC;
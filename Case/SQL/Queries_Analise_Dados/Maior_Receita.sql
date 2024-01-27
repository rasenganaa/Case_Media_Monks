-- Qual veículo gerou a maior receita? 
SELECT nome, MAX(valor_do_veiculo) AS maior_receita
FROM dados_gerais
GROUP BY nome
ORDER BY maior_receita DESC
LIMIT 1;

-- Qual veículo gerou menor receita? 
SELECT nome, MIN(valor_do_veiculo) AS menor_receita
FROM dados_gerais
GROUP BY nome
ORDER BY menor_receita
LIMIT 1;

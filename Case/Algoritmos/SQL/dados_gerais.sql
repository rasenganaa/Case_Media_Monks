/*
    Tabela: dados_gerais
    
    Descrição:
    Esta tabela armazena dados gerais relacionados a veículos, incluindo informações sobre vendas e valores.
*/

-- Comando para criar a tabela dados_gerais, caso ela não exista.
CREATE TABLE IF NOT EXISTS dados_gerais (
    -- ID: Chave primária para identificar de forma única cada registro na tabela.
    id INTEGER PRIMARY KEY,
    
    data TEXT,
    
    id_marca INTEGER,
    
    vendas INTEGER,
    
    valor_do_veiculo REAL,
    
    nome TEXT,
    
    marca TEXT,
    
    -- Garante que o valor da coluna 'id' seja único em toda a tabela, evitando duplicidade.
    UNIQUE (id)
);

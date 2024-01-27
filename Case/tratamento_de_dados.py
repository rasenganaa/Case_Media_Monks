
import csv

def remover_primeira_coluna_e_adicionar_linha0(arquivo_entrada: str, arquivo_saida: str) -> None:
    """
    Remove a primeira coluna de um arquivo CSV e adiciona uma nova linha no início.

    Parameters:
    - arquivo_entrada (str): O caminho do arquivo CSV de entrada.
    - arquivo_saida (str): O caminho do arquivo CSV de saída.

    Returns:
    - None
    """
    # Abrir o arquivo de entrada para leitura
    with open(arquivo_entrada, 'r', newline='') as arquivo_entrada:
        leitor_csv = csv.reader(arquivo_entrada)
        linhas = list(leitor_csv)

    # Remover o primeiro elemento de cada linha (antiga coluna 0)
    for linha in linhas:
        del linha[0]

    # Adicionar a nova linha (linha 0) no início da lista de linhas
    nova_linha = ['data', 'id_marca_', 'vendas', 'valor_do_veiculo', 'nome', 'marca']
    linhas.insert(0, nova_linha)

    # Abrir o arquivo de saída para escrita
    with open(arquivo_saida, 'w', newline='') as arquivo_saida:
        escritor_csv = csv.writer(arquivo_saida)
        escritor_csv.writerows(linhas)

# Exemplo de uso
arquivo_entrada = r'C:\Users\Ana Brandão\Desktop\Case\Dataset\dados_gerais.csv'
arquivo_saida = r'C:\Users\Ana Brandão\Desktop\Case\Dataset\dados_cleaned.csv'

# Chamar a função para processar o arquivo
remover_primeira_coluna_e_adicionar_linha0(arquivo_entrada, arquivo_saida)

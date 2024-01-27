import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import calendar
from pandas.plotting import table

def carregar_dados(caminho_arquivo):
    """
    Carrega dados a partir de um arquivo CSV.

    Parameters:
    - caminho_arquivo (str): O caminho do arquivo CSV.

    Returns:
    - pd.DataFrame: O DataFrame contendo os dados carregados.
    """
    return pd.read_csv(caminho_arquivo)

def criar_grafico_correlacao_popularidade_valor_marca_temporal(dados, salvar_grafico=False):
    """
    Cria um gráfico de linha que representa a correlação entre a popularidade de marca e o valor médio mensal por marca.

    Parameters:
    - dados (pd.DataFrame): O DataFrame contendo os dados.
    - salvar_grafico (bool): Indica se o gráfico deve ser salvo como imagem PNG.

    Returns:
    - None
    """
    if 'data' not in dados.columns:
        print("Erro: A coluna 'data' não foi encontrada nos dados.")
        return

    dados['data'] = pd.to_datetime(dados['data'])
    dados['mes'] = dados['data'].dt.month
    dados_agrupados = dados.groupby(['marca', 'mes'])[['vendas', 'valor_do_veiculo']].sum().reset_index()
    dados_agrupados['valor_medio'] = dados_agrupados['valor_do_veiculo'] / dados_agrupados['vendas']

    plt.figure(figsize=(14, 6))
    sns.lineplot(x='mes', y='valor_medio', hue='marca', data=dados_agrupados, marker='o', palette='magma')
    plt.title('Correlação entre Popularidade de Marca e Valor Médio Mensal por Marca')
    plt.xlabel('Mês')
    plt.ylabel('Valor Médio por Marca')
    plt.xticks(range(1, 13), calendar.month_abbr[1:], rotation=45, ha='right')
    plt.legend(title='Marca', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()

    print(f"Impressão do arquivo: {os.path.abspath(os.path.realpath(caminho_arquivo))}")

    if salvar_grafico:
        plt.savefig('correlacao_popularidade_valor_marca.png')

    plt.show()

def calcular_preco_medio_por_marca(dados):
    """
    Calcula o preço médio por marca.

    Parameters:
    - dados (pd.DataFrame): O DataFrame contendo os dados.

    Returns:
    - pd.DataFrame: O DataFrame com a média de preço por marca.
    """
    dados_agrupados = dados.groupby('marca')['valor_do_veiculo'].mean().reset_index()
    dados_agrupados['preco_medio'] = dados_agrupados['valor_do_veiculo'].map('R${:,.2f}'.format)
    return dados_agrupados

# Caminho do arquivo CSV
caminho_arquivo = r'C:\Users\Ana Brandão\Desktop\Case\Dataset\dados_cleaned.csv'
dados = carregar_dados(caminho_arquivo)

# Calcular o preço médio por marca
tabela_preco_medio = calcular_preco_medio_por_marca(dados)

# Salvar a tabela como uma imagem PNG
fig, ax = plt.subplots(figsize=(8, 3)) 
ax.axis('off')
tbl = table(ax, tabela_preco_medio, loc='center', colWidths=[0.2]*len(tabela_preco_medio.columns))
tbl.auto_set_font_size(False)
tbl.set_fontsize(10)
tbl.auto_set_column_width(col=list(range(len(tabela_preco_medio.columns))))
plt.savefig('tabela_preco_medio.png', bbox_inches='tight', pad_inches=0.05)
print("Tabela de preço médio salva como tabela_preco_medio.png")
plt.show()

# Cria e exibe o gráfico, e opcionalmente, salva como PNG
criar_grafico_correlacao_popularidade_valor_marca_temporal(dados, salvar_grafico=True)

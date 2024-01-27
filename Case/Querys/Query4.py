import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table
import seaborn as sns

class AnaliseVendasPorMarca:
    """
    Classe responsável por realizar a análise de vendas por marca, incluindo um gráfico de dispersão e uma tabela de resumo.

    Attributes:
        caminho_arquivo (str): Caminho do arquivo CSV contendo os dados.
        df (pd.DataFrame): DataFrame para armazenar os dados carregados.

    Methods:
        carregar_dados: Carrega os dados do arquivo CSV.
        limpar_nomes_marcas: Remove espaços extras nos nomes das marcas.
        calcular_receita_e_vendas: Calcula a receita total e o número total de vendas por marca.
        criar_grafico_dispersao: Cria um gráfico de dispersão destacando marcas com maior receita e menor número de vendas.
        criar_tabela_resumo: Cria uma tabela de resumo ordenada pela receita gerada por marca.
    """

    def __init__(self, caminho_arquivo: str):
        """
        Inicializa a instância da classe.

        Args:
            caminho_arquivo (str): Caminho do arquivo CSV contendo os dados.
        """
        self.caminho_arquivo = caminho_arquivo
        self.df = None

    def carregar_dados(self) -> None:
        """
        Carrega os dados do arquivo CSV.
        """
        self.df = pd.read_csv(self.caminho_arquivo)

    def limpar_nomes_marcas(self) -> None:
        """
        Remove espaços extras nos nomes das marcas.
        """
        self.df['marca'] = self.df['marca'].str.strip()

    def calcular_receita_e_vendas(self) -> None:
        """
        Calcula a receita total e o número total de vendas por marca.
        """
        receita_por_marca = self.df.groupby('marca')['valor_do_veiculo'].sum().sort_values(ascending=False)
        vendas_por_marca = self.df.groupby('marca')['vendas'].sum()
        marcas_destacadas = receita_por_marca[receita_por_marca / vendas_por_marca < receita_por_marca.mean() / vendas_por_marca.mean()]
        self.df = self.df.set_index('marca').loc[receita_por_marca.index].reset_index()

        # Criando o gráfico de dispersão
        plt.figure(figsize=(12, 8))

        # Adicionando os pontos no gráfico
        for marca in self.df['marca'].unique():
            marca_data = self.df[self.df['marca'] == marca]
            valor_total = marca_data['valor_do_veiculo'].sum()
            label = f'{marca}\n(R$ {valor_total:,.2f} receita)'

            # Destacando marcas com maior receita e menor número de vendas
            if marca in marcas_destacadas.index:
                plt.scatter(marca_data['vendas'], marca_data['valor_do_veiculo'], s=150, alpha=0.9, label=label, color='red', marker='o')
            else:
                plt.scatter(marca_data['vendas'], marca_data['valor_do_veiculo'], s=100, alpha=0.7, label=label)

        # Adicionando rótulos e título
        plt.title('Relação entre Vendas e Valor do Veículo por Marca')
        plt.xlabel('Número de Vendas')
        plt.ylabel('Valor do Veículo')

        # Ajustando layout
        plt.tight_layout()

        # Exibindo o gráfico
        plt.show()

    def criar_tabela_resumo(self) -> None:
        """
        Cria uma tabela de resumo ordenada pela receita gerada por marca e a exibe como uma imagem PNG.
        """
        tabela_resumo = pd.DataFrame({
            'Marca': self.df.groupby('marca')['vendas'].sum().index,
            'Número de Vendas': self.df.groupby('marca')['vendas'].sum().values,
            'Receita Gerada': self.df.groupby('marca')['valor_do_veiculo'].sum().values
        })

        tabela_resumo = tabela_resumo.sort_values(by='Receita Gerada', ascending=False)

        # Plotando a tabela como uma imagem com estilo moderno e paleta de cinza
        fig, ax = plt.subplots(figsize=(8, 3))
        ax.set_frame_on(False)
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)

        # Utilizando o estilo de fundo do seaborn
        sns.set_style("whitegrid")

        tabla = table(ax, tabela_resumo, loc='center', colWidths=[0.15]*len(tabela_resumo.columns), cellLoc='center', colColours=['#f2f2f2']*len(tabela_resumo.columns))
        tabla.auto_set_font_size(False)
        tabla.set_fontsize(8)
        tabla.scale(1.2, 1.2)

        # Salvando a imagem como um arquivo PNG
        plt.savefig('tabela_resumo.png', bbox_inches='tight', pad_inches=0.05, transparent=True)
        plt.show()

def main():
    """
    Função principal para executar a análise de vendas por marca.
    """
    caminho_arquivo = r'C:\Users\Ana Brandão\Desktop\Case\Dataset\dados_cleaned.csv'
    analise_vendas = AnaliseVendasPorMarca(caminho_arquivo)
    analise_vendas.carregar_dados()
    analise_vendas.limpar_nomes_marcas()
    analise_vendas.calcular_receita_e_vendas()
    analise_vendas.criar_tabela_resumo()

if __name__ == "__main__":
    main()

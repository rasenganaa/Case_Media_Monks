import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class GraficoVendas:
    """
    Classe que representa um gráfico de barras horizontais mostrando o volume de vendas por marca.

    Attributes:
        dados (pd.DataFrame): DataFrame contendo os dados de vendas por marca.

    Methods:
        calcular_vendas_por_marca: Calcula o número total de vendas por marca.
        plotar_grafico: Plota o gráfico de barras horizontais mostrando o volume de vendas por marca.
    """

    def __init__(self, caminho_arquivo: str):
        """
        Inicializa a instância da classe.

        Args:
            caminho_arquivo (str): O caminho do arquivo CSV contendo os dados.
        """
        self.dados = pd.read_csv(caminho_arquivo)

    def calcular_vendas_por_marca(self):
        """
        Calcula o número total de vendas por marca.

        Returns:
            pd.DataFrame: DataFrame contendo as marcas e seus respectivos volumes de vendas, ordenados por volume.
        """
        vendas_por_marca = self.dados.groupby('marca')['vendas'].sum().reset_index()
        return vendas_por_marca.sort_values(by='vendas', ascending=False)

    def plotar_grafico(self):
        """
        Plota o gráfico de barras horizontais mostrando o volume de vendas por marca.
        Os resultados são salvos como uma imagem PNG chamada 'grafico_vendas.png'.
        """
        # Calcular o número de vendas por marca
        vendas_por_marca = self.calcular_vendas_por_marca()

        # Definir a paleta de cores Viridis
        viridis_colors = sns.color_palette("viridis", len(vendas_por_marca))

        # Inicializar o gráfico
        plt.figure(figsize=(12, 8))

        # Gráfico de barras horizontal com a paleta de cores Viridis
        barplot = sns.barplot(x='vendas', y='marca', data=vendas_por_marca, palette=viridis_colors, hue='marca', legend=False)

        # Adicionar os valores em frente a cada barra
        for index, value in enumerate(vendas_por_marca['vendas']):
            barplot.text(value + 1, index, f'{value:,}', ha='left', va='center', fontsize=10)

        # Adicionar rótulos e título
        plt.xlabel('Vendas')
        plt.ylabel('Marca')
        plt.title('Volume de Vendas por Marca')

        # Ajustar layout e salvar o gráfico
        plt.tight_layout()
        plt.savefig('grafico_vendas.png')

        # Mostrar o gráfico
        plt.show()

def main():
    """
    Função principal para executar o exemplo de uso da classe GraficoVendas.
    """
    # Caminho do arquivo CSV
    caminho_arquivo = r'Dataset\dados_cleaned.csv'

    # Criar uma instância da classe GraficoVendas
    grafico_vendas = GraficoVendas(caminho_arquivo)

    # Plotar o gráfico
    grafico_vendas.plotar_grafico()

if __name__ == "__main__":
    main()

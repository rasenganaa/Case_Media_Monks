import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MatrizCorrelacaoPlotter:
    def __init__(self, caminho_arquivo: str, colunas_interesse: list):
        """
        Inicializa um objeto MatrizCorrelacaoPlotter.

        Args:
            caminho_arquivo (str): O caminho do arquivo CSV contendo os dados.
            colunas_interesse (list): Lista de colunas para as quais a matriz de correlação será calculada.
        """
        self.caminho_arquivo = caminho_arquivo
        self.colunas_interesse = colunas_interesse

    def carregar_dados(self):
        """
        Carrega os dados do arquivo CSV e retorna o DataFrame correspondente.

        Returns:
            pd.DataFrame: DataFrame carregado a partir do arquivo CSV.
        """
        return pd.read_csv(self.caminho_arquivo)

    def calcular_matriz_correlacao(self, dados):
        """
        Calcula a matriz de correlação para as colunas de interesse.

        Args:
            dados (pd.DataFrame): DataFrame contendo os dados.

        Returns:
            pd.DataFrame: Matriz de correlação calculada.
        """
        return dados[self.colunas_interesse].corr()

    def plotar_matriz_correlacao(self, correlation_matrix):
        """
        Plota a matriz de correlação usando Seaborn.

        Args:
            correlation_matrix (pd.DataFrame): Matriz de correlação a ser plotada.
        """
        # Configurações estéticas para melhor visualização
        plt.figure(figsize=(8, 6))
        sns.set(font_scale=1.2)
        sns.set_style("whitegrid")

        # Plotando a matriz de correlação usando Seaborn
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=.5)

        # Adicionando título
        plt.title('Matriz de Correlação entre Vendas e Valor do Veículo')

        # Exibindo o gráfico
        plt.show()

    def executar(self):
        """
        Executa o processo completo de carregar dados, calcular matriz de correlação e plotar o gráfico.
        """
        dados = self.carregar_dados()
        correlation_matrix = self.calcular_matriz_correlacao(dados)
        self.plotar_matriz_correlacao(correlation_matrix)

# Exemplo de uso
caminho_arquivo = "Dataset/dados_cleaned.csv"
colunas_interesse = ['vendas', 'valor_do_veiculo']

# Criando uma instância do MatrizCorrelacaoPlotter
plotter = MatrizCorrelacaoPlotter(caminho_arquivo, colunas_interesse)

# Executando o processo completo
plotter.executar()

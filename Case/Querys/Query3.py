import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

class MediaVendasPorMarca:
    """
    Classe responsável por calcular e visualizar a média ponderada de vendas por marca.

    Attributes:
        file_path (str): Caminho do arquivo CSV contendo os dados.
        df (pd.DataFrame): DataFrame para armazenar os dados carregados.

    Methods:
        carregar_dados: Carrega os dados do arquivo CSV. Exibe uma mensagem de erro se o arquivo não for encontrado.
        calcular_media_ponderada: Calcula a média ponderada de vendas por marca.
        criar_grafico: Cria um gráfico de barras verticais com a média ponderada de vendas por marca.
    """

    def __init__(self, file_path: str):
        """
        Inicializa a instância da classe.

        Args:
            file_path (str): Caminho do arquivo CSV contendo os dados.
        """
        self.file_path = file_path
        self.df = None

    def carregar_dados(self) -> None:
        """
        Carrega os dados do arquivo CSV. Exibe uma mensagem de erro se o arquivo não for encontrado.
        """
        try:
            self.df = pd.read_csv(self.file_path)
        except FileNotFoundError:
            print(f'O arquivo {self.file_path} não foi encontrado. Verifique o caminho.')

    def calcular_media_ponderada(self) -> pd.DataFrame:
        """
        Calcula a média ponderada de vendas por marca.

        Returns:
            pd.DataFrame: DataFrame contendo as marcas e suas respectivas médias ponderadas de vendas.
        """
        self.df['Vendas_Ponderadas'] = self.df['vendas'] * self.df.groupby('marca')['vendas'].transform('mean')
        media_vendas_por_marca = self.df.groupby('marca')['Vendas_Ponderadas'].sum() / self.df.groupby('marca')['vendas'].sum()
        media_vendas_por_marca = media_vendas_por_marca.reset_index()
        media_vendas_por_marca.columns = ['marca', 'Media_Vendas']
        return media_vendas_por_marca

    def criar_grafico(self) -> None:
        """
        Cria um gráfico de barras verticais com a média ponderada de vendas por marca.
        """
        media_vendas_por_marca = self.calcular_media_ponderada()

        # Configurações estéticas com Seaborn e Matplotlib
        sns.set(style="whitegrid")
        plt.figure(figsize=(10, 6))
        ax = sns.barplot(x='marca', y='Media_Vendas', data=media_vendas_por_marca, palette='viridis')

        # Adicionando rótulos e título ao gráfico
        plt.title('Média de Vendas por Marca')
        plt.xlabel('Marca')
        plt.ylabel('Média de Vendas(%)')
        plt.xticks(rotation=45, ha='right')

        # Adicionando rótulos em porcentagem dentro das barras
        for p in ax.patches:
            ax.annotate(f'{p.get_height():.2f}%', (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center', xytext=(0, 10), textcoords='offset points')

        plt.tight_layout()
        plt.show()

def main():
    """
    Função principal para executar o exemplo de uso da classe MediaVendasPorMarca.
    """
    file_path = r'C:\Users\Ana Brandão\Desktop\Case\Dataset\dados_cleaned.csv'
    analise_vendas = MediaVendasPorMarca(file_path)
    analise_vendas.carregar_dados()
    analise_vendas.criar_grafico()

if __name__ == "__main__":
    main()

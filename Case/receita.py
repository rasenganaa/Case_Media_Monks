import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import table

class TabelaReceitaPlotter:
    """
    A classe TabelaReceitaPlotter é responsável por carregar dados de um arquivo CSV,
    calcular a receita por marca, criar uma tabela com as informações relevantes e gerar
    um gráfico de tabela destacando a receita total.

    Attributes:
        caminho_arquivo (str): O caminho do arquivo CSV contendo os dados.
    """

    def __init__(self, caminho_arquivo: str):
        """
        Inicializa um objeto TabelaReceitaPlotter.

        Args:
            caminho_arquivo (str): O caminho do arquivo CSV contendo os dados.
        """
        self.caminho_arquivo = caminho_arquivo

    def carregar_dados(self):
        """
        Carrega os dados do arquivo CSV e retorna o DataFrame correspondente.

        Returns:
            pd.DataFrame: DataFrame carregado a partir do arquivo CSV.
        """
        return pd.read_csv(self.caminho_arquivo)

    def calcular_receita_por_marca(self, dados):
        """
        Agrupa os dados por marca e calcula a receita total para cada uma.

        Args:
            dados (pd.DataFrame): DataFrame contendo os dados.

        Returns:
            pd.Series: Série contendo a receita total por marca.
        """
        grupo_marca = dados.groupby('marca')
        return grupo_marca['vendas', 'valor_do_veiculo'].apply(lambda x: (x['vendas'] * x['valor_do_veiculo']).sum())

    def criar_tabela_df(self, dados, receita_por_marca):
        """
        Cria um DataFrame para a tabela com as informações relevantes.

        Args:
            dados (pd.DataFrame): DataFrame contendo os dados.
            receita_por_marca (pd.Series): Série com a receita total por marca.

        Returns:
            pd.DataFrame: DataFrame para a tabela.
        """
        tabela_df = pd.DataFrame(columns=['Data', 'ID_Marca', 'Vendas', 'Valor/Veículo', 'Nome', 'Marca', 'Receita'])
        total_receita = 0

        for indice, linha in dados.iterrows():
            marca = linha['marca']
            if marca not in receita_por_marca:
                continue

            receita = linha['vendas'] * linha['valor_do_veiculo']
            total_receita += receita

            tabela_df = tabela_df.append({
                'Data': linha['data'],
                'ID_Marca': linha['id_marca_'],
                'Vendas': linha['vendas'],
                'Valor/Veículo': linha['valor_do_veiculo'],
                'Nome': linha['nome'],
                'Marca': marca,
                'Receita': receita
            }, ignore_index=True)

        tabela_df = tabela_df.append({'Receita': total_receita}, ignore_index=True)
        return tabela_df

    def plotar_tabela_receita(self, tabela_df, total_receita):
        """
        Gera um gráfico de tabela destacando a receita total.

        Args:
            tabela_df (pd.DataFrame): DataFrame para a tabela.
            total_receita (float): Receita total a ser destacada.
        """
        # Criar figura e eixo
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.axis('off')

        # Criar a tabela e adicionar à figura
        tbl = table(ax, tabela_df, loc='center', colWidths=[0.1] * len(tabela_df.columns),
                    cellLoc='center', colColours=['#f5f5f5'] * len(tabela_df.columns))
        tbl.auto_set_font_size(False)
        tbl.set_fontsize(10)
        tbl.scale(1.2, 1.2)

        # Adicionar linha de destaque para o total
        tabela_df = tabela_df.append({'Receita': total_receita}, ignore_index=True)

        # Salvar a figura como PNG
        plt.savefig('tabela_receita.png', bbox_inches='tight', pad_inches=0.5)
        plt.show()

    def executar(self):
        """
        Executa o processo completo de carregar dados, calcular receita por marca,
        criar a tabela e gerar o gráfico de tabela.
        """
        dados = self.carregar_dados()
        receita_por_marca = self.calcular_receita_por_marca(dados)
        tabela_df = self.criar_tabela_df(dados, receita_por_marca)
        total_receita = tabela_df.loc[tabela_df['Receita'].idxmax(), 'Receita']
        self.plotar_tabela_receita(tabela_df, total_receita)


# Exemplo de uso
caminho_arquivo = "Dataset/dados_cleaned.csv"
tabela_plotter = TabelaReceitaPlotter(caminho_arquivo)
tabela_plotter.executar()
 
 
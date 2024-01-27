import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import table

class TabelaTop10Veiculos:
    """
    Classe que cria uma tabela dos top 10 veículos com base nas vendas totais.

    Args:
        dados (pd.DataFrame): DataFrame contendo os dados dos veículos.

    Attributes:
        dados (pd.DataFrame): DataFrame contendo os dados dos veículos.
        fig (matplotlib.figure.Figure): A figura matplotlib que contém a tabela.
        ax (matplotlib.axes._axes.Axes): Os eixos matplotlib nos quais a tabela é desenhada.
        table (matplotlib.table.Table): A tabela matplotlib que exibe os dados.

    Methods:
        _criar_tabela: Cria a tabela matplotlib.
        _obter_top_10_veiculos: Obtém os top 10 veículos com base nas vendas totais.
        _formatar_dados_tabela: Formata os dados para a tabela matplotlib.
        _estilizar_tabela: Estiliza a tabela matplotlib.
        salvar_como_imagem: Salva a tabela como uma imagem PNG.
        exibir_tabela: Exibe a tabela (opcional).
    """

    def __init__(self, dados):
        """
        Inicializa a instância da classe.

        Args:
            dados (pd.DataFrame): DataFrame contendo os dados dos veículos.
        """
        self.dados = dados
        self._criar_tabela()

    def _criar_tabela(self):
        """
        Cria a tabela matplotlib.
        """
        tabela_top_10_veiculos = self._obter_top_10_veiculos()

        # Criar tabela matplotlib
        self.fig, self.ax = plt.subplots(figsize=(16, 8))
        self.ax.axis('off')

        table_data = self._formatar_dados_tabela(tabela_top_10_veiculos)

        self.table = self.ax.table(cellText=table_data, colLabels=tabela_top_10_veiculos.columns,
                                   cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

        self._estilizar_tabela()

        # Adicionar borda à tabela
        self.ax.add_table(self.table)

    def _obter_top_10_veiculos(self):
        """
        Obtém os top 10 veículos com base nas vendas totais.

        Returns:
            pd.DataFrame: DataFrame com os top 10 veículos e suas vendas totais.
        """
        vendas_por_veiculo = self.dados.groupby('nome')['vendas'].sum()
        tabela_top_10_veiculos = pd.DataFrame({'Veículo': vendas_por_veiculo.index, 'Vendas Totais': vendas_por_veiculo.values})
        tabela_top_10_veiculos = tabela_top_10_veiculos.sort_values(by='Vendas Totais', ascending=False).head(10)
        tabela_top_10_veiculos.index = range(1, 11)
        return tabela_top_10_veiculos

    def _formatar_dados_tabela(self, tabela_top_10_veiculos):
        """
        Formata os dados para a tabela matplotlib.

        Args:
            tabela_top_10_veiculos (pd.DataFrame): DataFrame com os top 10 veículos e suas vendas totais.

        Returns:
            list: Lista de listas contendo os dados formatados para a tabela matplotlib.
        """
        # Adicionar a coluna de índice de 1 a 10
        tabela_top_10_veiculos.insert(0, 'Índice', range(1, 11))

        # Função para formatar os dados para a tabela matplotlib
        table_data = [list(row) for _, row in tabela_top_10_veiculos.iterrows()]
        return table_data

    def _estilizar_tabela(self):
        """
        Estiliza a tabela matplotlib.
        """
        self.table.auto_set_font_size(False)
        self.table.set_fontsize(12)
        self.table.scale(1.2, 1.2)

        colors = ['#F0F0F0', '#D9D9D9', '#C0C0C0']
        for i, key in enumerate(self.table._cells):
            cell = self.table._cells[key]
            if i % 3 == 0:  # Destacar a primeira coluna
                cell.set_facecolor('#606c88')  # Usar a cor da paleta cinza moderna
                cell.set_text_props(color='white')
            elif i // 1 == 0:  # Destacar a primeira linha
                cell.set_facecolor('#606c88')  # Usar a cor da paleta cinza moderna
                cell.set_text_props(color='white')
            elif i > 30:  # Ignorar as três primeiras células (cabeçalho)
                cell.set_facecolor('#606c88')  # Usar a cor da paleta cinza moderna
                cell.set_text_props(color='white')

    def salvar_como_imagem(self, caminho):
        """
        Salva a tabela como uma imagem PNG.

        Args:
            caminho (str): O caminho do arquivo onde a imagem será salva.
        """
        self.fig.savefig(caminho, bbox_inches='tight', pad_inches=0.5, transparent=True)

    def exibir_tabela(self):
        """
        Exibe a tabela (opcional).
        """
        plt.show()

# Exemplo de uso
caminho_arquivo = 'Dataset/dados_cleaned.csv'
dados = pd.read_csv(caminho_arquivo)

# Configurar a paleta de cores cinza para seaborn
sns.set_palette("Greys")

tabela_top_10_veiculos = TabelaTop10Veiculos(dados)
tabela_top_10_veiculos.salvar_como_imagem('Querys\\Query5\\tabela_top_10_veiculos.png')
tabela_top_10_veiculos.exibir_tabela()

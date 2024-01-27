import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

class TabelaReceita:
    """
    Classe responsável por criar e visualizar uma tabela de receitas por veículo.

    Attributes:
        caminho_dados (str): Caminho do arquivo CSV contendo os dados.
        dados (pd.DataFrame): DataFrame para armazenar os dados carregados.

    Methods:
        carregar_dados: Tenta carregar os dados do arquivo CSV. Exibe uma mensagem de erro se o arquivo não for encontrado.
        verificar_valores_nulos: Verifica a presença de valores nulos nos dados carregados.
        calcular_receita: Calcula a receita para cada veículo e a receita total.
        criar_tabela: Cria um DataFrame com as informações de receita, formata e visualiza a tabela.
    """

    def __init__(self, caminho_dados: str):
        """
        Inicializa a instância da classe.

        Args:
            caminho_dados (str): Caminho do arquivo CSV contendo os dados.
        """
        self.caminho_dados = caminho_dados
        self.dados = None

    def carregar_dados(self) -> None:
        """
        Tenta carregar os dados do arquivo CSV. Exibe uma mensagem de erro se o arquivo não for encontrado.
        """
        try:
            self.dados = pd.read_csv(self.caminho_dados)
        except FileNotFoundError:
            print(f'O arquivo {self.caminho_dados} não foi encontrado. Verifique o caminho.')

    def verificar_valores_nulos(self) -> None:
        """
        Verifica a presença de valores nulos nos dados carregados.
        """
        if self.dados is not None and self.dados.isnull().any().any():
            print('Existem valores nulos nos dados. Considere tratá-los antes de prosseguir.')

    def calcular_receita(self) -> pd.DataFrame:
        """
        Calcula a receita para cada veículo e a receita total.

        Returns:
            pd.DataFrame: DataFrame contendo o nome do veículo e sua respectiva receita.
        """
        self.dados['receita'] = self.dados['vendas'] * self.dados['valor_do_veiculo']
        receita_por_veiculo = self.dados.groupby('nome')['receita'].sum()
        receita_por_veiculo = receita_por_veiculo.sort_values(ascending=False)
        return pd.DataFrame({
            'Nome do Veículo': receita_por_veiculo.index,
            'Receita (R$)': receita_por_veiculo.values
        })

    def criar_tabela(self) -> None:
        """
        Cria um DataFrame com as informações de receita, formata a tabela e a visualiza.
        """
        tabela_receita = self.calcular_receita()

        # Formatar a coluna 'Receita (R$)' para moeda brasileira
        tabela_receita['Receita (R$)'] = tabela_receita['Receita (R$)'].map('{:,.2f}'.format)

        # Calculando o total
        total_receita = tabela_receita['Receita (R$)'].str.replace(',', '').astype(float).sum()

        # Formatar todos os valores da coluna 'Receita (R$)' sem o prefixo 'R$'
        tabela_receita['Receita (R$)'] = tabela_receita['Receita (R$)'].replace('[\$,]', '', regex=True).astype(float).map('{:,.2f}'.format)

        # Adicionando uma linha com o total ao DataFrame
        tabela_receita.loc[len(tabela_receita)] = ['Total', '{:,.2f}'.format(total_receita)]

        # Criando uma figura e eixo para a tabela
        fig, ax = plt.subplots(figsize=(16, 8))
        ax.axis('off')  # Desativando os eixos

        # Criando a tabela
        table_data = [list(row) for _, row in tabela_receita.iterrows()]

        # Criando uma escala de cinza para as células da tabela
        gray_cmap = LinearSegmentedColormap.from_list('gray_cmap', ['#F0F0F0', '#D9D9D9', '#C0C0C0'])

        # Adicionando a tabela ao eixo
        table = ax.table(cellText=table_data, colLabels=tabela_receita.columns, cellLoc='center', loc='center', bbox=[0, 0, 1, 1])

        # Estilizando a tabela com design moderno em tons de cinza
        table.auto_set_column_width([0, 1])
        table.set_fontsize(10)
        table.scale(2, 2)

        # Iterando sobre as células da tabela
        for i, key in enumerate(table._cells):
            cell = table._cells[key]
            if i >= 0:  # Ignorando o cabeçalho
                cell.set_facecolor(gray_cmap(i % gray_cmap.N))
                cell.set_edgecolor('white')

        # Adicionando uma borda à tabela
        ax.add_table(table)
        plt.savefig('tabela_receita.png')
        plt.show()

def main():
    """
    Função principal para executar o exemplo de uso da classe TabelaReceita.
    """
    caminho_dados = 'Dataset/dados_cleaned.csv'
    tabela = TabelaReceita(caminho_dados)
    tabela.carregar_dados()
    tabela.verificar_valores_nulos()
    tabela.criar_tabela()

if __name__ == "__main__":
    main()

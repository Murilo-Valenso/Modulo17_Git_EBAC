
import pandas as pd
import seaborn as sns

fonte_df = pd.read_csv('gasolina.csv', sep=',')
fonte_df

with sns.axes_style('whitegrid'):

  grafico = sns.lineplot(data=fonte_df, x="dia", y="venda", palette="pastel")
  grafico.set(title='Preço da Gasolina por Dia', xlabel='Data', ylabel='Valor');
  grafico.get_figure().savefig(f"gasolina.png")

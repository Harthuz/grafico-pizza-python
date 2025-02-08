import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('Gastos e ganhos planilha - Respostas ao formulário 1.csv', delimiter=',')

# Verifique as primeiras linhas do arquivo CSV para entender sua estrutura
print(df.head())

# Substituir a vírgula por ponto e converter para numérico
df['Valor'] = df['Valor'].str.replace(',', '.').astype(float)

# Filtrar os dados para remover as categorias "Pix" e "Dinheiro"
df_filtrado = df[~df['Categoria'].isin(['Pix', 'Dinheiro'])]

# Agrupar os valores por categoria e somar os valores
df_categoria = df_filtrado.groupby('Categoria')['Valor'].sum()

# Gerar o gráfico de pizza
plt.figure(figsize=(8, 8))

# Criar gráfico de pizza
df_categoria.plot.pie(autopct='%1.1f%%', startangle=90, legend=False, figsize=(8, 8))

# Personalização do gráfico
plt.title('Distribuição de Categorias (Ignorando Pix e Dinheiro)')

# Exibir o gráfico
plt.tight_layout()
plt.show()

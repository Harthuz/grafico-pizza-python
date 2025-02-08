# Gráfico de Pizza - Análise de Gastos e Ganhos

Este projeto gera um gráfico de pizza que mostra a distribuição de categorias de gastos e ganhos a partir de uma planilha CSV. O gráfico considera apenas as categorias diferentes de **Pix** e **Dinheiro**, que são ignoradas no cálculo. O gráfico exibe a porcentagem de cada categoria após agrupar os valores por categoria.

## Objetivo

O objetivo deste script é ajudar a visualizar a distribuição dos gastos e ganhos categorizados em uma planilha CSV, permitindo uma análise rápida dos dados financeiros, excluindo transações de "Pix" e "Dinheiro".

## Funcionalidade

- **Filtragem**: Exclui as categorias "Pix" e "Dinheiro".
- **Agrupamento**: Agrupa os dados por categoria e soma os valores.
- **Visualização**: Gera um gráfico de pizza com a porcentagem de cada categoria, considerando os dados filtrados e agrupados.

## Como Usar

### Requisitos

- **Python 3.x**
- **Pandas**
- **Matplotlib**

Você pode instalar as dependências com o seguinte comando:

```bash
pip install pandas matplotlib
```

### Passos para rodar o script

1. **Prepare sua planilha CSV**: O arquivo CSV deve ter pelo menos as colunas `Categoria` e `Valor`, onde "Valor" representa o valor financeiro (com vírgula como separador decimal).
   
2. **Substitua o caminho do arquivo**: No script, substitua o nome do arquivo `'Gastos e ganhos planilha - Respostas ao formulário 1.csv'` para o caminho correto do seu arquivo CSV.

3. **Execute o script**:
   
   ```bash
   python graficoPizza.py
   ```

4. **Visualização**: Após a execução, o gráfico de pizza será exibido com a distribuição das categorias, excluindo "Pix" e "Dinheiro".

## Como Funciona

- **Leitura do CSV**: O arquivo CSV é carregado usando a biblioteca **pandas**.
- **Conversão de Valores**: A coluna `Valor` é processada para garantir que os números sejam tratados corretamente, substituindo a vírgula por ponto.
- **Filtragem de Dados**: As categorias "Pix" e "Dinheiro" são removidas dos dados.
- **Agrupamento**: Os valores são somados por categoria.
- **Geração do Gráfico**: Um gráfico de pizza é gerado usando **matplotlib**, mostrando a distribuição das categorias e suas respectivas porcentagens.

## Exemplo de Saída

Ao executar o script, será gerado um gráfico de pizza, onde cada fatia representa uma categoria, e o gráfico será exibido com a porcentagem correspondente a cada uma delas.

---

### Exemplo de Entrada CSV

| Carimbo de data/hora    | Data       | Categoria | Descrição | Tipo   | Valor | Saldo total | Coluna 1 |
|-------------------------|------------|-----------|-----------|--------|-------|-------------|----------|
| 01/02/2025 15:02:17     | 01/02/2025 | Pix       | Saldo inter | Ganho  | 74,13 | 74,13       |          |
| 02/02/2025 10:30:22     | 02/02/2025 | Aluguel   | Mensalidade | Gasto  | 300,00 | 374,13      |          |
| 02/02/2025 16:15:45     | 02/02/2025 | Restaurante | Jantar    | Gasto  | 45,00 | 329,13      |          |

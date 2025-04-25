import pandas as pd

df = pd.read_csv('jessica/dados.csv')

print('Dados iniciais:')
print(df.head())

filtro_idade = df[df['idade'] > 25]
print("\nPessoas com mais de 25 anos:")
print(filtro_idade)

df_ordenado = df.sort_values(by='idade', ascending=False)

df_ordenado.to_csv('jessica/dados_processados.csv', index=False)

print("\nArquivo 'dados_processados.csv' gerado com sucesso!")
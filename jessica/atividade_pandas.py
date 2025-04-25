import pandas as pd

df = pd.read_csv(r'jessica\dados_ficticios.csv')

 
if 'idade' in df.columns and 'renda' in df.columns:
        
        pessoas_maior_40 = df[df['idade'] > 40]

        # Filtra as pessoas com renda maior que 5 mil
        pessoas_renda_maior_5mil = df[df['renda'] > 5000]

      
        df_ordenado_idade = df.sort_values(by='idade', ascending=False)
        df_ordenado_renda = df.sort_values(by='renda', ascending=False)
    
       
        df_ordenado_idade.to_csv('jessica/pessoas_maior_40.csv', index=False)
        df_ordenado_renda.to_csv('jessica/pessoas_renda_maior_5mil.csv', index=False)

        print("Pessoas com idade maior que 40:")
        print(pessoas_maior_40)

        print("\nPessoas com renda maior que 5 mil:")
        print(pessoas_renda_maior_5mil)
else:
        print("Colunas 'idade' e/ou 'renda' não encontradas no arquivo.")
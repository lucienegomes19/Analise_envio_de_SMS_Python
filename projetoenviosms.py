import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "XXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console
auth_token  = "XXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

lista_preco = ['janeiro', 'fevereiro', 'marco', 'abril']

for mes in lista_preco:


    tabela_precos = pd.read_excel(f'{mes}.xlsx')


    if (tabela_precos['Valor']> 250).any():
        produtos = tabela_precos.loc[tabela_precos['Valor'] > 250, 'Produtos'].values[0]
        valor = tabela_precos.loc[tabela_precos['Valor'] > 250, 'Valor'].values[0]
        print(f' No mês de {mes}, o produto com maior valor agregado foi: Produto: {produtos}, Valor: {valor}')
        message = client.messages.create(
            to="+55XXXXXXXXX",
            from_="XXXXXXXXXXXXXX",
            body=f' No mês de {mes}, o produto com maior valor agregado foi: Produto: {produtos}, Valor: {valor}')

        print(message.sid)



#bibliotecas usadas: pandas, openpyxl, twilio
import pandas as pd
from twilio.rest import Client
#passo a passo solução

#abrir 6 arquivos em Excel

#para cada arquivo:
#verificar se algum valor na coluna de vendas é +55.000

#se for maior que 55.000 -> envia sms com o: Nome, mês e vendas do vendedor

#caso não seja maior que 55.000 não quero fazer nada

account_sid = "AC3fbd3c3fcdc7353f528baf2884f932a3"
auth_token = "a3b2c666718f29ed6ab803c2c7e7f119"

client = Client(account_sid, auth_token)

lista_meses = ["janeiro","fevereiro","março","abril","maio","junho"]

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f"{mes}.xlsx")
    if (tabela_vendas["Vendas"] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela_vendas.loc[tabela_vendas["Vendas"] > 55000, "Vendas"].values[0]
        print(f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}")
        message = client.messages.create(
            #adicionar número
            to="whatsapp:+55xxxxxxxxx",
            from_="whatsapp:+14155238886",
            body=f"No mês {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas:{vendas}")
        print(message.sid)
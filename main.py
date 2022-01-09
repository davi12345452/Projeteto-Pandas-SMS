import pandas as pd
from twilio.rest import Client

# O "as pd" simplfica a nomeclatura pandas no có-
# digo, ao invés de escrever pandas, escreve pd

# Solução do problema: programa que identifique
# quando o primeiro vendedor atingir R$55000.00
# em vendas em um único mês, parando a pesquisa
# e mandando um SMS para mim

# A primeira coisa que fiz, foi abrir as plani-
# lhas de Excel dos 6 meses de vendas

# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token = ""
client = Client(account_sid, auth_token)

meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho"]

for mes in meses:
    tabela = pd.read_excel("{}.xlsx".format(mes))

# Para cada um dos 6 arquivos, identificar se
# houveram valores > que 55.000 na coluna ven-
# das.

    if (tabela["Vendas"] > 55000).any():
        vendedor = tabela.loc[tabela["Vendas"] > 55000, "Vendedor"].values[0]
        vendas = tabela.loc[tabela["Vendas"] > 55000, "Vendas"].values[0]


# Se houver um valor > 55000, enviar um SMS
# para um número de telefone, indicando o ven-
# dedor e o valor da venda.

        message = client.messages.create(
            to="", #Aqui você coloca o seu número de telefone
            from_="+16093364135",
            body="No mes de {}, o vendedor(a) {} obetve\n"
              "uma receita de R${:.2f}".format(mes, vendedor, vendas))
        print(message.sid)

# Se não houver alguma venda acima de 55000,
# não fazer nada

    else:
        break


import pandas as pd
import numpy as np
#Importando o dataset
url = '##########'
df = pd.read_csv('./TODOS-googlex.csv', encoding="UTF-8")
df.head()
#Deletando as colunas desnecessarias
df = df.drop(columns=['NOME DA MÃE','UNIDADE','LOTAÇÃO','TELEFONE','E-mail','FUNÇÃO'])
#Trocando os nomes das colunas
df = df.rename(columns={'Nome completo:': 'Name','Código do líder:': 'Family Name', 'Contatos (Telefone Celular):': 'Phone','Escola onde vota:':'Observação'})
#Mudando as posições das colunas 
df = df[[u'Name',u'Family Name',u'Phone',u'Observação']]
#Fazendo uma manipulação de string de uma coluna inteira
df2 = df['Family Name'].str.upper()
#Atribuindo o valor da df2 para df
df['Family Name'] = df2
#alterando string de varias linhas de uma coluna com numeros por tamannho
def alterandoStringDeUmaColuna(param):
  altera = param
  lista = []
  for i in range(len(altera)):
    if len(altera[i]) == 8:
      lista.append('9'+altera[i])
    else:
      lista.append(altera[i])
  return lista
a = alterandoStringDeUmaColuna(df['Phone'])
df['Phone'] = a
#Mexendo na capitalização das strings
alterandoString = df[u'Name'].str.title()
df['Name'] = alterandoString
#Manipulando duas colunas para concatenação
nova = []
for i in range(len(df2)):
  nova.append(f"{alterandoString[i]} - {df2[i]}")
df[u'Name'] = nova
df = df.drop(columns=['Family Name'])
df.to_csv(r'ultimaversao.csv', header=True, index=False, encoding='latin')
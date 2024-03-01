# NUMPY #
print('>>>> NUMPY <<<<\n\n')

# 1) Importar biblioteca
import numpy as np

# 2) Criando arrays:

arr = np.array([1, 2, 3, 4, 5])
arr = np.array((1, 2, 3, 4, 5))

# 3) Indexing e Slicing
print('\n3) Indexing e Slicing')
print(arr[1:3])
print(arr[1])
print(arr[:3])



# 4) Iteração em um Numpy array
print('\n4) Iteração em um Numpy array')

# a)
print('\na)')
arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])

quantidadeElementos = len(arr)

soma = 0

for elemento in arr:
  soma = soma + elemento
  
media = soma/quantidadeElementos
print('Media: ',media)

# b)
print('\nb)')
somaDesvio = 0
for elemento in arr:
  somaDesvio = somaDesvio + (elemento - media)**2

desvioPadrao = (somaDesvio/quantidadeElementos)**(1/2)
print('Desvio Padrão: ',desvioPadrao)
      
# 5) Funções facilitadoras
print('\n5) Funções facilitadoras')
# a)
print('\na)')
arr = np.array([5.5, 3.8, 9, 7.5, 10.0, 9.9, 8.5])
arr = np.sort(arr)

print('Array com método sort(): ',arr)

# b)
print('\nb)')
dimensao = np.shape(arr)
print('Dimensao: ',dimensao)

# c)
print('\nc)')
media = arr.mean()
print('Media:', media)

# d)
print('\nd)')
desvioPadrao = arr.std()
maximo = arr.max()
minimo = arr.min()

print('Desvio Padrao: ',desvioPadrao)
print('Máximo: ',maximo)
print('Mínimo: ',minimo)

# e)
print('\ne)')
from numpy import random

arr = random.randint(11, size=(100))
print(arr)

media = arr.mean()
desvioPadrao = arr.std()
valorMaximo = arr.max()
valorMinimo = arr.min()

print('Media: ',media)
print('Desvio Padrão: ',desvioPadrao)
print('Maior Valor: ',valorMaximo)
print('Menor Valor: ',valorMinimo)

# PANDAS #
print('\n>>>> PANDAS <<<<')
print('\n\n')


# 1)

import pandas as pd
dados = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica.csv')

# 2) 
print('\n2)')
dados
print(dados)

# 3)
print('\n3)')
selecaoAno = dados['ano'] == 1991
dadosSelecionados = dados[selecaoAno]
valoresIDH = dadosSelecionados['idhm']

media = valoresIDH.mean()
print('IDH médio do brasil no ano de 1991: ', media)

# 4)
print('\n4)')
selecaoMedia = dadosSelecionados['idhm'] > media
dadosSelecionados2 = dadosSelecionados[selecaoMedia]
estadosPedidos = dadosSelecionados2['sigla_uf']
estadosPedidos = estadosPedidos.reset_index(drop=True)

df = pd.DataFrame(
    {
        "estados_acima_da_media": estadosPedidos
    }
)

print(df)

print('\n Os estados que estão a cima da média são:')

for indice in estadosPedidos.index:
  print(estadosPedidos[indice])

# 5)
print('\n5)')
dadosSelecionadosOrdenados = dadosSelecionados.sort_values('idhm')
print(dadosSelecionadosOrdenados.head(5))

# 6)
print('\n6)')
maiorValor = dadosSelecionados['idhm'].max()
menorValor = dadosSelecionados['idhm'].min()
indiceMaiorValor = dadosSelecionados['idhm'].idxmax()
indiceMenorValor = dadosSelecionados['idhm'].idxmin()
estadoMaior = dadosSelecionados['sigla_uf'][indiceMaiorValor]
estadoMenor = dadosSelecionados['sigla_uf'][indiceMenorValor]

print('Estado com maior IDH:',estadoMaior, '| Valor IDH: ', maiorValor)
print('Estado com menor IDH:',estadoMenor, '| Valor IDH: ', menorValor)

# MATPLOTLIB #
print('\n>>>> MATPLOTLIB <<<<')
import matplotlib.pyplot as plt

# 1) Qual a proporção da População Urbana entre os estados brasileiros?
print('\n 1) Proporção da População Urbana entre os estados brasileiros')
x = dadosSelecionados['sigla_uf']
y = dadosSelecionados['populacao_urbana'].sort_values()

plt.figure(figsize=(10,6))
plt.bar(x,y, color = "hotpink" )
plt.title('Polulacão Urbana por estado em 1991')
plt.xlabel('ESTADOS')
plt.ylabel('POPULAÇÃO')

plt.show()

print(' Análise: Podemos notar que o estado do Tocantis possui disparado a maior taxa de populção urbana nesse ano.\
      Alguns outros estados, como DF, ES, GO, MA, MG, MS, MT, possuem valores muito semelhantes.\
      Outros possuem taxas extremamentes baixas.\
      Dependendo da análise, o estado TO poderia ser analisado separadamente já que está muito distante dos demais. \
      Para uma análise melhor alguns dados poderiam ter sidos mesclados.')

# 2) Qual o nível de desigualdade do Brasil?
print('\n 2) Nível de desigualdade do Brasil')

dadosPorAnos = dados.groupby('ano')
valoresIDH = dadosPorAnos['idhm']

for ano, valores in valoresIDH:
  plt.figure()
  plt.hist(valores, color = "hotpink")
  plt.title(ano)
  plt.xlabel('IDH')
  plt.ylabel('FRQUÊNCIA')
  plt.show()

print(' Análise: Podemos notar que em 1991 temos altas quantidades de estados com IDHS muito baixos, menores que 0.5.\
      Em 2000 já houve um aumento nos valores dos IDH e ficaram mais distribuidos os estados pelos novos valores. \
      Em 2010 houve um aumento muito significativo e boa parte dos estados estão com valores de IDH ente 0.630 e 0.750 (bem altos comparados ao priemiro ano)\
      Um IDH mais alto indica um melhor padrão de vida geral, o que geralmente está associado a uma menor desigualdade entre os habitantes.\
      Logo, podemos concluir que a desigualde diminuiu no Brasil comparando com anos anteriores.')

# 3)Existe alguma correlação entre IDH e Expectativa de Vida?
print('\n 3) Correlação entre IDH e Expectativa de Vida')
x = dados['idhm']
y = dados['expectativa_vida']

plt.scatter(x, y,color = "hotpink")
plt.title('IDH e expectativa de vida')
plt.xlabel('IDH')
plt.ylabel('EXPECTATIVA DE VIDA')

plt.show()

print('  Análise: Podemos notar que com o aumento do IDH também há um aumento na expectativa de vida. \
\n Os pontos estão tendendo a ficar alinhados, tendendo a uma reta. \
\n Não há nenhum ponto com uma dispersão muito grande em relação aos demais \
\n Então, existe uma relação direta e positiva entre as duas medidas.')

# DESAFIO FINAL # 

print('\n >>>> DESAFIO FINAL <<<< \n\n')

# Obtendo a diferença de expectativa de vida entre 1991 e 2010 para cada estado
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv('Dataset_Processo_Seletivo_UFRJ_Analytica.csv')

selecaoAno1 = dados['ano'] == 1991
dadosSelecionados1991 = dados[selecaoAno1]

selecaoAno2 = dados['ano'] == 2010
dadosSelecionados2010 = dados[selecaoAno2]
dadosSelecionados2010 = dadosSelecionados2010.reset_index(drop=True)


estados = []
diferencas = []

for indice in dadosSelecionados1991.index:
  diferenca = dadosSelecionados2010['expectativa_vida'][indice] - dadosSelecionados1991['expectativa_vida'][indice]
  estado = dadosSelecionados1991.loc[indice, 'sigla_uf']
  estados.append(estado)
  diferencas.append(diferenca)

estados = np.array(estados)
diferencas = np.array(diferencas)

print('Estados: ',estados)
print('\n')
print('Diferença: ', diferencas)

# Fazendo um gráfico de barras:
df = pd.DataFrame(
    {
        "estado":estados,
        "dif_expect_vida":diferencas
    }
)

x = df['estado']
y = df['dif_expect_vida']

plt.figure(figsize=(10,6))
plt.bar(x,y, color = "hotpink" )
plt.title('Diferenca da expectativa de vida entre os anos de 1991 e 2010 por estado')
plt.xlabel('ESTADOS')
plt.ylabel('DIFERENÇA')

plt.show()

print('\n Podemos notar que alguns estados como PB, MA, AL tiveram maiores valores de diferença.\
      Logo, a expectativa de vida aumentou mais significamente nesses estados.\
      Estados como RS, SC, SP tabém tiveram suas expectativas de vida aumentadas, \
      porém com uma diferença do ano de 2010 para o de 1991 menor se comparado aos demais.\n')

# Retornando todos os estados que tiveram um aumento de pelo menos 10 anos na expectativa de vida entre 1991 e 2010.

selecaoVida = df['dif_expect_vida'] >= 10
selecaoVida = df[selecaoVida]
estadosPedidos = selecaoVida['estado']
estadosPedidos = estadosPedidos.reset_index(drop=True)
df = pd.DataFrame(
    {
        "estados_com_aumento": estadosPedidos
    }
)

print(df)
print('\n')

print('Os estados com expectativa de vida maior que 10 anos são:')

for indice in estadosPedidos.index:
  print(estadosPedidos[indice])


print('\n\nFim!\n\n')
#Lista: Crie uma estrutura de repetição para fazer a leitura de 5 números inteiros
# e os armazene dentro de uma lista. Após a leitura, crie outra estrutura de repetição
# para somar todos os valores digitados

lista=[]
numero=0

print(list)
for i in range(1,6):
    numero=float(input("insira: um numero: "))
    lista.insert(i-1,numero)

print("lista",lista)

resultado=0
for numero in lista:
    resultado +=numero


print("a soma da lista é:",resultado)

#Dicionário: Crie um dicionário para armazenar o nome e a nota de 3 alunos,
# fazendo a leitura dos valores por meio de uma estrutura de repetição.
# Depois, crie uma nova estrutura de repetição para somar todas as notas e
# retornar a média


map={}
aluno=""
nota=0

for i in range(1,4):
   aluno= input("Insira o nome do aluno: ")
   nota=float(input(f"Insira a nota do aluno {aluno}"))
   map.update({aluno:nota})


soma=0
for nota in map.values():
    soma +=nota

print("a média da sala é:",soma/len(map))

#Matriz: Dada a matriz abaixo, construa uma estrutura de repetição para
# percorrer e somar todos os elementos da matriz

import numpy as np

matriz=np.array([[3,4,1],
                 [3,1,5]])

soma=0

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        soma +=matriz[i][j]


print(soma)
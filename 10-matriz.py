#Matriz
import numpy as np

matriz=np.array([[2,3,4],
                [4,5,7]])

print(matriz)

#exibição:(2,3)=>2 linhas 3 colunas
print(matriz.shape)

#printa a primeira linha
print(matriz[0])

#printa a segunda linha
print(matriz[1])

#linha 0 coluna 2
print(matriz[0][2])

#linha 1 coluna 2
print(matriz[1][2])

#printo as linhas no primeiro for,
#no segundo for eu printo as colunas

for i in range(matriz.shape[0]):
    print(f"print da linha {i+1}", matriz[i])
    print(f"print da coluna {i + 1}: ")
    for j in range(matriz.shape[1]):
        print(matriz[i][j])


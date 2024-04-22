#Tuplas
#tuplas são imutáveis
tupla=('Homo sapiens', 'Canis familiaris', 'Felis catus')

#printa a posição 0 da tupla
tupla[0]

#printa a posição de 'Canis familiaris' na tupla
tupla.index('Canis familiaris')

for elemento in tupla:
    print(elemento)


#Listas
#as listas podem ser mutáveis

l1=['Homo sapiens', 'Canis familiaris', 'Felis catus']
l2 = ['Xenopus laevis', 'Ailuropoda melanoleuca']

l2

#replica os dados da lista 2 vezes
l2_2=l2 *2
print(l2_2)

l1[0]

l1

#retorna as 2 primeiras posições da lista
print(l1[0:2])

#adiciona 'Gorila gorila' a lista
l1.append('Gorila gorila')
print(l1)

#remove o dado 'Felis catus'
l1.remove('Felis catus')
print(l1)

#deleta a lista
del(l1)

print(l1)

for item in l2_2:
    print(item)

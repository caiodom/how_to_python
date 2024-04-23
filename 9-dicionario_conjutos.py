#Dicionários
coleta={'Aedes aegypt':32,'Aedes albopictus':22, 'Anopheles darlingi':14}

#retorna o valor a partir da chave
coleta['Aedes aegypt']

#adicionando uma chave/valor no dicionario
coleta['Rhodnius montenegrensis']=11
print(coleta)

#remove o dado de chave 'Aedes albopictus' do dicionario
del(coleta)['Aedes albopictus']
print(coleta)

#retorna os dados do dicionario
coleta.items()

#retorna as chaves do dicionario
coleta.keys

#retorna os valores do dicionario
coleta.values()

coleta2 = {'Anopheles gambiae': 13, 'Anopheles deaneorum': 14}
print(coleta2)

coleta.update(coleta2)
print(coleta)

#adiciona um dicionario dentro de outro dicionario
coleta.update(coleta2)
print(coleta)

coleta.items()

    #chave  #valor
for especie,num_especimes in coleta.items():
    print(f'Espécie: {especie}, número de espécimes coletados: {num_especimes}')



#Conjuntos
biomoleculas=('proteína', 'ácidos nucleicos', 'carboidrato', 'lipídeo',
                'ácidos nucleicos', 'carboidrato', 'carboidrato', 'carboidrato')

print(biomoleculas)


print(set(biomoleculas))

#Intersecção dos conjuntos
c1={1,2,3,4,5}
c2={3,4,5,6,7}
c3=c1.intersection(c2)

print(c3)

#diferença
c1.difference(c2)

c2.difference(c1)




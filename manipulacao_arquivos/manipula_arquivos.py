
#nomeio o arquivo como tex
#r=read
with open('./frase1.txt','r') as tex:
    for linha in tex:
        print(linha)

#colocando as linhas em uma variável
with open('./frase1.txt') as tex:
    r=tex.readlines()

print(r)


#criando um texto
#w=write
with open('./texto2.txt','w') as texto:
    texto.write('Olá a todos')

#lendo o novo texto criado
with open('./texto2.txt','r') as texto_criado:
    for linha in texto_criado:
        print(linha)
a='casaco'
print(a)

#maiúscula
maiuscula=a.upper()
print(maiuscula)

#minúscula
minuscula=maiuscula.lower()
print(minuscula)

#capitalization
capital=a.capitalize()
print(capital)

#metade da palavra
metade_palavra=a[0:4]
print(metade_palavra)

#ultimas 3 letras
ultimas_letras=a[3:]
print(ultimas_letras)

#string replace
b=a.replace('aco','inha')
print(a)
print(b)

c=a.replace('o','a')
print(c)


#procura posição do caractere
posicao=c.find('s')
print(posicao)

#tamanho da string
sem_espaco='casaco'
print(len(sem_espaco))

com_espaco=' casaco '
print(len(com_espaco))

#remove o espaçamento inicial e final
espacados = '   casaco    '
print(len(espacados.strip()))

#interpolação strings
n1=14
n2=16
print(f'Dividindo {n1} por {n2} o resultado é: {n1/n2}')



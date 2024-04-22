nota=media=soma=0
print(nota,media,soma)
for _ in range(1,6):
    nota = float(input('Digite a nota: '))
    soma += nota

print(soma)
media = soma/5
print('A média é:',media)

nota=soma=0
numero=1
while numero<=5:
    nota = float(input('Digite a nota: '))
    soma+=nota
    numero +=1
print('A média é:',soma/5)

#imprimir tabuada numero 3 com for
numero=3
resultado=0
for multiplicador in range(1,11):
    print(f" 3 x {multiplicador}=",3*multiplicador)
print()

#imprimir tabuada numero 3 com while
numero=1
while(numero<=10):
    print(f" 3 x {numero}=", 3 * numero)
    numero += 1


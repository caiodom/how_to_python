nota=media=soma=0
print(nota,media,soma)
for _ in range(1,6):
    nota = float(input('Digite a nota: '))
    soma += nota

print(soma)
media = soma/5
print('A média é:',media)
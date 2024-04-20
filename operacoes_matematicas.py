a=5
b=3

print(a,b)

#soma
a+b
print('A soma é',a+b)

#subtração
print('a subtração é',a-b)

#divisão
print('a divisão é',a/b)

#multiplicação
print('A multiplicação é',a*b)

#resto divisão
print('O resto da divisão é',10 % 3)

#exponenciação
print('5 elevado a 4 é',5**4)

#raiz quadrada
#importante o import da lib math
import math
raiz_quadrada=math.sqrt(81)
print('A raiz quadrada de 81 é:',raiz_quadrada)

#arredondamento
casos_doenca=134
numero_habitantes=34432
casos_por_habitante=casos_doenca/numero_habitantes
print('Casos por habitantes arredondado por 6:',round(casos_por_habitante,6))
print('o número de casos por habitante é de',round(casos_por_habitante,4))


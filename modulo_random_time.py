#Biblioteca random

import random

#random
print("random",random.random())

#int random em uma faixa
print("inteiro random em uma faixa",random.randint(1,10))

#random em uma faixa por passo (par)
print("random em uma faixa por passo",random.randrange(0,10,2))

#random em uma faixa por passo (impar)
print("random em uma faixa por passo",random.randrange(0,10,2))

#escolha entre uma lista
x = ['K', 'd', 13, '34-j', 'x']

print(random.choice(x))

#Biblioteca time
import time as tm

#retorna o tempo atual em segundos
print("time",tm.time())

#medindo tempo de execução de um código
antes=tm.time()
lista=[]
for i in range(0,100000):
    lista.append(i)

depois=tm.time()

print(f"o intervalo de execução foi {depois-antes} segundos")


#para a execução por segundos
print('Finalizando...')
tm.sleep(2)
print('...')
tm.sleep(2)
print('Até a próxima')




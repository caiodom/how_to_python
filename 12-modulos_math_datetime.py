#Biblioteca math
import math

#raiz quadrada
print("raiz quadrada de 9",math.sqrt(9))

#seno
print("seno de 45",math.sin(45))

#cosseno
print("cosseno de 45",math.cos(45))

#logaritmo
print("logaritmo 1000 10",math.log(1000,10))
print("logaritmo 32 2",math.log(32,2))
# utiliza o numero de Euler quando nao passa a base
print("logaritmo 1000 euler",math.log(1000))

#número de Euler
print("número de Euler",math.e)

#PI
print("pi",math.pi)


#Biblioteca DateTime
import datetime

#mostra os recursos disponiveis na biblioteca
print("recursos disponiveis lib datetime",dir(datetime))

#mostra a data de hoje
print("data de hoje",datetime.date.today())

#mostra a data de agora
print("data de agora",datetime.datetime.now())

#formatador data
data = datetime.date(2020, 7, 10)
print("data formatada",data)

#dia
print("dia",data.day)

#mes
print("mes",data.month)

#ano
print("ano",data.year)

#horario
horario = datetime.datetime(2020, 7, 10, 7, 30, 0)
print("horario formatado",horario)

#hora
print("hora",horario.hour)

#minutos
print("minutos", horario.minute)

#segundos
print("segundos",horario.second)





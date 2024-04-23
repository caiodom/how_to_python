#Funções sem parametro e sem retorno
def mensagem():
    print("Texto da funçao")

mensagem()

#Função com passagem de parâmetro
def mensagem(texto):
    print(texto)

mensagem("meu texto 1")
mensagem("meu texto 2")
mensagem("meu texto 3")


def soma(a,b):
    print(a+b)

soma(2,3)

#Função com passagem de parâmetros e retorno
def soma(a,b):
    return a+b

r=soma(3,2)
print(r)

#função documentada
def calcula_energia_potencial_gravitacional(m, h, g = 10):
  '''
  Calcula a energia potencial gravitacional
  Argumentos:
  m: massa, entrada como uma variável float
  h: altura, entrada como uma variável float

  Argumento opcional:
  g: aceleração gravitacional, com valor default de 10
  '''
  e = g * m * h
  return e

print(calcula_energia_potencial_gravitacional(30, 12))

#mostra a documentação da função
help(calcula_energia_potencial_gravitacional)
import utilitarios as ut

print(ut.soma(1, 2, 3))
print(ut.mult(3, 2, 2))
print(ut.isPalindromo('abc'))
print(ut.isPalindromo('abccba'))

t = 'abccba'
#acessamos a posicao da string com o -1 indicando que é ao contrario assim invertendo
#a string
print(t[::-1])

t1 = 'abc'
print(t1[::-1])

print(ut.divisao(10,2))
from triangulo import Triangulo
from aluno import Aluno

t1 = Triangulo(5, 1, 3, 4, 3)

print(t1.lado1, t1.lado2, t1.lado3, t1.base, t1.altura)
print(t1.area())
print(t1.tipo())

t2 = Triangulo(8, 8, 8, 16, 9)
print(t2.lado1, t2.lado2, t2.lado3, t2.base, t2.altura)

print(t2.area())
print(t2.tipo())


aluno1 = Aluno('Pedro', 7.0, 9.0)
media = aluno1.calcula_media()
print(media)

aluno1.mostra_dados()
aluno1.resultado()

aluno2 = Aluno('João', 7.0, 2.0)
media = aluno2.calcula_media()
aluno2.mostra_dados()
aluno2.resultado()
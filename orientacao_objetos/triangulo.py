class Triangulo:

  #self:O self no Python é uma palavra-chave utilizada para referenciar a própria instância de uma classe.
  # o self é utilizado para acessar os atributos e métodos de um objeto em particular.
  # Ele é semelhante ao “this” em outras linguagens de programação, como o Java.
  def __init__(self, lado1, lado2, lado3, base, altura):
    self.lado1 = lado1
    self.lado2 = lado2
    self.lado3 = lado3
    self.base = base
    self.altura = altura

  def area(self):
    return (self.base * self.altura) / 2

  def tipo(self):
    if self.lado1 > self.lado2 + self.lado3:
      return 'não é um triângulo'
    elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado1 == self.lado2:
      return 'triângulo isósceles'
    else:
      return 'outro tipo de triângulo'
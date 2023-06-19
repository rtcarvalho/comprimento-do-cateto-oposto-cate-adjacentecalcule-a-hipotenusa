print('Faça um programa que leia o comprimento do cateto oposto e do cate adjacente de um triangulo retangulo,'
      ' calcule e mostre o comprimento da hipotenusa')

import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)

print('A hipotenusa mede {:.2f}'.format(hi))


# Segunda fora
from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
hi = hypot(co, ca)

print('A hipotenusa mede {:.2f}'.format(hi))
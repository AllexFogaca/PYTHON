"""

01 - área de um retângulo
02 - área de um quadrado
03 - se o produto que você quer avaliar custa (??) reais qual o valor
do mesmo com desconto de (??)%
04 - área de um circulo - pi = 3,141592
05 - conversão de reais em dolar
06 - conversão de dolar em reais

"""

# 01

print("Calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("qual o tamanho da altura do seu retangulo? ")

area = float(base) * float(altura)

print(f'O seu retangulo possui area : {area} ')


# 02

print('Calcule a area de um quadrado')

y = input("Qual o tamanho do seu quadrado? ")


x = float(y) ** 2

print(f'A area do seu quadrado é de: {x}')

# 03


valor = input('Qual valor do seu produto: ')
desconto = input('Qual o desconto: ')

porcentagem = float(desconto) / 100
valor_desconto = porcentagem * float(valor)
total = float(valor) - valor_desconto

print(f'O produto agora custa {total}')

# 04

print('calcule a area de um circulo')

raio = input('digite o raio do circulo: ')

pi = 3.14
area_circulo = pi * (float(raio)**2)

print(f'A area do circulo é de {area_circulo}')

# 05

print('Converta real em dolar')

real = input('Quanto voce tem na sua conta ? ')

dolar = float(real) / 5.17

print(f'Voce possui {dolar} dollars')


# 06

print('Converta dolar em real')

doll = input('How much do u have in you account? ')

reais = float(doll) * 5.17

round(reais, 2)

print(f'U have {reais} reais')

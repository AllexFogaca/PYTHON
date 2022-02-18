"""
01 - Implemente um programa que receba a idade de uma pessoa e imprima
mensagem de acordo com os criterios

menor de 16 anos: MENOR
Entre 16 e 18 anos: EMANCIPADO
Maior de 18 anos: MAIOR

02 - implemente um programa que receba a idade de um nadador
e imprima a sua categoria seguindo as regras

"""
# 01

idade = input('digite sua idade: ')

if int(idade) < 16:
    print('Voce eh menor de idade, desligue tudo imediatamente')
elif int(idade) <= 18:
    print('Voce é EMANCIPADO, cuidado com o que está mexendo')
else:
    print('Voce eh MAIOR de idade, responde por seus atos')


# 02

idade_nadador = int(input('Digite a sua idade nadador: '))

if idade_nadador < 5:
    print('Voce não tem a idade necessaria para participar')
elif idade_nadador >= 5 and idade_nadador <= 7:
    print('Sua categoria é Infantil A')
elif idade_nadador >= 8 and idade_nadador <= 10:
    print('Sua categoria é Infantil B')
elif idade_nadador >= 11 and idade_nadador <= 13:
    print('Sua categoria é Juvenil A')
elif idade_nadador >= 14 and idade_nadador <= 17:
    print('Sua categoria é Juvenil B')

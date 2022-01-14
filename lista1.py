####### programa 1 #######

# ano_nascimento = int(input('Insira o ano de seu nascimento:   '))

# if(2022 - ano_nascimento >= 16):
#     print('Apto a ser eleitor')
# else:
#     print('Inapto a ser eleitor')


####### programa 2 #######
# numero = int(input('Insira um numero e veja se ele e par ou impar:   '))

# if(numero % 2 == 0):
#     print('par')
# else:
#     print('impar')


####### programa 3 #######
# vogais = ['A','E','I','O','U']

# caractere = list(input('Insira um caractere:   '))[0]

# if(caractere.upper() in vogais):
#     print('Voce digitou uma vogal')
# else:
#     print('Voce nao digitou uma vogal')


####### programa 4 #######
# numero = 0

# dias_semana = ('Domingo','Segunda','Terça','Quarta','Quinta','Sexta','Sabado')

# while (numero < 1 or numero > 7 ):
#     numero = int(input('Insira um numero entre 1 e 7:   '))

# print('O dia da semana selecionado relativo ao numero e: {}'.format(dias_semana[numero - 1]))


####### programa 5 #######

# arquivo = open('copa.txt', 'r')
# linhas = arquivo.readlines()

# datas = []
# campeoes = []

# for item in linhas:
#     datas.append(int(item.split()[0]))
#     campeoes.append(item.split()[2])

# copas = dict(zip(datas,campeoes))

# data_chute = int(input('insira um ano que voce acredite que teve copa do mundo e veja a selecao campea:   '))

# if( data_chute in copas.keys()):
#     print('O campeao foi {}'.format(copas[data_chute]))
# else:
#     print('Data invalida')


####### programa 6 #######

# n_disciplinas = int(input('Insira o numero de disciplinas em que a media nao foi alcancada:     '))
# if(n_disciplinas == 0):
#     print('Aprovado')
# elif(n_disciplinas > 0 and n_disciplinas < 6):
#     print('Recuperacao')
# elif(n_disciplinas > 5):
#     print('Reprovado')
# else:
#     print('Numero de disciplinas inserido invalido')


####### programa 7 #######

# print('Insira as 2 notas obtidas ao longo do curso:\n')
# nota1 = int(input('nota 1 = '))
# nota2 = int(input('nota 2 = '))

# media = (nota1 + nota2)/2
# print('A sua media foi: {}'.format(media))

# if(media >= 6):
#     print('Aprovado')
# else:
#     print('Reprovado')


####### programa 8 #######

# A = int(input('Insira o lado 1 de um triangulo:     '))
# B = int(input('Insira o lado 2 de um triangulo:     '))
# C = int(input('Insira o lado 3 de um triangulo:     '))

# if(A > (B + C) or B > (A + C) or C > (A + B)):
#     print('Valores inseriodos nao formam um triangulo')
# else:
#     if(A==B and B == C):
#         print('Triangulo equilatero')

#     elif(A != B and B != C and C != A):
#         print('Triangulo escaleno')

#     else:
#         print('Triangulo Isosceles')


####### programa 9 #######

# mini_games = int(input('Insira a quantidade de mini-games vendidos:  '))
# calculadoras = int(input('Insira a quantidade de calculadoras vendidas:  '))
# canetas = int(input('Insira a quantidade de canetas vendidas:  '))


# total_minigames = 6.95 * mini_games
# total_calculadoras = 3.5 * calculadoras
# total_canetas = 1.2 * canetas

# print('Faturamento - mini-games: R$ {:.2f}'.format(total_minigames))
# print('Faturamento - calculadoras: R$ {:.2f}'.format(total_calculadoras))
# print('Faturamento - canetas : R$ {:.2f}'.format(total_canetas))

# print('Faturamento - TOTAL: R$ {:.2f}'.format(total_canetas + total_calculadoras + total_minigames))


####### programa 10 #######

salario = float(input('Insira seu salario bruto: R$ '))

aliquotas = [(1903.99, 2826.65, 7.5), (2826.66, 3751.05, 15), (3751.06, 4664.68, 22.5)]

if (salario > 4664.68):
    aliquota = 27.5
else:
    for i, j, k in aliquotas:
        if (i <= salario <= j):
            aliquota = k
            break

print('Salario bruto R$ {:.2f}'.format(salario))
print('Desconto R$ {:.2f}'.format(salario * aliquota * 0.01))
print('Salario liquido R$ {:.2f}'.format(salario * (1 - aliquota * 0.01)))


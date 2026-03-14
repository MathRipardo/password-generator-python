import random

print('seja bem-vindo ao gerador de senhas')

caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-+'

numero = input('quantidade de senhas que deseja gerar: ')
numero = int(numero)

tamanho = input('insira a quantidade de caracters desejado: ')
tamanho = int(tamanho)

print('aqui esta a sua(s) senhas:')

for pwd in range(numero) :
    senhas = ' '
    for c in range (tamanho):
        senhas += random.choice(caracteres)
    print(senhas) 

# Nome = input('Bem vindo ao mundo da programação, João')
# print(Nome)



# Valor_na_carteira = int(input('Digite o valor na carteira: '))
# cambio = Valor_na_carteira/5
# print(f"O valorem dolar é de: {cambio}")


# Numero01 = int(input('Digite o primeiro número: '))
# Numero02 = int(input('Digite o segundo número: '))
# Numero03 = int(input('Digite o terceiro número: '))
# soma = Numero01*Numero02*Numero03
# print(f'o resultado é: {soma}')

# idade = 25
# tex = f'Meu nome é Ádones, eu tenho {idade} anos'
# print(tex)

# valor_compra = int(input('Digite o valor da compra: '))
# if 500 < valor_compra < 1000:
#     desconto = valor_compra * 0.05
#     valor_final = valor_compra - desconto
#     print(valor_final)
# elif 1500 < valor_compra <= 5000:
#     desconto2 = valor_compra * 0.20
#     valor_fin = valor_compra - desconto2
# print(valor_compra)

# conta = int(input('Digite seu consumo: R$'))
# if (conta < 80):
#     print('consumação minima: R$')
#     conta = 80

    
# golspal = int(input('quantidade de gols palmeras '))
# golscor = int(input('quantidade de gols do corinthians '))
# if(golspal>golscor):
#     print('dale porco')
# elif(golspal<golscor):
#     print('vai coringa')
# else:
#     print('empatou')
# print('Jogo disputadissimo!')

# for Y in range(7, 2, -2):
#     print(Y)
#     print(Y, "* 10 =", Y*10)
# print('fim programa')

# x = 5
# while(x>= 1):
#     print(x)
#     x = x - 1
# print('Fim do programa')

# def pri_fap ():
#     ''' Exibe o cabeçalho da  disciplina '''
#     print('FAP')
#     print('Faculdade Adventista do Parana')
#     print('Campo ivatuba')
#     print('Primeiro semestre')
#     print('noturno')
#     return
# pri_fap()

# def saudacao (n,s):
#     print('Bom dia')
#     print(n,s)
#     print('Seja bem vindo\n')
#     return
# saudacao('Adones', 'Cerqueira')

# def area (LA, LB):
#     '''calcule a área do retângulo'''
#     a = LA * LB
#     return a
# print('a area de um retângulo 3 por 5 é igual a:', area(7,5))

# from datetime import datetime
# def hora_certa():
#     n = datetime.now()
#     h = str(n.hour)+':'+str(n.minute)+':'+str(n.second)
#     print(hex(id(h)))
#     return h
# input('Tecle qq coisa para saber a hora:')
# print(hora_certa())

alunos = []
alunos = ['pedro', 'carlos', 'adones', 'paulo']
print('pedro' in alunos)

# for idx in range(0,len(alunos)):
#     print(f'{idx+1}: {alunos[idx]}')

for aluno in alunos:
    print()
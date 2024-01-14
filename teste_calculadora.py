def soma(num1 , num2):
    print('Soma igual a :', num1+num2)

def subtracao(num1 , num2):
    print('Subtração igual a :', num1-num2)

def multiplicacao(num1, num2):
    print('Multiplicação igual a : ', num1*num2)

def divisao(num1, num2):
    print('Divisao igual a :', num1/num2)
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('Selecione uma opçao para realizar as operacoes\n'
      '1 - Soma\n'
      '2 - Subtração\n'
      '3 - Multiplicação\n'
      '4 - Divisão\n'
      '5 - Sair')
if __name__ == '__main__':
    opcao = int(input('Digite sua opção: '))
    if opcao > 5 or opcao < 1 :
        print('Opção Inválida!')
    else:
        if opcao == 1:
            soma(num1,num2)
        elif opcao == 2:
            subtracao(num1, num2)
        elif opcao == 3:
            multiplicacao(num1, num2)
        elif opcao == 4:
            divisao(num1,num2)
        else :
           print('SAINDO ... ')
        pass 
    pass
import time

print('Vamos calcular alguns números!')
time.sleep(2)
nome = str(input('Primeiro, digite seu nome: '))
time.sleep(0.5)
print(f'Muito bem, {nome}, vamos dar início aos nossos cálculos!')

def calculadora(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b != 0:             # Para não dividir por 0
            return a / b
        else:
            return print("ERRO!")

while True:
    n1 = float(input("Digite um número: "))
    n2 = float(input("Digite outro número: "))
    op = str(input("Digite a operação [+ , - , * , /]: "))
    resposta = calculadora(n1, n2, op)
    print(f'{n1} {op} {n2} é = {resposta:.2f}')
    time.sleep(1)
    while True:
        continuar = str(input('Deseja continuar? [S/N] '))
        if continuar.upper() == "N" or continuar.upper() == "S":
            break
        else:
            print("Favor digitar somente 'S' ou 'N'")
    if continuar.upper() == "N":
        print('Até logo!')
        break
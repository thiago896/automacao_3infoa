'''
Crie um script que solicita que o usuario digite dois numeros inteiros
Apos o programa deve realizar a divisão do primeiro número pelo segundo número.
Por fim, deve mostrar o resultado da divisão
'''
while True:
    try:
        a = int(input(('digite um numero: ')))
        b = int(input(('digite outro numero: ')))
        div = a / b
        print(f"o resultado da divisão desses numeros é {div}")
        break
    except ValueError:
        print("o valor digitado é inválido, digite novamente")
    except ZeroDivisionError:
        print("Não é possivel dividir por 0. Tente novamente")
    except Exception as bolinha:
        print("Ocorreu um erro", bolinha)
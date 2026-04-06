from funcao import imprimir, LerInteiro, dividir, pularlinha

imprimir("digite um número: ")
n1 = LerInteiro()

pularlinha()    

imprimir("digite outro número: ")
n2 = LerInteiro()
r = dividir(n1, n2)

pularlinha()

imprimir(r)


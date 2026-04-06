import funcao

funcao.imprimir("digite um numero 1: ")
n1 = funcao.LerInteiro()

funcao.imprimir("digite um numero 2: ")
n2 = funcao.LerInteiro()

r = funcao.somar(n1,n2)

funcao.pularlinha()
funcao.imprimir(f"O valor da soma de {n1} + {n2} é {r}")
funcao.pularlinha()
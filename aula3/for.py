#Estrutura de repetição for
#utilizada para repetir um conjunto de instruções por
#um numero determinado de vezes (conhecido)

#range -> Comando utilizado para criar intervalor númericos 
#exemplo

#range(5) -> Cria o intervalo númerico: 0, 1, 2, 3, 4
# (o ultimo valor não entra no conjunto)

#range(valor inicial, valor final, passo)
#range(1, 5, 1) -> (1, 2, 3, 4)
#range(4, 9, 2) -> (4, 6, 8) 
#range(, , ) -> (5, 4, 3, 2, 1)

for valor in range(5):
    print(valor, end=" ")

print("\n")

for valor1 in range(4, 9,2):
    print(valor1, end=" ") 

print("\n")

for valor2 in range(5, 0, -1):
    print(valor2, end=" ") 
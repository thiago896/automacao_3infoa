#estrutura de repetição for para listas
#Lisra: Estrutura de dados composta (armazena vários valores)

#cria uma lista com nomes
nomes = ['pietro' , 'ryan' , 'maria' , 'gabriela' , 'sophia']

#imprime toda a lista(conjunto)
print(nomes)

print("\n")

#imprime um nome individualmente (maria)
print(nomes[2])

print("\n")

#imprime todos os numes utilizando for - range
for i in range(5):
    print(nomes[i])

print("\n")

#outra opção para interar(percorrer de 1 em 1) sobre as listas
for nome in nomes:
    print(nome)

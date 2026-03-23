#lista de nomes 
nomes = ['giovanna' , 'mateus' , 'goão' , 'pietro' , 'julia' , 'vitoria']

for indice, nome in enumerate(nomes):
    print(f'Estou no {indice} que possui o {nome}')
    if nome == 'goão':
        nomes[indice] = 'joão'
        break

print(nomes)
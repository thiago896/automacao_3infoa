#entrada 
titulo = input("digite oo nome do filme: ")
diarias = int(input("por quantos dias alugou o filme: "))
tempo = int(input("por quantos dias ficou com o filme: "))

#processamento
valor = tempo * 5
multa = 0

if tempo - diarias > 0:
    multa = 15

total = valor + multa

#saida

print("o total foi de: ", total, "dolares")
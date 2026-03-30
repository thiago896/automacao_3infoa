dict_aluno1 = {'nome': 'giovanna', 'situacao': 'matriculada', 'nota': 0}
dict_aluno2 = {'nome': 'gabriel', 'situacao': 'evadido', 'nota': 0}
dict_aluno3 = {'nome': 'mateus', 'situacao': 'matriculada', 'nota': 0}
dict_aluno4 = {'nome': 'goão', 'situacao': 'matriculada', 'nota': 0}

lista_aluno = [dict_aluno1, dict_aluno2, dict_aluno3, dict_aluno4]

for aluno in lista_aluno:
    if aluno["situacao"] != 'matriculada':
        continue
    nota = float(input(f"digite a nota do aluno  {aluno['nome']}: "))
    aluno['nota'] = nota

print(lista_aluno)
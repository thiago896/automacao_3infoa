import pandas

#Pandas bibliotecas para manipular dados tabulares.
#No pandas uma planilha/tabela é chamada de dataframe.
#um dataframe de formado por um conunto de series (colunas)

#Vamos, ler uma planilha de excel e criar um dataframe

df = pandas.read_excel("aula9\\Planilha.xlsx")

#coisa a planilha inteira
print(df)
#coisa o alan inteiro
print(df.loc[10])
#coisa apenas o nome do alan
print(df.loc[10,"Nome"])


df.loc[10, "nome"] = "outro nome"

print(df)
string = str(input("Informe uma palavra ou frase:"))


dicionario = dict()
x = 0
while x < len(string):
    print("teste")
    if string[x] != " ":
        dicionario[string[x]] = string.count(string[x])
    x = x + 1
print(dicionario)

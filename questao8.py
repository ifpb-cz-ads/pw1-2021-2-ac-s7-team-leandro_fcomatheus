T = [-10, -8, 0, 1, 2, 5, -2, -4]
mínima = T[0]
máxima = T[0]
soma = 0
for temp in T:
    if temp < mínima:
        mínima = temp
    if temp > máxima:
        máxima = temp
    soma = soma + temp
print(f"Temperatura máxima: {máxima} °C")
print(f"Temperatura mínima: {mínima} °C")
print(f"Temperatura média: {soma / len(T)} °C")

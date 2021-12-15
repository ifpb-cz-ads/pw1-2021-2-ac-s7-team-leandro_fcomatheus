L = [15, 7, 27, 39]
p = int(input("Digite o primeiro valor a procurar(p):"))
v = int(input("Digite o segundo valor a procurar(v):"))
x = 0
achouP = False
achouV = False
achouPrimeiro = 0

while x < len(L):
    if L[x] == p:
        achouP = True
        if not achouV:
            achouPrimeiro = 1
    if L[x] == v:
        achouV = True
        if not achouP:
            achouPrimeiro = 2
    x += 1

if achouP:
    print(f"p: {p} encontrado")
else:
    print(f"p: {p} não encontrado")
if achouV:
    print(f"v: {v} encontrado")
else:
    print(f"v: {v} não encontrado")
if achouPrimeiro == 1:
    print("p foi achado antes de v")
elif achouPrimeiro == 2:
    print("v foi achado antes de p")

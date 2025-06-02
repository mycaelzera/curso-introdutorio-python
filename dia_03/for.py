
nome = "Mycael"

for i in nome: ## for vai PERCORRER os elementos de um objeto
    print(i)


numero = 2
max_numero = 100

for i in range(1, max_numero+1):
    print(numero, "X", i, "=", numero * i)

# Quais números são divisiveis por 4
# no intervalo [4-100] ?
for i in range(4, 101):
    if i % 4 == 0:
        print(i)
print("Acabou")



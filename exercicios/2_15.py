# Escreva um programa que receba uma lista de números do usúario e conte quantas vezes o numero específico aparece na lista. Solicite ao usuário um número e exiba a contagem.
# %%
lista = [1,2,3,3,2,1,1,1,1,1,5,6,7,7,6,5]

numero = int(input("Entre com um número: "))

contador = 0
for i in lista:
    if i == numero:
        contador += 1
    
print("Quantidade de", numero, ":", contador)
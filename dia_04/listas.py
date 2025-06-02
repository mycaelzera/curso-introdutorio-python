# listas

idades = [28, 42, 43, 35, 39, 28, 38]
print(idades)

# %%
mycael = ["Mycael", "Moreira", 20, False, "Solteiro", 1500.0]
print(mycael)

# %%
type(mycael)

# %%

# idade
mycael[2]

# renda
print(mycael[5])

print(mycael[0])

# %%

idades = [28, 42, 43, 35, 39, 28, 38, 42, 34]

# funções
print("Soma idades: ", sum(idades))

print("Qtde idades:", len(idades))

print("Média idades: ", sum(idades) / len(idades))

print("Menor idade: ", min(idades))

print("Maior idade: ", max(idades))

# %% 

mycael = ["Mycael Moreira", 20, False, "Solteiro", 
        ["Estagiario", "ds jr", "ds pl", "ds sr", "head"],
        [1500, 4000, 4550, 6500, 10000],
        ["Ana", "Maria", "Claudia"]]

print(mycael)

print("Tamanho da lista Mycael:", len(mycael))

print(mycael[4][0]) # isso aqui

exs = mycael[4] # é exatamente a mesma coisa que isso
primeira_ex = exs[0] # é exatamente a mesma coisa que isso
print(primeira_ex) # é exatamente a mesma coisa que isso

# %%

tamanho = len(mycael)
pos = tamanho - 1
exs = mycael[pos]

mycael[pos][len(exs)-1]

# %%
mycael[-1]  # O -1 é o ultimo elemento da lista
mycael[-1][-1] # acesar o ultimo elemento da lista e a ultima "ex"

# %%

mycael[0:4]

mycael[4][3:5]

# %%
mycael[4][-2:]

# %%
mycael[:4] # nao precisa colocar o ultimo elemento quando :

#  mycael[ star : stop ]

# %%

salarios = mycael[5]
salarios[::-1] # navegar de tras p frente
salarios[::2] # navegar de 2 em 2
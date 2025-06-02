texto = """
(1) Água mineral natural
(2) Água mineral com gás
"""

opcao = input(texto)
conta = 0

if opcao == "1":
    conta = 1.50
elif opcao == "2":
    conta = 2.50

if conta == 0:
    print("Entre com a porra da opção correta, com todo respeito.")
else:
    print("Sua conta deu: R$", conta)
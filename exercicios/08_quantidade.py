texto = """
(1) Água mineral natural - R$1,50
(2) Água mineral com gás - R$2,50

"""


opcao = input(texto)

valor_item = 0
if opcao == "1":
    valor_item = 1.50    
elif opcao == "2":
    valor_item = 2.50
      
if valor_item == 0:
    print("Entre com a porra da opção correta, com todo respeito.")
else:
    qtde = int(input("Quantas garrafas? "))
    valor_total = valor_item * qtde
    print("Sua conta deu: R$", valor_total)
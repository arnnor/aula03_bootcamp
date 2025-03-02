quantidade = int(input("Digite a quantidade: "))  # Exemplo de valor, substitua com input do usuário se necessário
preço = float(input("Digite o valor: "))  # Exemplo de valor, substitua com input do usuário se necessário

if quantidade > 0 and preço > 0:
    print("Dados válidos")
else:
    print("Dados inválidos")
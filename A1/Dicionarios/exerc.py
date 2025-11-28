produtos = {}

quantidade = int(input("Quantos produtos deseja cadastrar? "))
for _ in range(quantidade):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco

print("\nProdutos cadastrados:")
for nome, preco in produtos.items():    
    print(f"Produto: {nome}, Preço: R$ {preco:.2f}")
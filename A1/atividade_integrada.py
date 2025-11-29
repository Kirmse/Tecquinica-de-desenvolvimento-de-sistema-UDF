"""
SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
Exercício integrado que utiliza:
- Listas: armazenar livros
- Dicionários: dados dos livros
- Estruturas de condicionais: validações e categorias
- Estruturas de repetição: processar dados
"""

print("=" * 60)
print("SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
print("=" * 60)

# Inicializa a biblioteca com uma lista de dicionários
biblioteca = []

# Menu principal
while True:
    print("\n--- MENU PRINCIPAL ---")
    print("1. Cadastrar livro")
    print("2. Listar livros")
    print("3. Buscar livro por título")
    print("4. Remover livro")
    print("5. Sair")
    
    opcao = input("Escolha uma opção (1-5): ")
    
    # ESTRUTURA CONDICIONAL: Validar escolha do usuário
    if opcao == "1":
        print("\n--- CADASTRAR NOVO LIVRO ---")
        
        titulo = input("Digite o título do livro: ")
        autor = input("Digite o autor do livro: ")
        ano = int(input("Digite o ano de publicação: "))
        preco = float(input("Digite o preço do livro: "))
        quantidade = int(input("Digite a quantidade em estoque: "))
        
        # ESTRUTURA CONDICIONAL: Categorizar por ano
        if ano < 1900:
            categoria = "Clássico Antigo"
            desconto = 0.20  # 20% de desconto
        elif ano < 1950:
            categoria = "Clássico"
            desconto = 0.15  # 15% de desconto
        elif ano < 2000:
            categoria = "Moderno"
            desconto = 0.10  # 10% de desconto
        else:
            categoria = "Contemporâneo"
            desconto = 0.05  # 5% de desconto
        
        # Calcula preço com desconto
        preco_desconto = preco * (1 - desconto)
        
        # DICIONÁRIO: Armazena dados do livro
        livro = {
            "titulo": titulo,
            "autor": autor,
            "ano": ano,
            "categoria": categoria,
            "preco": preco,
            "preco_desconto": preco_desconto,
            "quantidade": quantidade
        }
        
        # LISTA: Adiciona livro à biblioteca
        biblioteca.append(livro)
        print(f"✓ Livro '{titulo}' cadastrado com sucesso!")
        print(f"  Categoria: {categoria} | Preço com desconto: R$ {preco_desconto:.2f}")
    
    # ESTRUTURA CONDICIONAL: Listar livros
    elif opcao == "2":
        print("\n--- LIVROS NA BIBLIOTECA ---")
        
        # ESTRUTURA CONDICIONAL: Verificar se há livros
        if len(biblioteca) == 0:
            print("Nenhum livro cadastrado.")
        else:
            # ESTRUTURA DE REPETIÇÃO: Iterar sobre a lista de livros
            for indice, livro in enumerate(biblioteca, 1):
                print(f"\n{indice}. Título: {livro['titulo']}")
                print(f"   Autor: {livro['autor']}")
                print(f"   Ano: {livro['ano']} | Categoria: {livro['categoria']}")
                print(f"   Preço: R$ {livro['preco']:.2f} → R$ {livro['preco_desconto']:.2f}")
                print(f"   Quantidade em estoque: {livro['quantidade']}")
            
            # ESTRUTURA DE REPETIÇÃO: Calcular estatísticas
            print(f"\n--- ESTATÍSTICAS ---")
            total_livros = len(biblioteca)
            
            # Soma usando repetição
            valor_total_estoque = 0
            quantidade_total = 0
            
            for livro in biblioteca:
                valor_total_estoque += livro['preco_desconto'] * livro['quantidade']
                quantidade_total += livro['quantidade']
            
            print(f"Total de títulos: {total_livros}")
            print(f"Total de livros em estoque: {quantidade_total}")
            print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")
    
    # ESTRUTURA CONDICIONAL: Buscar livro
    elif opcao == "3":
        print("\n--- BUSCAR LIVRO ---")
        
        titulo_busca = input("Digite o título do livro para buscar: ").lower()
        encontrado = False
        
        # ESTRUTURA DE REPETIÇÃO: Percorrer lista para buscar
        for livro in biblioteca:
            if livro['titulo'].lower() == titulo_busca:
                print(f"\n✓ Livro encontrado!")
                print(f"Título: {livro['titulo']}")
                print(f"Autor: {livro['autor']}")
                print(f"Ano: {livro['ano']} | Categoria: {livro['categoria']}")
                print(f"Preço: R$ {livro['preco']:.2f}")
                print(f"Preço com desconto: R$ {livro['preco_desconto']:.2f}")
                print(f"Quantidade: {livro['quantidade']}")
                encontrado = True
                break
        
        # ESTRUTURA CONDICIONAL: Validar resultado
        if not encontrado:
            print(f"✗ Livro '{titulo_busca}' não encontrado na biblioteca.")
    
    # ESTRUTURA CONDICIONAL: Remover livro
    elif opcao == "4":
        print("\n--- REMOVER LIVRO ---")
        
        # ESTRUTURA CONDICIONAL: Verificar se há livros
        if len(biblioteca) == 0:
            print("Nenhum livro cadastrado.")
        else:
            # Listar livros com índices
            print("Livros cadastrados:")
            for indice, livro in enumerate(biblioteca, 1):
                print(f"{indice}. {livro['titulo']}")
            
            # ESTRUTURA DE REPETIÇÃO: Validar entrada
            while True:
                try:
                    indice_remover = int(input("\nDigite o número do livro para remover (0 para cancelar): "))
                    
                    # ESTRUTURA CONDICIONAL: Validar índice
                    if indice_remover == 0:
                        print("Operação cancelada.")
                        break
                    elif indice_remover < 1 or indice_remover > len(biblioteca):
                        print("Índice inválido!")
                    else:
                        livro_removido = biblioteca.pop(indice_remover - 1)
                        print(f"✓ Livro '{livro_removido['titulo']}' removido com sucesso!")
                        break
                except ValueError:
                    print("❌ Por favor, digite um número válido.")
    
    # ESTRUTURA CONDICIONAL: Sair
    elif opcao == "5":
        print("\nObrigado por usar o sistema! Até logo!")
        break
    
    # ESTRUTURA CONDICIONAL: Opção inválida
    else:
        print("❌ Opção inválida! Tente novamente.")

print("=" * 60)

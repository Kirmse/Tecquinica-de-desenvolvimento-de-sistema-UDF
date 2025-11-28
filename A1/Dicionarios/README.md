# Cadastro de Produtos com Dicionários

## Descrição
Este programa implementa um sistema simples de cadastro de produtos utilizando **dicionários** em Python. O programa permite que o usuário registre produtos com seus respectivos preços e depois exibe todos os produtos cadastrados.

## Como funciona

### 1. Inicialização
```python
produtos = {}
```
- Cria um dicionário vazio chamado `produtos` que armazenará os dados

### 2. Entrada de dados
```python
quantidade = int(input("Quantos produtos deseja cadastrar? "))
```
- Solicita ao usuário quantos produtos deseja registrar
- Converte a entrada para inteiro com `int()`

### 3. Loop de cadastro
```python
for _ in range(quantidade):
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produtos[nome] = preco
```
- Executa um loop que se repete conforme o número de produtos desejado
- Para cada iteração:
  - Solicita o **nome** do produto
  - Solicita o **preço** do produto (convertido para float)
  - Armazena no dicionário usando o nome como chave e o preço como valor

### 4. Exibição dos resultados
```python
print("\nProdutos cadastrados:")
for nome, preco in produtos.items():    
    print(f"Produto: {nome}, Preço: R$ {preco:.2f}")
```
- Itera sobre todos os itens do dicionário usando `.items()`
- Exibe cada produto e seu preço formatado com 2 casas decimais (`:.2f`)
- O símbolo `R$` é adicionado antes do preço

## Conceitos-chave utilizados

- **Dicionários**: Estrutura de dados que armazena pares de chave-valor
- **Loop `for`**: Repete instruções um número específico de vezes
- **`.items()`**: Método que retorna pares chave-valor do dicionário
- **F-strings**: Formatação de strings com `f"...{variável}..."`
- **Conversão de tipos**: `int()` e `float()` para converter entradas

## Exemplo de uso

```
Quantos produtos deseja cadastrar? 2
Digite o nome do produto: Notebook
Digite o preço do produto: 2500.50
Digite o nome do produto: Mouse
Digite o preço do produto: 45.90

Produtos cadastrados:
Produto: Notebook, Preço: R$ 2500.50
Produto: Mouse, Preço: R$ 45.90
```

## Observações

- Os produtos são armazenados apenas durante a execução do programa (dados não persistem em arquivo)
- Se dois produtos tiverem o mesmo nome, o segundo sobrescreverá o primeiro no dicionário
- O programa assume que o usuário entrará dados válidos (números para preço)

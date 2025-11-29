# Atividade Integrada A1 - Sistema de Gerenciamento de Biblioteca

## 📝 Descrição

Esta atividade integrada combina **todos os 4 conceitos fundamentais** aprendidos no módulo A1 em uma única aplicação prática e realista. O programa implementa um **sistema de gerenciamento de biblioteca** com menu interativo, permitindo cadastrar, listar, buscar e remover livros com categorização automática por época de publicação.

## 🎯 Objetivo

Desenvolver uma compreensão integrada de:
- ✅ **Listas** - Armazenar múltiplos livros
- ✅ **Condicionais** - Validar dados e categorizar livros por época
- ✅ **Dicionários** - Armazenar dados complexos dos livros
- ✅ **Repetição** - Processar e calcular dados da biblioteca

## 🏗️ Estrutura do Programa

O programa é um **menu interativo** que permite 5 operações principais:

### **OPÇÃO 1: Cadastrar Livro (Utiliza todos os 4 conceitos)**

### **OPÇÃO 1: Cadastrar Livro (Utiliza todos os 4 conceitos)**

```python
# ESTRUTURA CONDICIONAL: Categorizar por ano
if ano < 1900:
    categoria = "Clássico Antigo"
    desconto = 0.20
elif ano < 1950:
    categoria = "Clássico"
    desconto = 0.15
elif ano < 2000:
    categoria = "Moderno"
    desconto = 0.10
else:
    categoria = "Contemporâneo"
    desconto = 0.05

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
```

**Conceitos:**
- **Condicionais** (`if/elif/else`): Categorizar livro por ano
- **Dicionários**: Estrutura com múltiplas chaves
- **Listas**: Método `.append()` para adicionar

---

### **OPÇÃO 2: Listar Livros (Utiliza REPETIÇÃO)**

```python
# ESTRUTURA DE REPETIÇÃO: Iterar sobre lista
for indice, livro in enumerate(biblioteca, 1):
    print(f"{indice}. Título: {livro['titulo']}")
    print(f"   Autor: {livro['autor']}")
    # ... mais dados

# ESTRUTURA DE REPETIÇÃO: Calcular estatísticas
for livro in biblioteca:
    valor_total_estoque += livro['preco_desconto'] * livro['quantidade']
    quantidade_total += livro['quantidade']
```

**Conceitos:**
- **Repetição**: Loop `for` com `.enumerate()`
- **Dicionários**: Acessar valores com chaves
- **Condicionais**: Verificar se há livros (`if len(biblioteca) == 0`)

---

### **OPÇÃO 3: Buscar Livro (Utiliza REPETIÇÃO + CONDICIONAIS)**

```python
# ESTRUTURA DE REPETIÇÃO: Percorrer lista
for livro in biblioteca:
    # ESTRUTURA CONDICIONAL: Comparar títulos
    if livro['titulo'].lower() == titulo_busca:
        encontrado = True
        break

# ESTRUTURA CONDICIONAL: Validar resultado
if not encontrado:
    print("Livro não encontrado.")
```

**Conceitos:**
- **Repetição**: Loop `for` para buscar
- **Condicionais**: Verificar condição de igualdade
- **Dicionários**: Acessar valores durante iteração

---

### **OPÇÃO 4: Remover Livro (Utiliza REPETIÇÃO + CONDICIONAIS)**

```python
# Listar com REPETIÇÃO
for indice, livro in enumerate(biblioteca, 1):
    print(f"{indice}. {livro['titulo']}")

# REPETIÇÃO enquanto entrada inválida
while True:
    indice_remover = int(input("Digite o número: "))
    
    # CONDICIONAIS: Validar
    if indice_remover == 0:
        break
    elif indice_remover < 1 or indice_remover > len(biblioteca):
        print("Inválido!")
    else:
        livro_removido = biblioteca.pop(indice_remover - 1)
        break
```

**Conceitos:**
- **Repetição**: Loop `while` para validação
- **Condicionais**: Validar entrada do usuário
- **Listas**: Método `.pop()` para remover

---

### **OPÇÃO 5: Sair

O programa finaliza e sai do loop `while`.

## 📊 Fluxo de Dados

```
MENU PRINCIPAL
    ↓
[LISTAS] biblioteca = []
    ↓
while True (loop infinito até sair):
    ↓
[CONDICIONAIS] if opcao == "1":
    ├─ Entrada: título, autor, ano, preço, quantidade
    ├─ [CONDICIONAIS] Categorizar por ano
    ├─ [DICIONÁRIOS] Criar dict com dados do livro
    └─ [LISTAS] biblioteca.append(livro)
    ↓
[CONDICIONAIS] elif opcao == "2":
    ├─ [CONDICIONAIS] if len(biblioteca) == 0
    ├─ [REPETIÇÃO] for livro in biblioteca
    ├─ [DICIONÁRIOS] Acessar livro['titulo'], etc
    └─ [REPETIÇÃO] Calcular totais
    ↓
[CONDICIONAIS] elif opcao == "3":
    ├─ [REPETIÇÃO] for livro in biblioteca
    ├─ [CONDICIONAIS] if livro['titulo'].lower() == titulo_busca
    └─ [DICIONÁRIOS] Exibir dados do livro
    ↓
[CONDICIONAIS] elif opcao == "4":
    ├─ [REPETIÇÃO] for indice, livro in enumerate(biblioteca)
    ├─ [REPETIÇÃO] while True (validação)
    ├─ [CONDICIONAIS] Validar entrada
    └─ [LISTAS] biblioteca.pop(indice)
    ↓
[CONDICIONAIS] elif opcao == "5":
    └─ break (sair do programa)
```

---

## 🧪 Exemplo de Execução

```
============================================================
SISTEMA DE GERENCIAMENTO DE BIBLIOTECA
============================================================

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 1

--- CADASTRAR NOVO LIVRO ---
Digite o título do livro: Dom Casmurro
Digite o autor do livro: Machado de Assis
Digite o ano de publicação: 1899
Digite o preço do livro: 45.00
Digite a quantidade em estoque: 5
✓ Livro 'Dom Casmurro' cadastrado com sucesso!
  Categoria: Clássico Antigo | Preço com desconto: R$ 36.00

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 1

--- CADASTRAR NOVO LIVRO ---
Digite o título do livro: Harry Potter e a Pedra Filosofal
Digite o autor do livro: J.K. Rowling
Digite o ano de publicação: 1997
Digite o preço do livro: 55.00
Digite a quantidade em estoque: 10
✓ Livro 'Harry Potter e a Pedra Filosofal' cadastrado com sucesso!
  Categoria: Moderno | Preço com desconto: R$ 49.50

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 1

--- CADASTRAR NOVO LIVRO ---
Digite o título do livro: Sapiens
Digite o autor do livro: Yuval Noah Harari
Digite o ano de publicação: 2011
Digite o preço do livro: 65.00
Digite a quantidade em estoque: 8
✓ Livro 'Sapiens' cadastrado com sucesso!
  Categoria: Contemporâneo | Preço com desconto: R$ 61.75

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 2

--- LIVROS NA BIBLIOTECA ---

1. Título: Dom Casmurro
   Autor: Machado de Assis
   Ano: 1899 | Categoria: Clássico Antigo
   Preço: R$ 45.00 → R$ 36.00
   Quantidade em estoque: 5

2. Título: Harry Potter e a Pedra Filosofal
   Autor: J.K. Rowling
   Ano: 1997 | Categoria: Moderno
   Preço: R$ 55.00 → R$ 49.50
   Quantidade em estoque: 10

3. Título: Sapiens
   Autor: Yuval Noah Harari
   Ano: 2011 | Categoria: Contemporâneo
   Preço: R$ 65.00 → R$ 61.75
   Quantidade em estoque: 8

--- ESTATÍSTICAS ---
Total de títulos: 3
Total de livros em estoque: 23
Valor total do estoque: R$ 1,469.50

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 3

--- BUSCAR LIVRO ---
Digite o título do livro para buscar: harry potter e a pedra filosofal

✓ Livro encontrado!
Título: Harry Potter e a Pedra Filosofal
Autor: J.K. Rowling
Ano: 1997 | Categoria: Moderno
Preço: R$ 55.00
Preço com desconto: R$ 49.50
Quantidade: 10

--- MENU PRINCIPAL ---
1. Cadastrar livro
2. Listar livros
3. Buscar livro por título
4. Remover livro
5. Sair
Escolha uma opção (1-5): 5

Obrigado por usar o sistema! Até logo!
============================================================
```

---

## 🔑 Conceitos-Chave Integrados

### 1. **Listas**
- Declaração e inicialização
- Método `.append()`
- Iteração com `for`
- Função `len()`

### 2. **Condicionais**
- `if/elif/else`
- Operadores de comparação (`<`, `>`, `<=`, `>=`)
- Lógica de validação
- Categorização baseada em condições

### 3. **Dicionários**
- Declaração e inicialização
- Armazenamento chave-valor
- Dicionários aninhados
- Método `.items()` para iteração

### 4. **Repetição**
- Loop `for` com `range()`
- Loop `for` com `.items()`
- Loop `while` com condição
- Incremento manual em `while`
- Acumuladores

## 🔑 Conceitos-Chave Integrados

### 1. **Listas**
- Declaração e inicialização: `biblioteca = []`
- Método `.append()`: Adicionar elementos
- Método `.pop()`: Remover elementos
- Função `len()`: Obter quantidade
- `.enumerate()`: Iterar com índices
- Acessar por índice: `biblioteca[0]`

### 2. **Condicionais**
- `if/elif/else`: Estrutura condicional
- Operadores: `<`, `>`, `<=`, `>=`, `==`, `!=`
- Lógica de validação
- Categorização baseada em condições
- Verificação de estados

### 3. **Dicionários**
- Declaração: `livro = {}`
- Armazenamento chave-valor
- Método `.items()`: Iterar sobre pares
- Função `len()`: Contar elementos
- Acessar valores: `livro['titulo']`
- Aninhamento de estruturas

### 4. **Repetição**
- Loop `for`: Iterar sobre sequências
- Loop `while`: Repetir enquanto condição
- `range()`: Gerar sequências
- Acumuladores: `total += valor`
- `break` e `continue`: Controlar fluxo
- `.enumerate()`: Iteração com índices

---

## 💡 Variações e Exercícios

### Desafio 1: Adicione filtro por categoria
```python
categoria_busca = input("Qual categoria? ")
for livro in biblioteca:
    if livro['categoria'] == categoria_busca:
        print(livro)
```

### Desafio 2: Ordene livros por preço
```python
livros_ordenados = sorted(biblioteca, key=lambda x: x['preco'])
```

### Desafio 3: Adicione operação de editar livro
- Permitir atualizar dados de um livro existente

### Desafio 4: Implemente desconto por quantidade
- Se quantidade > 20, aplique desconto adicional

### Desafio 5: Exporte relatório para arquivo
```python
with open('relatorio.txt', 'w') as arquivo:
    for livro in biblioteca:
        arquivo.write(f"{livro['titulo']} - {livro['preco']}\n")
```

---

## 📚 Mapeamento com Atividades Originais

Este programa utiliza conceitos das 4 atividades originais:

| Atividade Original | Onde é usada | Exemplo |
|-------------------|--------------|---------|
| `Listas/exerc.py` | Armazenar livros | `biblioteca = []` e `.append()` |
| `Estruturas_de_condicionais/exerc.py` | Categorizar por ano | `if ano < 1900: categoria = "Clássico Antigo"` |
| `Dicionarios/exerc.py` | Dados dos livros | `livro = {"titulo": ..., "autor": ..., ...}` |
| `Estruturas_de_repeticao/exerc.py` | Iterar e calcular | `for livro in biblioteca: total += ...` |

---

## 🚀 Como Executar

1. Abra o terminal no diretório `A1`
2. Execute:
   ```bash
   python atividade_integrada.py
   ```
3. Siga as instruções na tela
4. Fornecça dados de entrada conforme solicitado

---

## 📋 Checklist de Aprendizado

Após completar esta atividade, você consegue:

- ✅ Criar e manipular listas
- ✅ Iterar sobre listas com `for`
- ✅ Usar estruturas condicionais para validação
- ✅ Criar dicionários com chaves complexas
- ✅ Usar dicionários aninhados
- ✅ Implementar loops `for` e `while`
- ✅ Trabalhar com acumuladores
- ✅ Integrar múltiplos conceitos em um programa
- ✅ Formatar strings com f-strings
- ✅ Realizar cálculos e estatísticas

---

## 🎓 Notas Didáticas

Esta atividade é um **passo importante** para:
1. Passar de exemplos isolados para aplicações integradas
2. Entender como os conceitos trabalham juntos
3. Praticar estrutura de código profissional
4. Resolver problemas do mundo real com Python

---

**Autor:** Estudante de Técnicas de Desenvolvimento de Sistemas  
**Módulo:** A1 - Fundamentos de Python  
**Tipo:** Atividade Integrada  
**Data:** Novembro 2025  
**Status:** Completo

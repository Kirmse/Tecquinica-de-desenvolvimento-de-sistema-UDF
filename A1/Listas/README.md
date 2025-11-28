# Cadastro de Alunos com Listas

## Descrição
Este programa implementa um sistema simples de cadastro de alunos utilizando **listas** em Python. O programa permite que o usuário registre nomes de alunos e depois exibe todos os cadastrados.

## Como funciona

### 1. Inicialização
```python
alunos = []
```
- Cria uma lista vazia chamada `alunos` que armazenará os nomes

### 2. Entrada do número de alunos
```python
quantidade = int(input("Quantos alunos deseja cadastrar? "))
```
- Solicita ao usuário quantos alunos deseja registrar
- Converte a entrada para inteiro com `int()`

### 3. Loop de cadastro
```python
for n in range(quantidade):
    nome = input(f"Digite o nome do aluno {n + 1}: ")
    alunos.append(nome)
```

**Explicação:**
- `for n in range(quantidade)`: Itera um número de vezes igual à quantidade
- `n + 1`: Exibe a posição começando em 1 (em vez de 0)
- `f"..."`: F-string que insere valores dentro da string
- `.append(nome)`: Adiciona o nome ao final da lista

### 4. Exibição dos resultados
```python
print("\nAlunos cadastrados:")
for nome in alunos:
    print(f"Aluno: {nome}")
```
- `for nome in alunos`: Itera sobre cada aluno na lista
- Exibe cada aluno com formatação

## Conceitos-chave utilizados

- **Listas**: Estrutura de dados que armazena múltiplos valores em sequência
- **`.append()`**: Método que adiciona um elemento ao final da lista
- **F-strings**: Formatação de strings com `f"...{variável}..."`
- **`range()`**: Gera sequência de números para o loop
- **Conversão de tipos**: `int()` para converter entrada

## Métodos úteis de listas

| Método | Descrição |
|--------|-----------|
| `.append()` | Adiciona elemento ao final |
| `.insert()` | Insere elemento em posição específica |
| `.remove()` | Remove primeiro elemento encontrado |
| `.pop()` | Remove elemento pela posição |
| `.sort()` | Ordena a lista |
| `.reverse()` | Inverte a ordem |
| `len()` | Retorna quantidade de elementos |

## Exemplo de uso

```
Quantos alunos deseja cadastrar? 3
Digite o nome do aluno 1: João
Digite o nome do aluno 2: Maria
Digite o nome do aluno 3: Pedro

Alunos cadastrados:
Aluno: João
Aluno: Maria
Aluno: Pedro
```

## Observações

- Os alunos são armazenados apenas durante a execução (dados não persistem)
- A lista mantém a ordem de inserção
- Permite cadastrar alunos com nomes duplicados
- Usa indexação a partir de 0 internamente, mas exibe posição a partir de 1

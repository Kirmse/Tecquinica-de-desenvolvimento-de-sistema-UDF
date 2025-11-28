# Estruturas de Condicionais

## Descrição
Este programa demonstra o uso de **estruturas condicionais** em Python (`if`, `elif`, `else`). O programa valida a idade de um usuário e determina se ele pode entrar em um evento, aplicando diferentes regras de acesso.

## Como funciona

### 1. Entrada de dados
```python
idade = int(input("Digite a sua idade: "))
```
- Solicita a idade do usuário
- Converte para inteiro com `int()`

### 2. Validações com estruturas condicionais

#### Caso 1: Idade inválida
```python
if idade < 0:
    print("Idade inválida.")
```
- Se a idade for menor que 0, exibe mensagem de erro

#### Caso 2: Menores de 14 anos
```python
elif idade < 14:
    print("Entrada proibida para menores de 14 anos.")
```
- Se a idade for entre 0 e 13, acesso é proibido

#### Caso 3: Menores de 18 anos
```python
elif idade < 18:    
    print("Entrada permitida somente com acompanhante maior de 18 anos.")
```
- Se a idade for entre 14 e 17, acesso permitido apenas com acompanhante

#### Caso 4: Maiores de 18 anos
```python
else:
    print("Entrada liberada. Aproveite o evento!")
```
- Se nenhuma das condições anteriores for verdadeira, acesso liberado

## Conceitos-chave

- **`if`**: Testa a primeira condição
- **`elif`**: Testa condições adicionais (else if)
- **`else`**: Executa se nenhuma condição anterior for verdadeira
- **Operadores de comparação**: `<`, `>`, `<=`, `>=`, `==`, `!=`

## Exemplo de uso

```
Digite a sua idade: 25
Entrada liberada. Aproveite o evento!
```

```
Digite a sua idade: 16
Entrada permitida somente com acompanhante maior de 18 anos.
```

```
Digite a sua idade: 10
Entrada proibida para menores de 14 anos.
```

## Observações

- O programa valida apenas a idade
- Não há validação contra entradas inválidas (letras, caracteres especiais)
- A estrutura `elif` permite múltiplas condições encadeadas de forma eficiente

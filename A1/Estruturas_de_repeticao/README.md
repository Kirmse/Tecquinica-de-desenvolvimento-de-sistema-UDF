# Estruturas de Repetição

## Descrição
Este programa demonstra duas formas diferentes de realizar **estruturas de repetição** em Python: usando `for` e `while`. Ambas as versões exibem os números pares de 1 a 100.

## Como funciona

### Método 1: Usando `for` com `range()`

```python
print("Números pares de 1 a 100:")

for numero in range(1, 101):
    if numero % 2 == 0:
        print(numero)
```

**Explicação:**
- `range(1, 101)`: Gera sequência de números de 1 a 100 (101 é excluído)
- `for numero in range()`: Itera sobre cada número da sequência
- `numero % 2 == 0`: Verifica se o número é par (resto da divisão por 2 é zero)
- `print(numero)`: Exibe o número se for par

### Separador
```python
print('__' * 20)
```
- Imprime uma linha separadora (`__` repetido 20 vezes)

### Método 2: Usando `while`

```python
print("Números pares de 1 a 100:")
numero = 1
while numero <= 100:
    if numero % 2 == 0:
        print(numero)
    numero += 1
```

**Explicação:**
- `numero = 1`: Inicializa o contador
- `while numero <= 100`: Repete enquanto a condição for verdadeira
- `numero += 1`: Incrementa o contador em cada iteração
- `if numero % 2 == 0`: Verifica se é par

## Comparação: `for` vs `while`

| Aspecto | `for` | `while` |
|---------|-------|--------|
| **Uso** | Quando sabe a quantidade de iterações | Quando a condição é complexa |
| **Inicialização** | Automática | Manual |
| **Incremento** | Automático | Manual |
| **Legibilidade** | Mais clara para sequências | Mais flexível |
| **Resultado** | Idêntico para este caso | Idêntico para este caso |

## Conceitos-chave

- **`for`**: Itera sobre uma sequência (listas, ranges, etc.)
- **`while`**: Repete enquanto a condição for verdadeira
- **`range(inicio, fim)`**: Gera sequência de números
- **Operador módulo `%`**: Retorna o resto da divisão
- **`+=`**: Operador de incremento (equivalente a `numero = numero + 1`)

## Exemplo de saída

```
Números pares de 1 a 100:
2
4
6
8
...
98
100
________________________________________

Números pares de 1 a 100:
2
4
6
8
...
98
100
```

## Observações

- Ambos os métodos produzem exatamente o mesmo resultado
- O `for` é geralmente mais eficiente e legível para este caso
- O `while` oferece mais controle quando as iterações são condicionais complexas
- O operador `%` é fundamental para verificar divisibilidade

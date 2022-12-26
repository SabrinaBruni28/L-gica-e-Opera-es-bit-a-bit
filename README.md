# Logica-e-Operacoes-bit-a-bit
Trabalho de Matemática Discreta

## Lógica e Operações bit a bit 
 
Informações são armazenadas nos computadores por meio dos chamados bits, que são
símbolos com dois valores possíveis, 0 (zero) e 1 (um). Um bit pode ser usado para
representar um valor-verdade, sendo o 1 usado como verdadeiro (V) e o 0 como falso (F).
Uma sequência de bits de tamanho N possui N símbolos 0 ou 1 em sequência. Uma
operação binária entre duas sequências de bits de mesmo tamanho N aplica um operador
lógico (AND, OR, XOR, NAD ou NOR, por exemplo) a cada bit na mesma posição. Veja a
tabela abaixo como exemplo (mais detalhes na página 16 do livro texto “Lógicas e
Operações Bit”):

A   B    (A OR B)  (A AND B)  (A XOR B)  (A NAND B)  (A NOR B)  (A MOR B) ≡ ((NOT A) OR B)

0   0       0          0           0          1           1                 1

0   1       1          0           1          1           0                 1

1   0       1          0           1          1           0                 0

1   1       1          1           0          0           0                 1


O objetivo deste trabalho é desenvolver um programa que lê como entrada duas
sequências de bits, S1 e S2, de tamanho N, lê uma expressão lógica contendo os
operadores (AND, OR, XOR, NAND, NOR ou MOR) e gera como saída o
resultado da aplicação da operação lógica nas sequências S1 e S2.

### Entrada:

O problema possui quatro linhas de entrada, sendo:
Linha 1: o tamanho N da sequência (máximo de 1000)
Linha 2: a sequência de bits S1
Linha 3: a sequência de bits S2
Linha 4: uma expressão lógica que envolva as sequências S1 e S2 e até duas operações
da lista (AND, OR, XOR, NAND, NOR ou MOR). A prioridade dos operadores deve ser
pela ordem na expressão. Não será utilizado parênteses para mudar a ordem.

### Saída:

Uma linha com uma sequência de N bits como resultado da expressão lógica. Caso o
tamanho de alguma das sequências S1 e S2 seja diferente de N, deve ser gerado ERRO
como saída. Caso a operação da entrada seja diferente das permitidas, deve ser gerado
ERRO como saída. Caso algum símbolo das sequências S1 ou S2 seja diferente de 0 ou
1, deve ser gerado ERRO como saída.


### Exemplos de entrada/saída:

Entrada               Saída

4                      1111
1111
1111
S1 AND S2 

3                      101
101
000
S1 OR S2 

4                      ERRO
1100
101
S1 XOR S2 

7                      ERRO
0000000
0000009
S2 MOR S1 

4                      0000
1111
0000
S2 MOR S1 AND S2 

5                      11111
10100
11111
S2 OR S2 AND S2



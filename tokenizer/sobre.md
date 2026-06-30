Computadores processam bits e bytes
1 bits = 8 bytes
- enconding: codificacao da informacao para bits e bytes.
- tabela ASCII
0 A 127 posicoes a codificacao. em ascii A = 65
UTF-8
- 4 bytes
- a tabela ascii inteira é o primeiro byte.
- linguas não latinase emojis usam os demais.

Algoritmos lida com numeros então como transformar texto em numeros?
A idéia é criar um vocabulario que mapeia um texto em numeros
3 tipos de vocabulario:
    - nivel de caracter
    - nivel de palavra
    - nivel de subpalavra
cada caracter/palavra/subpalavra é representado por uma posicao no vocabulario e essa representacao é token.
entao temos vocabulario de n posicoes que escolhemos.

1 -  Tokens a nível de caracteres:
cada token é 1 caracter, para lingua latina seria 500.
Como transformers decoder é autoregressivo entao teria muitas geracao para cada caracter e perderia de certa forma valor semantico.

2 - token a nível de palavra:
poucos tokens para gerar um output no encoder.
temos infinitas palavras, um erro gramatical faria com que a palavra nao existisse no vocabulario ou diferente da palavra original.
 
3 - tokena a nivel subpalavra
linguas sub-representadas precisam de muitos tokens para gerar uma frase.
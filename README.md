# My-Large-Language-Model

Por que você deve construir seu próprio LLM? Codificar um LLM do zero é um excelente exercício para entender sua mecânica e limitações. Além disso, ele nos equipa com o conhecimento necessário para pré-treinamento ou ajustes definitivos de arquiteturas LLM de código aberto existentes para nossos próprios conjuntos de dados ou tarefas específicas do domínio.

A pesquisa mostrou que, quando se trata de modelar o desempenho, os LLMs personalizados – aqueles adaptados para tarefas ou domínios específicos – podem superar os LLMs de propósito geral, como o ChatGPT, que são projetados para uma ampla gama de aplicativos.

# 🧠 Build a Large Language Model — Do Zero

> Trilha de estudos baseada no livro **"Build a Large Language Model (From Scratch)"** de Sebastian Raschka.  
> Objetivo: construir minha própria LLM do zero em **8 meses**, documentando cada etapa aqui.

---

## 🗺️ Visão Geral da Jornada

```
ETAPA 1 — Fundamentos        → Meses 1–2
ETAPA 2 — Arquitetura LLM   → Meses 3–4
ETAPA 3 — Pré-treinamento   → Mês 5
ETAPA 4 — Fine-tuning        → Meses 6–7
ETAPA 5 — Projeto Final      → Mês 8
```

---

## ✅ Progresso

> Marque com `[x]` conforme for concluindo cada item.

---

### 🟡 PRÉ-REQUISITOS (Mês 1)

> Antes de começar o livro, nivelamento em Python e estruturas de dados.

#### Python Básico
- [ ] Variáveis, tipos de dados, operadores
- [ ] Condicionais e loops (`if`, `for`, `while`)
- [ ] Funções e escopo
- [ ] Listas, tuplas, dicionários, sets
- [ ] Compreensão de listas (`list comprehensions`)
- [ ] Manipulação de strings
- [ ] Leitura e escrita de arquivos

#### Estruturas de Dados Essenciais
- [ ] Arrays e como funcionam na memória
- [ ] Pilhas e filas (stack/queue)
- [ ] Dicionários e tabelas hash
- [ ] Grafos e árvores (conceito básico)
- [ ] Complexidade de algoritmos — O que é Big O?

#### NumPy e PyTorch Introdutório
- [ ] Tensores: o que são e para que servem
- [ ] Operações básicas com NumPy
- [ ] Introdução ao PyTorch (Apêndice A do livro)
  - [ ] Criando tensores
  - [ ] Operações com tensores
  - [ ] Autograd e gradientes
  - [ ] GPU vs CPU

---

### 🟠 CAPÍTULO 1 — Entendendo LLMs (Mês 2 — Semana 1)

> Fundamentos conceituais antes de escrever qualquer código.

- [ ] O que é uma LLM?
- [ ] Aplicações de LLMs no mundo real
- [ ] As 3 etapas de construção de uma LLM
  - [ ] Etapa 1: Preparação de dados e arquitetura
  - [ ] Etapa 2: Pré-treinamento
  - [ ] Etapa 3: Fine-tuning
- [ ] Introdução à arquitetura Transformer
- [ ] Por que grandes datasets são necessários
- [ ] Uma olhada de perto na arquitetura GPT

---

### 🟠 CAPÍTULO 2 — Trabalhando com Dados de Texto (Mês 2 — Semanas 2–3)

> Como transformar texto bruto em números que uma rede neural entende.

- [ ] O que são word embeddings?
- [ ] Tokenização de texto
  - [ ] Implementar tokenizador simples
- [ ] Convertendo tokens em IDs
- [ ] Adicionando tokens especiais de contexto
- [ ] **Byte Pair Encoding (BPE)**
- [ ] Amostragem de dados com janela deslizante (sliding window)
- [ ] Criando embeddings de tokens
- [ ] Codificando posições das palavras (positional encoding)

---

### 🔴 CAPÍTULO 3 — Mecanismos de Atenção (Mês 2 — Semana 4 + Mês 3)

> O coração do Transformer. A parte mais complexa conceitualmene.

- [ ] O problema com sequências longas
- [ ] Capturando dependências com mecanismos de atenção
- [ ] **Self-Attention** — o que é e como funciona
  - [ ] Self-attention simples sem pesos treináveis
  - [ ] Calculando pesos de atenção para todos os tokens
- [ ] Self-attention com pesos treináveis
  - [ ] Calculando pesos passo a passo
  - [ ] Implementando classe Python compacta de self-attention
- [ ] **Causal Attention** — escondendo palavras futuras
  - [ ] Aplicando máscara de atenção causal
  - [ ] Mascaramento com dropout
  - [ ] Classe compacta de causal attention
- [ ] **Multi-Head Attention**
  - [ ] Empilhando múltiplas camadas de atenção
  - [ ] Implementando com weight splits

---

### 🔴 CAPÍTULO 4 — Implementando o Modelo GPT (Mês 3–4)

> Hora de juntar tudo e montar a arquitetura completa.

- [ ] Codificando a arquitetura do modelo LLM
- [ ] **Layer Normalization** — normalizando ativações
- [ ] **Feed Forward Network** com ativações GELU
- [ ] Shortcut connections (conexões residuais)
- [ ] Conectando atenção e camadas lineares — o **Transformer Block**
- [ ] Codificando o modelo GPT completo
- [ ] **Gerando texto** — primeira geração!

---

### 🟣 CAPÍTULO 5 — Pré-treinamento (Mês 5)

> Treinando o modelo em dados não rotulados para criar um modelo base.

- [ ] Avaliando modelos de texto generativo
  - [ ] Usando o GPT para gerar texto
  - [ ] Calculando a perda (loss) de geração de texto
  - [ ] Calculando perda nos conjuntos de treino e validação
- [ ] **Treinando a LLM** — loop de treinamento completo
- [ ] Estratégias de decodificação para controlar aleatoriedade
  - [ ] Temperature scaling
  - [ ] Top-k sampling
  - [ ] Modificando a função de geração de texto
- [ ] Salvando e carregando pesos do modelo em PyTorch
- [ ] **Carregando pesos pré-treinados da OpenAI**

---

### 🔵 CAPÍTULO 6 — Fine-tuning para Classificação (Mês 6)

> Adaptando o modelo base para uma tarefa específica.

- [ ] Categorias de fine-tuning
- [ ] Preparando o dataset de classificação
- [ ] Criando data loaders
- [ ] Inicializando o modelo com pesos pré-treinados
- [ ] Adicionando uma camada de classificação (classification head)
- [ ] Calculando loss e acurácia de classificação
- [ ] Fine-tuning supervisionado
- [ ] **Usando a LLM como classificador de spam**

---

### 🔵 CAPÍTULO 7 — Fine-tuning para Seguir Instruções (Mês 7)

> Transformando o modelo em um assistente que responde a comandos.

- [ ] Introdução ao instruction fine-tuning
- [ ] Preparando dataset para fine-tuning supervisionado de instrução
- [ ] Organizando dados em batches de treinamento
- [ ] Criando data loaders para dataset de instrução
- [ ] Carregando LLM pré-treinada
- [ ] Fine-tuning da LLM em dados de instrução
- [ ] Extraindo e salvando respostas
- [ ] **Avaliando a LLM fine-tunada**

---

### 🟤 APÊNDICES & EXTRAS (Mês 8)

> Tópicos avançados para aprimorar o projeto.

- [ ] **Apêndice D** — Melhorando o loop de treinamento
  - [ ] Learning rate warmup
  - [ ] Cosine decay
  - [ ] Gradient clipping
- [ ] **Apêndice E** — LoRA: Fine-tuning eficiente em parâmetros
  - [ ] O que é LoRA e por que usar?
  - [ ] Implementando LoRA

---

### 🏁 PROJETO FINAL (Mês 8)

- [ ] Consolidar todo o código em um projeto limpo e organizado
- [ ] Escrever documentação clara para cada módulo
- [ ] Criar notebook de demonstração end-to-end
- [ ] Publicar versão final no GitHub com README completo

---

## 📁 Estrutura do Repositório

```
llm-do-zero/
│
├── README.md                 
│
├── 00_prereqs/
│   ├── python_basics.py
│   └── pytorch_intro.py
│
├── 01_entendendo_llms/
│   └── notas.md
│
├── 02_dados_texto/
│   ├── tokenizador.py
│   ├── bpe.py
│   └── embeddings.py
│
├── 03_atencao/
│   ├── self_attention.py
│   ├── causal_attention.py
│   └── multi_head_attention.py
│
├── 04_modelo_gpt/
│   ├── transformer_block.py
│   ├── gpt_model.py
│   └── gerar_texto.py
│
├── 05_pretreinamento/
│   ├── treino.py
│   └── avaliacao.py
│
├── 06_finetune_classificacao/
│   └── spam_classifier.py
│
├── 07_finetune_instrucoes/
│   └── assistente.py
│
└── extras/
    ├── lora.py
    └── melhorias_treino.py
```

---

## 📚 Recursos de Apoio

| Recurso | Link | Para quê |
|---|---|---|
| Livro (referência principal) | *Build a LLM From Scratch* — Sebastian Raschka | Base de todo o projeto |
| Python para Iniciantes | [python.org/doc](https://docs.python.org/pt-br/3/tutorial/) | Nivelamento de Python |
| PyTorch Docs | [pytorch.org/docs](https://pytorch.org/docs/stable/index.html) | Referência técnica |
| 3Blue1Brown — Redes Neurais | [YouTube](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Intuição visual |
| Andrej Karpathy — makemore | [YouTube](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Contexto prático |

---

## 📊 Cronograma

| Mês | Foco |
|---|---|
| **Mês 1** | Pré-requisitos: Python, estruturas de dados, NumPy, PyTorch básico |
| **Mês 2** | Caps. 1, 2 e início do Cap. 3 — teoria + dados de texto |
| **Mês 3** | Cap. 3 (atenção) e Cap. 4 (arquitetura GPT) |
| **Mês 4** | Cap. 4 finalizado — primeiro modelo gerando texto! |
| **Mês 5** | Cap. 5 — pré-treinamento completo |
| **Mês 6** | Cap. 6 — fine-tuning para classificação |
| **Mês 7** | Cap. 7 — fine-tuning para instruções |
| **Mês 8** | Apêndices, LoRA, refatoração e projeto final |

---

## 💡 Dicas Pessoais

- Se travar em algo, avançar e voltar depois — entendimento vem com iteração.
- Copiar o código do livro à mão (não copiar/colar) ajuda a fixar.
- Commit pequeno a cada subtópico concluído — o histórico conta a história.
- Não pular os exercícios — eles testam o que você realmente entendeu.

---

*Iniciado em: <!-- data de início -->*  
*Livro: Build a Large Language Model (From Scratch) — Sebastian Raschka, Manning Publications, 2025*

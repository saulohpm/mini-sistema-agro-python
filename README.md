# 🌱 Mini Sistema de Manuseio de Plantações

Sistema desenvolvido em Python, executado no terminal (CLI), com objetivo educacional, voltado ao aprendizado de lógica de programação, organização de código, manipulação de datas e persistência de dados.

O projeto permite gerenciar plantações agrícolas, acompanhando o ciclo de plantio e colheita, status da produção e geração de relatórios estatísticos simples.

---

## 📌 Funcionalidades

- Cadastro, edição, visualização e remoção de plantações
- Cadastro e alteração do nome do usuário
- Cálculo automático do tempo restante até a colheita
- Classificação do status da colheita:
  - Agendada, Em andamento e Concluída
- Análise de proximas colheitas
- Persistência dos dados em arquivo JSON
- Interface interativa via menu no terminal

---

## 🧠 Conceitos Trabalhados

- Estruturas de dados (list, dict)
- Modularização e organização do código
- Funções e reutilização
- Tratamento de exceções (try/except)
- Manipulação e comparação de datas
- Regras de negócio baseadas em datas
- Entrada e saída de dados no terminal
- Persistência de dados em JSON

---

## 📚 Bibliotecas Utilizadas

- datetime — manipulação e cálculo de datas
- json — leitura e escrita de arquivos JSON
- os — controle do terminal (limpeza de tela)

O projeto não utiliza bibliotecas externas, apenas bibliotecas padrão do Python.

---

## ▶️ Como Executar

Pré-requisitos:
- Python 3 instalado

Execução:
1. Clone o repositório ou baixe os arquivos
2. Acesse a pasta raiz do projeto pelo terminal
3. Execute o comando:
```bash
   python main.py
```

---

## 📂 Estrutura do Projeto

```bash
├── src/
│   ├── main.py
│   ├── utils.py
│   └── usuario.py
│   └── plantacoes.py
├── data/
│   └── plantacoes.json
│   └── usuarios.json
│   └── sementes.json
├── README.md
└── main.py
```


---

## 📌 Observações

- Sistema offline
- Dados armazenados localmente
- Projeto com finalidade educacional
- Estrutura pensada para fácil manutenção e evolução


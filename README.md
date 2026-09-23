# 🛡️ Lab Sandbox

Laboratório experimental para praticar **Python, lógica, validação de dados e fundamentos de segurança de software**.

O projeto atual contém um analisador educacional de requisitos básicos de senhas. A ideia do repositório é evoluir pequenos experimentos com código simples, testável e bem documentado.

## 🎯 Objetivos

- praticar lógica de programação;
- transformar scripts em funções reutilizáveis;
- validar entradas e tipos;
- desenvolver testes automatizados;
- aplicar organização e documentação de código;
- explorar fundamentos de segurança de software.

## 🛡️ Analisador de senhas

O arquivo `senha_segura.py` verifica cinco critérios:

- pelo menos 8 caracteres;
- letra maiúscula;
- letra minúscula;
- número;
- caractere especial.

A classificação é uma **heurística educacional baseada nesses critérios**. Ela não calcula entropia, não estima tempo real para quebra de senha e não substitui políticas de autenticação ou ferramentas especializadas.

O programa não exibe nem armazena a senha informada.

## ▶️ Como executar

Requer Python 3.10+.

```bash
python senha_segura.py
```

## 🧪 Testes

Os testes usam a biblioteca padrão `unittest`.

```bash
python -m unittest discover -s tests -v
```

## 🔄 Integração contínua

O GitHub Actions executa os testes automaticamente em pushes para `main` e em pull requests.

## 📁 Estrutura

```text
lab-sandbox/
├── .github/
│   └── workflows/
│       └── tests.yml
├── tests/
│   └── test_senha_segura.py
├── .gitignore
├── LICENSE
├── README.md
└── senha_segura.py
```

## 📚 Conceitos praticados

**Python**
- funções;
- type hints;
- dicionários;
- validação de tipos;
- interface de linha de comando.

**Engenharia de Software**
- separação entre lógica e apresentação;
- testes automatizados;
- documentação;
- CI;
- código reutilizável.

**Segurança**
- avaliação básica de requisitos de senha;
- princípio de não expor a credencial analisada;
- diferença entre heurística e avaliação de segurança real.

## 🚀 Próximos experimentos

- adicionar métricas de entropia de forma responsável;
- separar o domínio da interface de linha de comando;
- criar validações configuráveis;
- experimentar análise de logs e tratamento seguro de dados;
- explorar conceitos de autenticação e armazenamento seguro de credenciais.

## 👩‍💻 Autora

**Marcella Bongiolo**

Repositório voltado à prática de programação e fundamentos de Engenharia de Software.

## 📄 Licença

Distribuído sob a licença MIT.

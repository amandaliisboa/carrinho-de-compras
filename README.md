# 🛒 Carrinho de Compras em Python

Sistema de carrinho de compras via terminal, desenvolvido em Python como projeto de estudo. Permite visualizar catálogo de produtos, adicionar itens ao carrinho, calcular o valor total e aplicar cupom de desconto.

## 📋 Funcionalidades

- **Ver catálogo** — lista todos os produtos disponíveis com seus preços
- **Adicionar produto ao carrinho** — busca o produto no catálogo e adiciona (com limite de tentativas em caso de erro)
- **Ver carrinho e valor total** — mostra os itens adicionados e soma o valor total da compra
- **Aplicar cupom de desconto** — aplica 10% de desconto com o cupom `PYTHON10` (com controle para não usar o mesmo cupom duas vezes)
- **Finalizar compra** — encerra o programa

## 🧠 Conceitos praticados

- Estruturas de repetição (`while`, `for`)
- Estruturas condicionais (`if`, `elif`, `else`)
- Dicionários e listas
- Tratamento de erros (`try`/`except`)
- Funções
- `set()` para controle de itens únicos (cupons usados)

## ▶️ Como rodar o projeto

1. Certifique-se de ter o Python instalado ([python.org](https://www.python.org/downloads/))
2. Clone este repositório ou baixe o arquivo `.py`
3. No terminal, navegue até a pasta do projeto e execute:

```bash
python carrinho_de_compras.py
```

4. Use o menu numérico (1 a 5) para navegar pelas opções

## 💡 Exemplo de uso

```
[1] Ver catálogo
[2] Adicionar produto ao carrinho
[3] Ver carrinho e valor total
[4] Aplicar cupom de desconto
[5] Finalizar compra / Sair

Opção: 1
['camiseta', 'calca', 'tenis', 'bone']
camiseta - 49.90
calca - 120.00
tenis - 250.00
bone - 29.90
```

## 🚀 Sobre este projeto

Este é um dos projetos que venho desenvolvendo enquanto estudo Python e Análise e Desenvolvimento de Sistemas.

---

Feito com 🐍 Python
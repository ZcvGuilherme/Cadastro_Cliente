# Aplicação Web de cadastro de clientes e produtos

Sistema de gerenciamento e cadastro de produtos e clientes utilizando o framework Flask para a web, SQLite para banco de dados e Python como linguagem dominante, visando aplicar a arquitetura MVC (Model-View-Controller).

## 🚀 Funcionalidades 
- Cadastro de clientes de produtos
- Persistência dos dados com SQLite
- Interface simples e interativa para manusear

## 🛠 Tecnologias Utilizadas
- Python
- SQLite
- Flask
- HTML/JS/CSS

## 📁 Estrutura do projeto

```markdown
Cadastro/
├──app/
│  ├── static
│  │ ├── imagem
│  │   └── png's
│  │ ├── client.js
│  │ ├── product.js
│  │ └──style.css
│  ├── templates
│  │  ├── cadastrar_cliente.html
│  │  ├── cadastrar_produto.html
│  │  ├── gerenciar_cliente.html
│  │  ├── gerenciar_produto.html
│  │  └── index_navegação.html
│  ├── controller.py
│  ├── models.py
│  └──views.py
├── banco_produto.db
├── cadastro_clientes.db
├── main.py
├── requeriments.txt
└── Readme.md
```

## ⚙️ Como executar o Projeto

1. Clone o repositório:
```
git clone https://github.com/ZcvGuilherme/Cadastro_Cliente.git
cd Cadastro_Cliente
```
2. Crie um ambiente virtual (opcional):
  ```bash
  python -m venv venv
  source venv/bin/activate  # No Windows: venv\Scripts\activate
  ```
3. instale as dependencias:
  ```bash
  pip install -r requeriments.txt
  ```
4. execute a aplicação:
  ```bash
  python main.py
  ```

## ✨ Contribuições
Esse projeto foi projetado e desenvolvido por:
- [![GitHub: ZcvGuilherme](https://img.shields.io/github/followers/ZcvGuilherme?label=follow&style=social)](https://github.com/ZcvGuilherme)

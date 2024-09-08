# Kaggle Extract and Analysis

# Como instalar as dependencias do projeto
Primeiro, instale o [Poetry](https://python-poetry.org/), ele é usado em todo o projeto para gerenciar as dependencias
```bash
pip install poetry
```

Agora, com o `poetry` instalado precisa instalar os pacotes que estão em `pyproject.toml` e criar um ambiente virtual
```bash
poetry install
```

Com o ambiente criado e os pacotes instalados precisa baixar os dados do kaggle, para isso, vai precisar autenticar com a API do Kaggle.

Agora precisa baixar [suas credenciais](https://www.kaggle.com/settings/account) (create new token) e colocar em `C:\Users\<usuário>\.kaggle\kaggle.json`.

Agora rode o projeto

```bash
cd etl
poetry run python main.py
```

Com os dados baixados e extraídos, pode iniciar a analise.
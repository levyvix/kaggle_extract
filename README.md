# kaggle_extract


Primeiro, visite a documentação do Kaggle API para obter as credenciais de autenticação.
[Kaggle Docs](https://www.kaggle.com/docs/api#:~:text=for%20that%20command.-,Interacting%20with%20Datasets,-The%20Kaggle%20API)

Depois, instale a biblioteca kaggle para poder utilizar a API.
```bash
pip install kaggle
```

Agora precisa baixar [suas credenciais](https://www.kaggle.com/settings/account) (create new token) e colocar em `C:\Users\<usuário>\.kaggle\kaggle.json`.

Agora rode o projeto

```bash
cd etl
python main.py
```

# IMPORTANTE

Os dados de `brazil_population_2019.csv` tem um problema que impede que ele seja lido

para resolver, precisa abrir o arquivo csv, ir na linha 1282 e apagar as colunas extras "Entorno...". Seleciona até a virgula, aperta Ctrl+h e clica em "replace all" (segunda caixinha)


Os dados ficam disponiveis em `data/`
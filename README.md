# kaggle_extract


Primeiro, visite a documentação do Kaggle API para obter as credenciais de autenticação.
[Kaggle Docs](https://www.kaggle.com/docs/api#:~:text=for%20that%20command.-,Interacting%20with%20Datasets,-The%20Kaggle%20API)

Depois, instale a biblioteca kaggle para poder utilizar a API.
```bash
pip install kaggle
```

Agora, você pode utilizar a API para baixar os datasets do Kaggle.
```python
from kaggle.api.kaggle_api_extended import KaggleApi

api = KaggleApi()

api.authenticate() # Autenticação

api.dataset_download_files('shivan118/healthcare-analytics') # Download do dataset
```

Agora, você pode utilizar o dataset baixado para realizar suas análises.
```python
import pandas as pd

df = pd.read_csv('healthcare-analytics.zip') # Leitura do dataset
```

Pronto! Agora você pode utilizar o dataset para realizar suas análises.
```

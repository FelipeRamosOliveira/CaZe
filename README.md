## O PROBLEMA

Este projeto foi baseado na competição de Precificação de Casas (Housing Prices Competition for Kaggle Learn Users) do [Kaggle](https://www.kaggle.com/competitions/home-data-for-ml-course).

O projeto explora os seguintes tópicos:

- aprendizado de máquina
- programação orientada a objetos
- docker
- APIs
- feature store.

**CONJUNTO DE DADOS**

O conjunto de dados da Ames Housing foi compilado por Dean De Cock para uso na educação em ciência de dados. É uma alternativa incrível para cientistas de dados que procuram uma versão modernizada e expandida do conjunto de dados do Boston Housing frequentemente citado.

**META**

O objetivo desse projeto é prever o preço de venda de casas.

---

## COMO EXECUTAR O PROJETO

Primeiro clone o repositório com o comando :

```yml
git clone https://github.com/FelipeRamosOliveira/CaZe.git
```

Em seguida execute o Makefile com o comando:

```yml
make
```

Para executar a API entre na pasta `src api/` e digite o comando:

```yml
docker-compose build
```

Em seguida execute:

```yml
docker-compose up
```

Por padrão a porta de comunicação com a API é a `5002`

---

## DIRETÓRIOS

O projeto está dividido em :

```
.
├── notebooks   --> Contem os códigos utilizados para análise de dados e construção de modelo.
├── src         --> Scripts utlizados para construção da API
│   └──  app.py
└── volume      --> Contem o banco de dados utlizados
    └── db.sqlite
```

---

## CAMPOS DE DADOS

Aqui está uma breve descrição dos campos de entrada da API.

- Neighborhood: locais físicos dentro dos limites da cidade de Ames. Possíveis valores:

```yml
['CollgCr' 'Veenker' 'Crawfor' 'NoRidge' 'Mitchel' 'Somerst' 'NWAmes' 'OldTown' 'BrkSide' 'Sawyer' 'NridgHt' 'NAmes' 'SawyerW' 'IDOTRR' 'MeadowV' 'Edwards' 'Timber' 'Gilbert' 'StoneBr' 'ClearCr' 'NPkVill''Blmngtn' 'BrDale' 'SWISU' 'Blueste']
```

- ExterQual: Qualidade do material exterior. Possíveis valores:

```yml
['Gd' 'TA' 'Ex' None 'Fa']
```

- BsmtQual: Altura do porão. Possíveis valores:

```yml
['Ex' 'Gd' 'TA' 'Fa' 'Po']
```

- HeatingQC: Qualidade e condição de aquecimento. Possíveis valores:

```yml
['Ex' 'Gd' 'TA' 'Fa' 'Po']
```

- CentralAir: Ar condicionado central. Possíveis valores:

```yml
['Y' 'N']
```

- KitchenQual: Qualidade da cozinha. Possíveis valores:

```yml
['Gd' 'TA' 'Ex' 'Fa']
```

- Qualidade geral: qualidade geral do material e do acabamento. Possíveis valores:

```yml
['RFn' 'Unf' 'Fin' None]
```

- Ano de construção: data de construção original
- MasVnrArea: Área de folheado de alvenaria em pés quadrados
- BsmtFinSF1: Tipo 1 pés quadrados acabados
- TotalBsmtSF: Total de pés quadrados da área do porão
- 1stFlrSF: Primeiro andar pés quadrados
- 2ndFlrSF: Segundo andar pés quadrados
- GrLivArea: Área de estar acima do nível (solo) pés quadrados
- FullBath: banheiros completos acima do nível
- TotRmsAbvGrd: Total de quartos acima do nível (não inclui banheiros)
- GarageYrBlt: Ano em que a garagem foi construída
- GarageCars: Tamanho da garagem em capacidade do carro
- GarageArea: Tamanho da garagem em pés quadrados

---

## PREVISÃO DE VALOR

Abaixo segue um exemplo de como relizar uma previsão via API:

```python
import requests
import json

url = f"{host}/predict"

payload = json.dumps({
"Neighborhood": "CollgCr",
"ExterQual": "Gd",
"BsmtQual": "Gd",
"HeatingQC": "Ex",
"CentralAir": "Y",
"KitchenQual": "Gd",
"GarageFinish": "RFn",
"OverallQual": 7,
"YearBuilt": 2003,
"MasVnrArea": 196,
"BsmtFinSF1": 706,
"TotalBsmtSF": 856,
"1stFlrSF": 856,
"2ndFlrSF": 854,
"GrLivArea": 1710,
"FullBath": 2,
"TotRmsAbvGrd": 8,
"GarageYrBlt": 2003,
"GarageCars": 2,
"GarageArea": 548
})
headers = {
'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

Resposta esperada :

```json
{ "house value": "203675.86" }
```

## DETALHES DO MODELO

Abaixo segue um exemplo de como consultar os detalhes do modelo via API:

```python
import requests

url = f"{host}/details"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

```

Resposta esperada :

```json
{
  "model details": "Pipeline(steps=[('columntransformer ..."
}
```

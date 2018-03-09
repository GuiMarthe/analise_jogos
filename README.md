Análise de vendas de Video Games
==============================

Análise de vendas de jogos de video games com no mínimo 100 mil cópias vendidads. 

### Algumas perguntas preliminares
- a decisão de se concentrar a publicação em menos gêneros afeta o resultado global de unidades vendidas de uma produtora?
- como se comporta o tempo de decadência de uma plataforma?
- dentre as franquias identificadas, quais são aquelas que são mais bem sucedidas?
- dentre as franquias identificadas, quais são aquelas que estão em crescimento ao longo do tempo? E quais estão em decrescimento?

Os scripts em Python, localizados em src/data são responsáveis por limpar os dados provindos das tabelas da wikipedia.

Basta roda-los a partir do topo do projeto.


Project Organization
------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks or RMD notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

Este projeto é uma API backend desenvolvida em Python utilizando o framework FastAPI. O sistema gerencia o cadastro de veículos em uma oficina mecânica, seguindo a arquitetura de 3 camadas (Model, Service, Controller).

Tecnologias
- Python
- FastAPI
- SQLAlchemy (SQLite)

Estrutura
O projeto respeita a arquitetura MVC/3 Camadas:
- Model: Representação da tabela de veículos.
- Service: Lógica de negócio (validação de placa única).
- Controller: Rotas da API (POST e GET).

Como rodar o projeto

1. Instale as dependências:

bash
pip install -r requirements.txt

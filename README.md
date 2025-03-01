Locadora de Filmes em Django
Este projeto é uma aplicação web simples para gerenciar uma locadora de filmes. Ele utiliza o framework Django para criar um CRUD (Create, Read, Update, Delete) de filmes, além de consumir a API do OMDb para buscar informações sobre filmes.

Características
CRUD de Filmes: Permite criar, ler, atualizar e deletar filmes.

Consumo da API do OMDb: Busca informações sobre filmes usando a API do OMDb.

Interface Web: Utiliza templates HTML para renderizar as páginas da aplicação.

Banco de Dados SQLite: Armazena os dados dos filmes em um banco de dados SQLite.

Requisitos
Python 3.11+

Django 5.1.6

requests 2.29.0

Chave de API do OMDb

Instalação

Lista de Filmes: Visualize todos os filmes cadastrados.

Novo Filme: Adicione um novo filme manualmente.

Editar Filme: Atualize informações de um filme existente.

Excluir Filme: Remova um filme do banco de dados.

Buscar Filmes na API do OMDb: Busque filmes usando a API do OMDb e adicione-os ao banco de dados.

Contribuição
Contribuições são bem-vindas! Se você tiver alguma ideia ou encontrar um bug, por favor, abra uma issue ou envie um pull request.

Como Rodar o Projeto
Clone este repositório:
git clone https://github.com/bernardoaquino28/wsBackend-Fabrica25.1
Crie e ative um ambiente virtual utilizando o venv:
python -m venv venv
venv/Scripts/activate  # Para Windows
Caso você enfrente algum erro ao tentar ativar o ambiente virtual, execute o seguinte comando no PowerShell para alterar a política de execução:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Instale as dependências listadas no arquivo requirements.txt:
pip install -r requirements.txt
Realize as migrações do banco de dados:
python manage.py migrate
Inicie o servidor de desenvolvimento:
python manage.py runserver
Acesse http://localhost:8000/filmes/ para usar a aplicação.
Abra a sua IDE de preferência (como PyCharm, VS Code, etc.) para editar o código, realizar melhorias, e monitorar a aplicação.
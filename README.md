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

Funcionalidades
Lista de Filmes: Visualize todos os filmes cadastrados.

Novo Filme: Adicione um novo filme manualmente.

Editar Filme: Atualize informações de um filme existente.

Excluir Filme: Remova um filme do banco de dados.

Buscar Filmes na API do OMDb: Busque filmes usando a API do OMDb e adicione-os ao banco de dados.

Como Rodar o Projeto
Clone o Repositório:

bash
git clone https://github.com/bernardoaquino28/wsBackend-Fabrica25.1
Crie e Ative um Ambiente Virtual:

bash
python -m venv myenv
myenv\Scripts\activate  # No Windows
# ou source myenv/bin/activate # No Linux/Mac
Se necessário, altere a política de execução no PowerShell com:

powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Instale as Dependências:

bash
pip install -r requirements.txt
Realize as Migrações do Banco de Dados:

bash
python manage.py migrate
Inicie o Servidor de Desenvolvimento:

bash
python manage.py runserver
Acesse a Aplicação:
Acesse http://localhost:8000/filmes/ para usar a aplicação.

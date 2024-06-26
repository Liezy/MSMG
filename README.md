# MSMG - Management System for Musical Groups

![Python](https://img.shields.io/badge/python-3.9-blue.svg)
![Django](https://img.shields.io/badge/django-4.0.1-green.svg)
![Bootstrap](https://img.shields.io/badge/bootstrap-5.3.0-purple.svg)

## Sobre o Projeto

Este é um projeto desenvolvido para a disciplina de Desenvolvimento Web Mobile da Universidade Federal do Tocantins. O MSMG visa criar uma plataforma web para auxiliar grupos musicais na organização e gerenciamento de shows e eventos.

## Universidade Federal do Tocantins

- **Curso**: Bacharelado em Ciência da Computação
- **Professor**: Thiago Magalhães
- **Aluno**: Eliézer Alencar Moreira

## Funcionalidades Principais

- Cadastro de grupos musicais com informações detalhadas.
- Gestão de eventos com adição de músicas, funções dos membros e detalhes do local.
- Armazenamento do repertório musical com áudio, letra, cifra e vídeo.

## Tecnologias Utilizadas

- [Python 3.9](https://www.python.org/)
- [Django 4.0.1](https://www.djangoproject.com/)
- [Bootstrap 5.3.0](https://getbootstrap.com/)
- Banco de Dados: SQLite (para ambiente de desenvolvimento)

## Como Executar o Projeto

### Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.9](https://www.python.org/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

### Passo a Passo

1. **Clone o repositório**
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    ```

2. **Navegue até o diretório do projeto**
    ```bash
    cd msmg-project
    ```

3. **Crie e ative o ambiente virtual**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use venv\Scripts\activate
    ```

4. **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

5. **Configure o banco de dados**
    - Configure as variáveis de ambiente ou diretamente no arquivo `settings.py`.

6. **Aplique as migrações do banco de dados**
    ```bash
    python manage.py migrate
    ```

7. **Inicie o servidor de desenvolvimento**
    ```bash
    python manage.py runserver
    ```

8. **Acesse o sistema no navegador**
    ```
    http://127.0.0.1:8000/
    ```

## Contato

**Eliézer Alencar Moreira**  
Email: [eliezer.alencar@uft.edu.br](mailto:eliezer.alencar@uft.edu.br)

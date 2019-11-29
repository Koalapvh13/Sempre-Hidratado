# Sempre-Hidratado
## Descrição
O site Sempre Hidratado faz parte de um sistema de controle de galões d'água utilizando Arduino e sensores de umidade.

Este sistema foi apresentado como exigência parcial para obtenção de nota referente ao 4º período nas matérias de Fundamentos de Programação Web e Internet das Coisas (IoT) do CST em Análise e Desenvolvimento de Sistemas do IFRO Porto Velho Calama.

Para acessar um exemplo do sistema acesse: https://sempre-hidratado.herokuapp.com/

## Stack de Desenvolvimento
- Python 3.7
- Web Framework Django 2.1
- Twitter Bootstrap 4.1

## Como Instalar o Projeto em Ambiente de Desenvolvimento
- Clone o projeto para sua máquina;
- Recomenda-se a criação de um ambiente virtual (Virtualenv) para o trabalho com o SysBettina. Utilize o comando ```python -m venv NomeDoSeuAmbiente``` para criar a sua virtualenv.
- Para ativar a virtualenv utilize o comando ```NomeDoSeuAmbiente\Scripts\activate.bat```.
- Após a ativação do ambiente utilize ```pip install -r requeriments.txt``` para instalar as dependências necessárias.

## Criar o Usuário Admin
- Usando o Terminal, acesse a pasta onde se encontra o projeto.
- Rode o comando ```python manage.py makemigrations``` para estruturar o banco de dados e o comando ```python manage.py migrate``` para salvar as mudanças.
- Crie um novo usuário master ulizando ```python manage.py createsuperuser```. forneça todas as informações solicitadas.
- Para rodar a aplicação inicie o servidor local com o comando ```python manage.py runserver```.

## Desenvolvedores
- [Matheus Dias Vieira](http://twitter.com/koalapvh13)
- [Bruno Felipe](http://github.com/agentecaveira)
- [Helenice Saldanha](http://github.com)

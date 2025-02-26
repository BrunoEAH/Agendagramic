TAREFAS:
- Conectar a agenda com o banco de dados:
    - Editar eventos;
    - Editar tarefas;
    - Listar tarefas e eventos na agenda.
- Deploy do banco de dados.

EXTENÕES USADAS:
- Python Telegram Bot API
- Nuxt.js (Framework principal)
- Node.js e Express
- Tailwind CSS (Framework de CSS)
- Axios (Para requisições HTTP)
- PostCSS (Para processamento de CSS com Autoprefixer e Tailwind)
- @types/node (Para garantir a compatibilidade com tipos Node.js)
- npm install firebase (autenticar usu'rios em json
- Mariadb
- Python FLASK

ACESSO AO TELEGRAM
- Arquivo .env
__________________________________________________________________________________________

ACESSO PADRÃO DA PÁGINA:
http://localhost:3000

SERVIDOR NODE 
http://localhost:3001

Autenticar no servidor (receber get)
Problema: Servidor ainda é local, não sei se o bot ou o telegram vai ter acesso.

CONSTRUIR E RODAR O DOCKER:

docker-compose up --build

RODAR O DOCKER:

docker-compose up

PARAR O DOCKER:

docker-compose down

TESTAR O BOT:

- Evento : 
    - começar com /event
    - escrever nesse formato:  DD/MM/YY HH:MM-HH:MM Info 

- Tarefa:
    - começar com /task
    - escreve nesse formato: DD/MM/YY HH:MM Info
    - Exemplo: 10/03/2024 13:20 Fazer licao

- Lista:
    - enviar /lista

BANCO DE DADOS:

-  Alterar os dados no arquivo server/config/database.js para utilizar o banco de dados local;

- Inserir dados padrões no banco de dados antes de enviar tarefas, EXEMPLO DE COMANDO:
    USE agendagramic;
    INSERT INTO Grupos (grupo_id , nome , admin , criado_em)
    VALUES (1,'@UsuarioTelegram','@UsuarioTelegram',NOW());

- Instalar mariadb ( npm install mariadb --save-dev)

EXECUÇÃO DE TESTES:

- Instalar as dependências:
pip install selenium pytest pytest-html webdriver-manager

- Verificar se foram instaladas corretamente:
pip show selenium pytest pytest-html webdriver-manager

- Para executar todos os testes, utilize:
npm run dev;
ou
python -m pytest testes

- Executar um Teste Específico: por exemplo, para rodar apenas test_exemple.py:
python -m pytest testes/test_exemple.py

- Executar uma Função de Teste específica dentro de um arquivo: Por exemplo, para rodar apenas test_navigation_to_profile dentro de test_exemple.py:
python -m pytest testes/test_exemple.py::test_navigation_to_profile

LISTAR TAREFAS, EVENTOS E GRUPOS:
- python Agendagramic-Nuxt/server/api/getGTE.py




TAREFAS:
- Conectar a agenda com o banco de dados:
    - Login;
    - Editar eventos;
    - Editar tarefas;
    - Tarefas [Bruno Rocha];
    - Eventos [Bruno Rocha];
    - Grupos;
    - Organizar prioridade das tarefas.
- Bot do telegram:
    - Conexão do usuário [Rafael Navarro];
    - Conexão das tarefas[Rafael Navarro];
    - Conexão dos eventos[Rafael Navarro];
    - Listas eventos e tarefas;
    - Analisar o status do usuário [Bruno Hayek];
    - Analisar votação [Bruno Hayek];
    - Analisar a prioridade das tarefas [Bruno Hayek].
- Deploy do banco de dados.

AJUSTES FUTUROS:
1. Funcoes para o bot copiar o evento/tarefa do usuario para algum arquivo JSON; 
2. API para o a aplicacao ler esse arquivo JSON e mostrar no site;
3. Bot copiar resultado da pesquisa,processar,responder e armazena no JSON;
4. Elaborar a interface do site;
5. Menu do bot; [Bruno]
6. Elaborar a pagina de login.

EXTENÕES USADAS:
- Python Telegram Bot API
- Nuxt.js (Framework principal)
- Node.js e Express
- Tailwind CSS (Framework de CSS)
- Axios (Para requisições HTTP)
- PostCSS (Para processamento de CSS com Autoprefixer e Tailwind)
- @types/node (Para garantir a compatibilidade com tipos Node.js)
- npm install firebase (autenticar usu'rios em json

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






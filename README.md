AJUSTES FUTUROS:
1. Funcoes para o bot copiar o evento/tarefa do usuario para algum arquivo JSON;
2. API para o a aplicacao ler esse arquivo JSON e mostrar no site;
3. Bot copiar resultado da pesquisa,processar,responder e armazena no JSON;
4. Elaborar a interface do site;
5. Menu do bot;
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

Autenticar no servidor (eceber get)
Problema: Servidor ainda é local, não sei se o bot ou o telegram vai ter acesso.



TODO:

- Ajustar bot do telegram para ler inputs do usuário de diferentes formatos, usando 2:00 PM ao invés de 14:00 por exemplo.
- Fazer API do JSON para a agenda. 

TESTAR O BOT:

- Evento : 
    - começar com /event
    - escrever nesse formato:  DD/MM/YY HH:MM-HH:MM Info 

-Tarefa:
    -começar com /task
    -escreve nesse formato: DD/MM/YY HH:MM Info
    -Exemplo: 10/03/2024 13:20 Fazer licao
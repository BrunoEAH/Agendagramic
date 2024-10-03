import express from 'express';
import fs from 'fs';
import path from 'path';
import bodyParser from 'body-parser';
import { fileURLToPath } from 'url';

// Resolver __dirname manualmente
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const app = express();
app.use(bodyParser.json());

// Definir o caminho do arquivo users.json
const filePath = path.join(__dirname, 'users.json');

// Função auxiliar para ler o arquivo JSON
const readUsers = () => {
  try {
    const data = fs.readFileSync(filePath, 'utf-8');
    return JSON.parse(data).users;
  } catch (error) {
    return [];
  }
};

// Função auxiliar para escrever no arquivo JSON
const writeUsers = (users) => {
  fs.writeFileSync(filePath, JSON.stringify({ users }, null, 2));
};

// Rota de cadastro
app.post('/signup', (req, res) => {
  const { name, email, password } = req.body;
  const users = readUsers();
  const userExists = users.find((user) => user.email === email);

  if (userExists) {
    return res.status(400).json({ message: 'Usuário já existe' });
  }

  users.push({ name, email, password });
  writeUsers(users);
  res.status(201).json({ message: 'Usuário cadastrado com sucesso!' });
});

// Rota de login
app.post('/login', (req, res) => {
  const { email, password } = req.body;
  const users = readUsers();
  const user = users.find((user) => user.email === email && user.password === password);

  if (!user) {
    return res.status(401).json({ message: 'Email ou senha inválidos' });
  }

  res.status(200).json({ message: 'Login bem-sucedido!', user });
});

// Iniciar o servidor
app.listen(3001, () => {
  console.log('Servidor rodando na porta 3001');
});

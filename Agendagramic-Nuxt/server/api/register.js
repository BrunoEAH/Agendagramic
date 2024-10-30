// Importa os módulos necessários
const express = require('express');
const mariadb = require('mariadb');
const bcrypt = require('bcrypt');

const router = express.Router();

// Configura o pool de conexão com MariaDB
const pool = mariadb.createPool({
  host: 'localhost',
  user: 'seu-usuario',
  password: 'sua-senha',
  database: 'agendagramic',
  connectionLimit: 5,
});

// Endpoint de cadastro
router.post('/api/register', async (req, res) => {
  const { name, email, password } = req.body;

  try {
    const connection = await pool.getConnection();

    // Verifica se o email já está registrado
    const existingUser = await connection.query('SELECT * FROM users WHERE email = ?', [email]);
    if (existingUser.length > 0) {
      return res.status(400).json({ success: false, message: 'Email já cadastrado' });
    }

    // Faz o hash da senha antes de salvar no banco
    const hashedPassword = await bcrypt.hash(password, 10);

    // Insere o novo usuário no banco de dados
    await connection.query('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', [name, email, hashedPassword]);

    res.status(201).json({ success: true, message: 'Cadastro realizado com sucesso!' });
  } catch (error) {
    console.error('Erro no cadastro:', error);
    res.status(500).json({ success: false, message: 'Erro no servidor. Tente novamente mais tarde.' });
  }
});

module.exports = router;

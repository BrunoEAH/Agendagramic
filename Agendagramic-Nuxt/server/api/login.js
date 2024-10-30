// Importa os módulos necessários
const express = require('express');
const mariadb = require('mariadb');
const jwt = require('jsonwebtoken');
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

// Endpoint de login
router.post('/api/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    const connection = await pool.getConnection();

    // Consulta o usuário com o email fornecido
    const rows = await connection.query('SELECT * FROM users WHERE email = ?', [email]);
    if (rows.length === 0) {
      return res.status(401).json({ message: 'Usuário não encontrado' });
    }

    const user = rows[0];

    // Verifica a senha
    const match = await bcrypt.compare(password, user.password);
    if (!match) {
      return res.status(401).json({ message: 'Senha incorreta' });
    }

    // Gera um token JWT
    const token = jwt.sign({ id: user.id, email: user.email }, 'seu-segredo-jwt', { expiresIn: '1h' });

    res.json({ token });
  } catch (error) {
    res.status(500).json({ message: 'Erro no servidor' });
  }
});

module.exports = router;

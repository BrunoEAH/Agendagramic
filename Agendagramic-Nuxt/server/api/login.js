import pool from '~/server/config/database';
import jwt from 'jsonwebtoken';
import bcrypt from 'bcrypt';

// Endpoint de login
export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const { email, password } = body;

  if (!email || !password) {
    return { statusCode: 400, message: 'Email e senha são obrigatórios' };
  }


  let connection;
  try {
    connection = await pool.getConnection();

    // Consulta o usuário com o email fornecido
    const rows = await connection.query('SELECT * FROM Usuario WHERE email = ?', [email]);
    if (rows.length === 0) {
      return { statusCode: 401, message: 'Usuário não encontrado' };
    }

    const user = rows[0];

    // Verifica a senha
    const match = await bcrypt.compare(password, user.password);
    if (!match) {
      return { statusCode: 401, message: 'Senha incorreta' };
    }

    // Gera um token JWT
    const token = jwt.sign({ userTelegram: user.user_telegram, email: user.email }, 'seu-segredo-jwt', { expiresIn: '1h' });

    // Retorna o token e o nome do usuário
    return { success: true, 
              token, 
              userName: user.nome, 
              userTelegram: user.user_telegram 
            };

  } catch (error) {
    console.error('Erro em buscar os dados:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Falha ao buscar os dados',
      data: error.message,
    });
  } finally {
    if (connection) connection.release(); 
  }
});

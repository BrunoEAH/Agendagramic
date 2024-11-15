import pool from '~/server/config/database';
import jwt from 'jsonwebtoken';

export default defineEventHandler(async (event) => {
  try {
    // Obtém o token JWT do cabeçalho de autorização
    const token = event.req.headers.authorization?.split(' ')[1];
    if (!token) {
      throw createError({ statusCode: 401, statusMessage: 'Token não fornecido' });
    }

    // Decodifica o token JWT para obter o email do usuário
    const decoded = jwt.verify(token, 'seu-segredo-jwt');
    const email = decoded.email;

    // Consulta o banco de dados para buscar o nome do usuário
    const connection = await pool.getConnection();
    const [user] = await connection.query('SELECT nome FROM Usuario WHERE email = ?', [email]);
    connection.release();

    if (!user) {
      throw createError({ statusCode: 404, statusMessage: 'Usuário não encontrado' });
    }

    // Retorna o nome do usuário
    return { userName: user.nome };

  } catch (error) {
    console.error('Erro ao buscar o nome do usuário:', error);
    throw createError({ statusCode: 500, statusMessage: 'Erro ao buscar o nome do usuário' });
  }
});

import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  try {
    const connection = await pool.getConnection();
    const [users] = await connection.query('SELECT user_telegram, nome AS name FROM Usuario');
    connection.release();
    return { users };
  } catch (error) {
    console.error('Erro ao buscar usuários:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao buscar usuários',
      data: error.message,
    });
  }
});

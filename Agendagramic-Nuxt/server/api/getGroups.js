import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const userTelegram = getQuery(event).userTelegram;

  if (!userTelegram) {
    throw createError({
      statusCode: 400,
      statusMessage: 'UserTelegram is missing',
    });
  }

  try {
    const connection = await pool.getConnection();
    const [groups] = await connection.query(
      'SELECT group_id, nome AS group_name FROM Grupos WHERE admin = ?',
      [userTelegram]
    );
    connection.release();
    return { groups };
  } catch (error) {
    console.error('Erro ao buscar grupos:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao buscar grupos',
      data: error.message,
    });
  }
});

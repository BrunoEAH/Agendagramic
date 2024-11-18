import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const { userTelegram, selectedDate } = getQuery(event);

  if (!userTelegram || !selectedDate) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Parâmetros obrigatórios ausentes',
    });
  }

  let connection;
  try {
    connection = await pool.getConnection();
    console.log('Conexão com o banco de dados estabelecida.');

    const query = `
      SELECT 
        event_id, titulo, descricao, local, data, horario, criado_por, criado_em
      FROM Eventos
      WHERE criado_por = ? AND DATE(data) = ?
    `;

    const [events] = await connection.query(query, [userTelegram, selectedDate]);

    console.log('Eventos retornados do banco de dados:', events);

    return { success: true, events: events || [] }; // Garante um array vazio
  } catch (error) {
    console.error('Erro ao buscar eventos:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao buscar eventos.',
      data: error.message,
    });
  } finally {
    if (connection) {
      connection.release();
      console.log('Conexão com o banco de dados liberada.');
    }
  }
});

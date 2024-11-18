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
        task_id, titulo, info_task, data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em
      FROM Tarefas
      WHERE criado_por = ? AND DATE(data) = ?
    `;

    const [tasks] = await connection.query(query, [userTelegram, selectedDate]);

    console.log('Tarefas retornadas do banco de dados:', tasks);

    return { success: true, tasks: tasks || [] }; // Garante um array vazio
  } catch (error) {
    console.error('Erro ao buscar tarefas:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao buscar tarefas.',
      data: error.message,
    });
  } finally {
    if (connection) {
      connection.release();
      console.log('Conexão com o banco de dados liberada.');
    }
  }
});

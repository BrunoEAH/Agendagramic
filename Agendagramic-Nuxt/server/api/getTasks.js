import { defineEventHandler, getQuery } from 'h3';
import db from '../config/database.js';

export default defineEventHandler(async (event) => {
  const { userTelegram } = getQuery(event);
  let connection;

  try {
    connection = await db.getConnection(); // Obtenha uma conexão do pool
    const [tasks] = await connection.query(
      'SELECT task_id, titulo AS name, info_task AS description, data, esta_completa, prioridade FROM Tarefas WHERE criado_por = ?',
      [userTelegram]
    );
    return { success: true, tasks };
  } catch (error) {
    console.error('Erro ao buscar tarefas:', error);
    throw createError({ statusCode: 500, message: 'Erro ao buscar tarefas.' });
  } finally {
    if (connection) connection.release(); // Libere a conexão após o uso
  }
});

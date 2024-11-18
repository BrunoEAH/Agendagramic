import { defineEventHandler, getQuery } from 'h3';
import pool from '../config/database.js';

export default defineEventHandler(async (event) => {
  const query = getQuery(event);
  const userTelegram = query.userTelegram;
  
  let connection;


  if (!userTelegram) {
    throw createError({
      statusCode: 400,
      statusMessage: 'UserTelegram is missing',
    });
  }

  try {
    connection = await pool.getConnection();
    const [tasks] = await connection.query(
      'SELECT task_id, titulo AS name, info_task AS description, data as date, esta_completa AS status, prioridade AS priority FROM Tarefas WHERE criado_por = ?',
      [userTelegram]
    );
    return { success: true, tasks };
  } catch (error) {
    console.error('Erro ao buscar tarefas:', error);
    throw createError({ statusCode: 500, message: 'Erro ao buscar tarefas.' });
  } finally {
    if (connection) connection.release(); 
  }
});

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
    const [events] = await connection.query(
      'SELECT event_id, titulo AS name,info_evento AS description,comeco AS date_begin,fim AS date_end, group_id AS id_group,esta_completa as status, criada_em AS createdAt FROM Eventos WHERE criado_por = ?',
      [userTelegram]
    );
    return { success: true, events };
  } catch (error) {
    console.error('Erro ao buscar eventos:', error);
    throw createError({ statusCode: 500, message: 'Erro ao buscar eventos.' });
  }
});

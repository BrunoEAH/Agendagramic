import { defineEventHandler, getQuery } from 'h3';
import db from '../config/database.js';

export default defineEventHandler(async (event) => {
  const { userTelegram } = getQuery(event);

  try {
    // Consulta ajustada com os nomes corretos das colunas
    const [events] = await db.execute(
      `SELECT 
        event_id, 
        titulo AS name, 
        descricao AS description, 
        local AS location, 
        data AS eventDate, 
        horario AS eventTime, 
        criado_em AS createdAt 
      FROM Eventos 
      WHERE criado_por = ?`,
      [userTelegram]
    );
    return { success: true, events };
  } catch (error) {
    console.error('Erro ao buscar eventos:', error);
    throw createError({ statusCode: 500, message: 'Erro ao buscar eventos.' });
  }
});

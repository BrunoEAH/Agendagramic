
import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {eventTitle,eventDescription,eventBeginDateTime,eventEndDateTime,eventGroup,eventCreator,eventStatus} = body;

  const groupId = eventGroup && eventGroup.length > 0 ? eventGroup : null;

  let connection;
  try {
    // Conexao
    connection = await pool.getConnection();

    const result = await connection.query(
      'INSERT INTO Eventos (event_id,titulo,info_evento,comeco,fim,group_id,criado_por,esta_completa,criada_em) VALUES (UUID(),?,?,?,?,?,?,?,NOW())',
      [eventTitle,eventDescription,eventBeginDateTime,eventEndDateTime,groupId,eventCreator,eventStatus]
    );

    return { success: true, insertId: result.insertId.toString() };
  } catch (error) {
    console.error('Error inserting data:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Failed to insert data',
      data: error.message,
    });
  } finally {
    if (connection) connection.release(); 
  }
});

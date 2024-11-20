
import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {eventTitle,eventDescription,eventBeginDateTime,eventEndDateTime,eventGroup,eventCreator,eventStatus} = body;

  let connection;
  let groupId = null;
  console.log(eventGroup);
  try {
    // Conexao
    connection = await pool.getConnection();

    if(eventGroup){
      const [groupResult] = await connection.query(
        'SELECT group_id AS id_group FROM Grupos WHERE admin = ? AND nome = ?',
        [eventCreator,eventGroup]
      );
      console.log(groupResult)
      groupId = groupResult.id_group;
      
    }

    console.log(groupId);

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

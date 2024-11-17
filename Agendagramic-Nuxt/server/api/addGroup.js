import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {groupName,groupAdmin} = body;

  let connection;
  try {
    // Conexao
    connection = await pool.getConnection();

    const result = await connection.query(
      'INSERT INTO Grupos (group_id,nome,admin,criado_em) VALUES (UUID(),?,?,NOW())',
      [groupName,groupAdmin]
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

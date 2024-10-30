import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {group_ID,groupName,groupAdmin} = body;

  let connection;
  try {
    // Conexao
    connection = await pool.getConnection();

    const result = await connection.query(
      'INSERT INTO Grupos (group_id,nome,admin,criado_em) VALUES (?,?,?,NOW())',
      [group_ID,groupName,groupAdmin]
    );

    return { success: true, insertId: result.insertId };
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

import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const { groupName, groupAdmin } = body;

  if (!groupName || !groupAdmin) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Nome do grupo ou administrador ausente.',
    });
  }

  let connection;
  try {
    connection = await pool.getConnection();

    // Executa a query para inserir o grupo
    const result = await connection.query(
      'INSERT INTO Grupos (grupo_id, nome, admin, criado_em) VALUES (UUID(), ?, ?, NOW())',
      [groupName, groupAdmin]
    );

    // Converte insertId para string, caso seja BigInt
    return { success: true, insertId: result.insertId.toString() };
  } catch (error) {
    console.error('Erro ao inserir grupo:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao criar grupo.',
      data: error.message,
    });
  } finally {
    if (connection) connection.release();
  }
});

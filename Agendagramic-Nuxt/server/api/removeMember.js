import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);
  const { nomeGrupo, userMember, admin } = body;

  let connection;
  try {
    connection = await pool.getConnection();

    const [groupResult] = await connection.query(
      'SELECT group_id AS id_group FROM Grupos WHERE admin = ? AND nome = ?',
      [admin, nomeGrupo]
    );

    if (!groupResult || !groupResult.id_group) {
      throw new Error('Grupo não encontrado');
    }

    const groupId = groupResult.id_group;

    const result = await connection.query(
      'DELETE FROM Membros WHERE group_id = ? AND user_telegram = ?',
      [groupId, userMember]
    );

    if (result.affectedRows > 0) {
      return { success: true };
    } else {
      throw new Error('Falha ao remover o membro.');
    }
  } catch (error) {
    console.error('Error removing member:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Failed to remove member',
      data: error.message,
    });
  } finally {
    if (connection) connection.release();
  }
});

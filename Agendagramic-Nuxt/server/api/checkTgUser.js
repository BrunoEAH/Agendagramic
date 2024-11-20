import { defineEventHandler, getQuery } from 'h3';
import pool from '~/server/config/database';

const checkTgUser = async (user) => {
  if (!user) {
    return { exists: false };
  }

  let conn;
  try {
    conn = await pool.getConnection();
    const query = 'SELECT COUNT(*) AS count FROM Usuario WHERE user_telegram = ?';
    const [result] = await conn.query(query, [user]);
    return { exists: result.count > 0 };
  } catch (error) {
    console.error('Erro ao checar o usuario:', error);
    return { error: 'Internal server error' };
  } finally {
    if (conn) conn.release();
  }
};

export default defineEventHandler(async (event) => {
  const { user } = getQuery(event);
  return await checkTgUser(user);
});

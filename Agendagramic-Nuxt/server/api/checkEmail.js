import { defineEventHandler, getQuery } from 'h3';
import pool from '~/server/config/database';

const checkEmail = async (email) => {
  if (!email) {
    return { exists: false };
  }

  let conn;
  try {
    conn = await pool.getConnection();
    const query = 'SELECT COUNT(*) AS count FROM Usuario WHERE email = ?';
    const [result] = await conn.query(query, [email]);
    return { exists: result.count > 0 };
  } catch (error) {
    console.error('Erro ao checar o email:', error);
    return { error: 'Internal server error' };
  } finally {
    if (conn) conn.release();
  }
};

export default defineEventHandler(async (event) => {
  const { email } = getQuery(event);
  return await checkEmail(email);
});


import bcrypt from 'bcrypt';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const { name, email, password, tgUser } = body;

  let connection;

  try {
    connection = await pool.getConnection();

    // Hash da senha
    const hashedPassword = await bcrypt.hash(password, 10);

    // Tenta inserir o novo usuário, mas atualiza os dados se o user_telegram já existir
    const result = await connection.query(
      `INSERT INTO Usuario (user_telegram, nome, password, email, criado_em) 
      VALUES (?, ?, ?, ?, NOW()) 
      ON DUPLICATE KEY UPDATE 
      nome = VALUES(nome), 
      password = VALUES(password), 
      email = VALUES(email), 
      criado_em = NOW()`,
      [tgUser, name, hashedPassword, email]
    );

    return { success: true, message: 'Usuário cadastrado ou atualizado com sucesso' };
  } catch (error) {
    console.error('Falha ao buscar os dados:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Falha ao inserir ou atualizar os dados',
      data: error.message,
    });
  } finally {
    if (connection) connection.release(); 
  }
});

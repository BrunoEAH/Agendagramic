import bcrypt from 'bcrypt';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const { name, email, password, tgUser } = body;

  let connection;

  try {
    connection = await pool.getConnection();

    // Verifica se o email já está registrado
    const [existingUser] = await connection.query('SELECT * FROM Usuario WHERE email = ?', [email]);
    if (existingUser && existingUser.length > 0) {
      return { success: false, message: 'Email já cadastrado' };
    }
    // Faz o hash da senha antes de salvar no banco
    const hashedPassword = await bcrypt.hash(password, 10);

    // Insere o novo usuário no banco de dados
    const result = await connection.query(
      'INSERT INTO Usuario (user_telegram, nome, password, email, criado_em) VALUES (?, ?, ?, ?, NOW())', 
      [tgUser, name, hashedPassword, email]
    );

    return { success: true, insertId: result.insertId };
  } catch (error) {
    console.error('Falha ao buscar os dados:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Falha ao inserir os dados',
      data: error.message,
    });
  } finally {
    if (connection) connection.release(); 
  }
});

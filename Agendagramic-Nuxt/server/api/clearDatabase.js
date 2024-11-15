import pool from '../config/database.js';
import { eventHandler } from 'h3';

export default eventHandler(async (event) => {
  let connection;
  try {
    connection = await pool.getConnection();
    await connection.query('DELETE FROM Usuario'); // Limpa todos os registros na tabela de usuários
    return { success: true, message: 'Todos os usuários foram excluídos com sucesso.' };
  } catch (error) {
    console.error('Erro ao limpar o banco de dados:', error);
    return { success: false, message: 'Erro ao limpar o banco de dados.' };
  } finally {
    if (connection) connection.release();
  }
});

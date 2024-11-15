import pool from '../config/database.js';
import { eventHandler } from 'h3';

export default eventHandler(async (event) => {
  console.log("Iniciando teste de conexão com o banco de dados");
  try {
    const connection = await pool.getConnection();
    console.log("Conexão com o pool obtida com sucesso");

    await connection.ping(); // Testa a conexão
    console.log("Ping ao banco de dados bem-sucedido");

    connection.release();

    return { message: 'Conexão com o banco de dados bem-sucedida!' };
  } catch (error) {
    console.error('Erro ao conectar ao banco de dados:', error);
    
    // Retornar o erro de forma apropriada
    return { message: 'Erro ao conectar ao banco de dados', error: error.message };
  }
});

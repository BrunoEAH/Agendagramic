import { defineEventHandler, readBody, createError } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);

  // Extrair dados do corpo da requisição
  const { eventTitle, eventDescription = null, eventLocation = null, eventDate, eventTime = null, eventCreator } = body;

  // Validação dos campos obrigatórios
  if (!eventTitle || !eventDate || !eventCreator) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Campos obrigatórios ausentes. Certifique-se de preencher todos os campos obrigatórios.',
    });
  }

  let connection;
  try {
    // Estabelecer conexão com o banco de dados
    connection = await pool.getConnection();

    // Inserir os dados do evento no banco de dados
    const result = await connection.query(
      `INSERT INTO Eventos 
        (titulo, descricao, local, data, horario, criado_por, criado_em) 
      VALUES (?, ?, ?, ?, ?, ?, NOW())`,
      [
        eventTitle,          // Título do evento
        eventDescription,    // Descrição (pode ser NULL)
        eventLocation,       // Local (pode ser NULL)
        eventDate,           // Data do evento
        eventTime,           // Horário do evento (pode ser NULL)
        eventCreator,        // Criador do evento
      ]
    );

    // Retorna o ID do evento criado como string
    return { success: true, insertId: result.insertId.toString() };
  } catch (error) {
    // Logar o erro para facilitar a depuração
    console.error('Erro ao inserir evento no banco de dados:', error);

    // Lançar um erro HTTP 500 com mensagem detalhada
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao adicionar evento no banco de dados.',
      data: error.message,
    });
  } finally {
    // Garantir que a conexão será liberada
    if (connection) {
      connection.release();
    }
  }
});

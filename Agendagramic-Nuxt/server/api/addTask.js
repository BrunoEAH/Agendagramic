import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event);

  // Campos extraídos do corpo da requisição
  const {
    taskName,
    taskDescription = null, // Descrição é opcional
    dueDate,
    taskStatus,
    taskPriority,
    taskGroup,
    taskMembers = null, // Responsáveis são opcionais
    taskCreator,
  } = body;

  // Validação dos campos obrigatórios
  if (!taskName || !dueDate || !taskPriority || !taskGroup || !taskCreator) {
    throw createError({
      statusCode: 400,
      statusMessage: 'Campos obrigatórios ausentes',
    });
  }

  let connection;
  try {
    // Estabelecendo conexão com o banco de dados
    connection = await pool.getConnection();

    // Executando o comando de inserção
    const result = await connection.query(
      `INSERT INTO Tarefas 
        (titulo, info_task, data, esta_completa, prioridade, group_id, responsaveis, criado_por, criado_em) 
      VALUES (?, ?, ?, ?, ?, ?, ?, ?, NOW())`,
      [
        taskName, // Nome da tarefa
        taskDescription, // Descrição (pode ser NULL)
        dueDate, // Data de conclusão
        taskStatus, // Status da tarefa (0, 1 ou 2)
        taskPriority, // Prioridade ('alta', 'media', 'baixa')
        taskGroup, // ID do grupo (int)
        taskMembers, // Responsáveis (separados por vírgulas, pode ser NULL)
        taskCreator, // Criador da tarefa
      ]
    );

    // Retornando o ID da nova tarefa criada
    const insertId = result.insertId || result[0]?.insertId; // Compatível com diferentes estruturas
    return { success: true, insertId: String(insertId) };
  } catch (error) {
    console.error('Erro ao inserir tarefa:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao adicionar tarefa',
      data: error.message,
    });
  } finally {
    if (connection) {
      connection.release();
    }
  }
});

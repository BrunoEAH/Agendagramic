
import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const { task_ID,taskName,taskDescription,dueDate,taskStatus,taskPriority,taskGroup,taskMembers,taskCreator} = body;

  let connection;
  try {
    // Conexao
    connection = await pool.getConnection();

    const result = await connection.query(
      'INSERT INTO Tarefas (task_id,titulo,info_task,data,esta_completa,prioridade,group_id,responsaveis,criado_por,criado_em) VALUES (?,?,?,?,?,?,?,?,?,NOW())',
      [task_ID,taskName,taskDescription,dueDate,taskStatus,taskPriority,taskGroup,taskMembers,taskCreator]
    );

    return { success: true, insertId: result.insertId };
  } catch (error) {
    console.error('Error inserting data:', error);
    throw createError({
      statusCode: 500,
      statusMessage: 'Failed to insert data',
      data: error.message,
    });
  } finally {
    if (connection) connection.release(); 
  }
});

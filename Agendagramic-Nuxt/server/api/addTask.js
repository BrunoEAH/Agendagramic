
import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {taskName,taskDescription,dueDate,taskStatus,taskPriority,taskGroup,taskMembers,taskCreator} = body;

  let connection;
  let groupId = null;

  try {
    // Conexao
    connection = await pool.getConnection();

    if(taskGroup){
      const [groupResult] = await connection.query(
        'SELECT group_id AS id_group FROM Grupos WHERE admin = ? AND nome = ?',
        [taskCreator,taskGroup]
      );
      console.log(groupResult)
      groupId = groupResult.id_group;
      
    }

    const result = await connection.query(
      'INSERT INTO Tarefas (task_id,titulo,info_task,data,esta_completa,prioridade,group_id,responsaveis,criado_por,criado_em) VALUES (UUID(),?,?,?,?,?,?,?,?,NOW())',
      [taskName,taskDescription,dueDate,taskStatus,taskPriority,groupId,taskMembers,taskCreator]
    );

    return { success: true, insertId: result.insertId.toString() };
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

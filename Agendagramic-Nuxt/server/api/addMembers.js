import { defineEventHandler, readBody } from 'h3';
import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const body = await readBody(event); 
  const {nomeGrupo,userMember,admin} = body;

  let connection;
  try {
    // Conexao
    connection = await pool.getConnection();

    console.log('admin:', admin);
    console.log('nomeGrupo:', nomeGrupo);


    const [groupResult] = await connection.query(
      'SELECT group_id AS id_group FROM Grupos WHERE admin = ? AND nome = ?',
      [admin,nomeGrupo]
    );

    if (!groupResult || !groupResult.id_group) {
      throw new Error('Grupo nao encontrado');
    }

    const groupId = groupResult.id_group;

    const result = await connection.query(
      'INSERT INTO Membros (group_id,user_telegram,papel,entrou_em) VALUES (?,?,"Membro",NOW())',
      [groupId,userMember]
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

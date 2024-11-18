import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  // Obter o parâmetro 'userTelegram' da query
  const { userTelegram } = getQuery(event);

  // Validar se o parâmetro foi fornecido
  if (!userTelegram) {
    console.error('Erro: Parâmetro userTelegram ausente.');
    throw createError({
      statusCode: 400,
      statusMessage: 'Parâmetro userTelegram ausente',
    });
  }

  console.log('Parâmetros recebidos no backend:', userTelegram);

  let connection;
  try {
    // Conectar ao banco de dados
    connection = await pool.getConnection();
    console.log('Conexão com o banco de dados estabelecida.');

    // Consulta SQL para buscar os grupos administrados pelo usuário
    const [rows] = await connection.query(
      'SELECT grupo_id AS group_id, nome AS group_name FROM Grupos WHERE admin = ?',
      [userTelegram]
    );

    console.log('Rows retornados pelo banco:', rows);

    // 'rows' é um array de grupos
    const groups = rows;

    // Verificar se grupos foram encontrados
    if (!groups || groups.length === 0) {
      console.log('Nenhum grupo encontrado para o usuário:', userTelegram);
      return { success: true, groups: [], message: 'Nenhum grupo encontrado.' };
    }

    // Retornar os grupos encontrados
    return { success: true, groups };
  } catch (error) {
    console.error('Erro ao buscar grupos:', error.message);
    console.error('Stack Trace:', error.stack);
    throw createError({
      statusCode: 500,
      statusMessage: 'Erro ao buscar grupos',
      data: error.message,
    });
  } finally {
    if (connection) {
      console.log('Liberando conexão com o banco de dados.');
      connection.release();
    }
  }
});

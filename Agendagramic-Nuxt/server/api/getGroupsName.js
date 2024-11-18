import pool from '~/server/config/database';

export default defineEventHandler(async (event) => {
  const query = getQuery(event);
  const userTelegram = query.userTelegram;

  if (!userTelegram) {
    throw createError({
      statusCode: 400,
      statusMessage: 'UserTelegram is missing',
    });
  }

  let connection;
  try {
    connection = await pool.getConnection();
    const [groups] = await connection.query(
      'SELECT nome AS group_name FROM Grupos WHERE admin = ? LIMIT 10',
      [userTelegram]
    );

    console.log('Query result:', groups);

    // Return groups to the client
    return { success: true, groups };
  } catch (error) {
    console.error('Error fetching groups:', error); // Log error on the server
    throw createError({
      statusCode: 500,
      statusMessage: 'An error occurred while fetching groups.',
    });
  }
});

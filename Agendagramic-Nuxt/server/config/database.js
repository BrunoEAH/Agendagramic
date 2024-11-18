import mariadb from 'mariadb';

const pool = mariadb.createPool({
  host: 'localhost',
  port: '3306',
  user: 'root',
  password: '29052672', 
  database: 'agendagramic',
  connectionLimit: 100,      // Limite de conexões reduzido
  acquireTimeout: 50000,    // Tempo limite menor para teste, 5 segundos
});

pool.getConnection()
  .then(conn => {
    console.log("Conexão bem-sucedida!");
    conn.release(); // Libere a conexão após o teste
  })
  .catch(err => {
    console.error("Erro ao conectar ao banco de dados:", err);
  });

export default pool;

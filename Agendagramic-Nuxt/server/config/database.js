import mariadb from 'mariadb';

const pool = mariadb.createPool({
  host: 'localhost',
  port: '3306',
  user: 'root',
  password: '29052672', 
  database: 'agendagramic',
  connectionLimit: 1,      // Limite de conexões reduzido
  acquireTimeout: 5000,    // Tempo limite menor para teste, 5 segundos
});

export default pool;

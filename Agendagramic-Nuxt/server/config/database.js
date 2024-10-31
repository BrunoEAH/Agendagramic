import mariadb from 'mariadb';

const pool = mariadb.createPool({
  host: 'localhost', // Localhost for MariaDB
  port: '3306',
  user: 'teste',
  password: 'teste',
  database: 'agendagramic',
  connectionLimit: 10,
  acquireTimeout: 20000
});

export default pool;

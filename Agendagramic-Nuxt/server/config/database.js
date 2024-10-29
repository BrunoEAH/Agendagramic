import mariadb from 'mariadb';

const pool = mariadb.createPool({
  host: 'localhost', // Localhost for MariaDB
  port: '3306',
  user: 'seu-user',
  password: 'senha',
  database: 'agendagramic',
  connectionLimit: 5,
});

export default pool;

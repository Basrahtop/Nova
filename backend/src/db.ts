import { Pool } from 'pg';

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'nova_db',
  password: 'your_password',
  port: 5432,
});

export default pool;

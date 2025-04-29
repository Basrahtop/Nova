import pool from '../db';

export interface Student {
  id?: number;
  name: string;
  age: number;
  grade: string;
  performanceScore: number;
}

export const createStudent = async (student: Student): Promise<Student> => {
  const res = await pool.query(
    'INSERT INTO students (name, age, grade, performance_score) VALUES ($1, $2, $3, $4) RETURNING *',
    [student.name, student.age, student.grade, student.performanceScore]
  );
  return res.rows[0];
};

export const getAllStudents = async (): Promise<Student[]> => {
  const res = await pool.query('SELECT * FROM students ORDER BY id DESC');
  return res.rows;
};

export const getStudentById = async (id: number): Promise<Student | null> => {
  const res = await pool.query('SELECT * FROM students WHERE id = $1', [id]);
  return res.rows[0] || null;
};

export const updatePerformanceScore = async (id: number, score: number): Promise<Student> => {
  const res = await pool.query(
    'UPDATE students SET performance_score = $1 WHERE id = $2 RETURNING *',
    [score, id]
  );
  return res.rows[0];
};

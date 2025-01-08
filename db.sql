/* This creates the students table */

TABLE students(
  id SERIAL PRIMARY KEY,
  first_name TEXT,
  last_name TEXT,
  math_level TEXT,
  grade_level INTEGER,
  school TEXT)

/* This creates the sessions table */

TABLE sessions(
  id SERIAL PRIMARY KEY,
  student_id INT,
  hours NUMERIC(2,1),
  rate INT,
  date DATE DEFAULT CURRENT_DATE,
  location TEXT,
  paid BOOLEAN)

# CREATE TABLE IF NOT EXISTS teachers (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(50) NOT NULL,
#     phone VARCHAR(20),
#     specialty VARCHAR(30) NOT NULL,
#     created_at VARCHAR(30) NOT NULL
# );
#
# CREATE TABLE IF NOT EXISTS students (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(50) NOT NULL,
#     phone VARCHAR(20),
#     birth_date VARCHAR(20) NOT NULL,
#     created_at VARCHAR(30) NOT NULL
# );
#
# CREATE TABLE IF NOT EXISTS payments (
#     id SERIAL PRIMARY KEY,
#     student_id VARCHAR(20),
#     group_id VARCHAR(20),
#     amount INTEGER CHECK (amount > 0),
#     payment_date VARCHAR(20),
#     payment_type VARCHAR(20)
# );
#
# CREATE TABLE IF NOT EXISTS groups (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     course_id VARCHAR(20) NOT NULL,
#     teacher_id VARCHAR(20) NOT NULL,
#     start_date VARCHAR(20) NOT NULL,
#     status VARCHAR(50) NOT NULL
# );
#
# CREATE TABLE IF NOT EXISTS enrollments (
#     id SERIAL PRIMARY KEY,
#     student_id VARCHAR(20) NOT NULL,
#     group_id VARCHAR(20) NOT NULL,
#     joined_date VARCHAR(20)
# );
#
# CREATE TABLE IF NOT EXISTS courses (
#     id SERIAL PRIMARY KEY,
#     name VARCHAR(50) NOT NULL,
#     price INTEGER CHECK (price > 0),
#     duration_month VARCHAR(30),
#     created_at VARCHAR(30)
# );
#
# CREATE TABLE IF NOT EXISTS homework (
#     id SERIAL PRIMARY KEY,
#     group_id VARCHAR(20) NOT NULL,
#     teacher_id VARCHAR(20) NOT NULL,
#     title VARCHAR(30) NOT NULL,
#     description VARCHAR(100),
#     deadline VARCHAR(30)
# );
#
# CREATE TABLE IF NOT EXISTS admins (
#     id SERIAL PRIMARY KEY,
#     full_name VARCHAR(50) NOT NULL,
#     phone VARCHAR(20),
#     password VARCHAR(20),
#     role VARCHAR(30)
# );
#
# CREATE TABLE IF NOT EXISTS attendance (
#     id SERIAL PRIMARY KEY,
#     student_id VARCHAR(20) NOT NULL,
#     group_id VARCHAR(20) NOT NULL,
#     lesson_date VARCHAR(30) NOT NULL,
#     status VARCHAR(50)
# );

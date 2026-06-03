from database.db_connection import get_connection
from models.student_class import Student

# Add student
def add_student(student):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                   (student.id, student.name, student.age, student.course))

    conn.commit()
    conn.close()
    print("✅ Student Added Successfully")


# Show all students
def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        print(row)


# Get student by ID
def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students WHERE id=?", (student_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        print(row)
    else:
        print("❌ Student not found")


# Update student
def update_student(student_id, name, age, course):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE students
    SET name=?, age=?, course=?
    WHERE id=?
    """, (name, age, course, student_id))

    conn.commit()
    conn.close()
    print("🔄 Student Updated")


# Delete student
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))

    conn.commit()
    conn.close()
    print("🗑️ Student Deleted")
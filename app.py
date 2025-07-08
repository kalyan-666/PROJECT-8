from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# ---------- MySQL Database Connection ----------
def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='kalyan2427',   # Change this to your MySQL password
        database='company'
    )

# ---------- Home Page: Show Form + Employees ----------
@app.route('/', methods=['GET', 'POST'])
def register_and_show():
    con = get_db_connection()
    cursor = con.cursor()

    # ---------- Save New Employee ----------
    if request.method == 'POST':
        emp_id = request.form['emp_id']
        emp_name = request.form['emp_name']
        designation = request.form['designation']
        department = request.form['department']

        insert_query = "INSERT INTO employee (emp_id, emp_name, designation, department) VALUES (%s, %s, %s, %s)"
        values = (emp_id, emp_name, designation, department)
        cursor.execute(insert_query, values)
        con.commit()

        return redirect('/')  # Reload the page to show updated list

    # ---------- Display All Employees ----------
    cursor.execute("SELECT * FROM employee")
    employees = cursor.fetchall()
    con.close()
    return render_template('employees.html', employees=employees)

if __name__ == '__main__':
    app.run(debug=True)

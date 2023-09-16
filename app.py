# app.py

from flask import Flask, jsonify, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'your_db_host'
app.config['MYSQL_USER'] = 'your_db_username'
app.config['MYSQL_PASSWORD'] = 'your_db_password'
app.config['MYSQL_DB'] = 'your_db_name'

mysql = MySQL(app)

# Create a route to fetch doctor names
@app.route('/')
def home():
    cur = mysql.connection.cursor()
    cur.execute('SELECT doctor_name FROM doctors')
    doctor_names = [row[0] for row in cur.fetchall()]
    cur.close()
    return render_template('home.html', doctor_names=doctor_names)

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/get_all_patient_data', methods=['GET'])
def get_all_patient_data():
    cur = mysql.connection.cursor()
    cur.execute('SELECT name, age, phone_no, hospital_id, doctor_id FROM patients ORDER BY id DESC')
    all_patient_data = cur.fetchall()
    cur.close()
    return jsonify(all_patient_data)
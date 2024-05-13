from flask import Flask, request, render_template
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Kết nối đến cơ sở dữ liệu PostgreSQL
conn = psycopg2.connect(
    dbname="datawebform",
    user="datawebform_user",
    password="UEVIQcRUMKdTNWjtreGf9eKKjWt7DNmT",
    host="dpg-cp0nqfg21fec7387tu30-a.oregon-postgres.render.com",
    port="5432"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        create_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        experience = request.form['experience']
        salary = request.form['salary']
        location = request.form['location']
        skill = ', '.join(request.form.getlist('skill'))

        cursor = conn.cursor()
        cursor.execute("INSERT INTO applications (create_at, name, email, phone, experience, salary, location, skill) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (create_at, name, email, phone, experience, salary, location, skill))
        conn.commit()
        cursor.close()
        print("Upload to postgres successfully")
        return render_template('submit-success.html') 

if __name__ == '__main__':
    app.run(debug=True)

# postgres://loaddata_user:G0WB4i58Zu4hJbJOEHWUxBTjzdujhCqR@dpg-cp09h5821fec7380hssg-a.oregon-postgres.render.com/loaddata
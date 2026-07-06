from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

db = mysql.connector.connect(
host="localhost",
user="root",
password="atchu@123",  
database="bus_booking"
)

cursor = db.cursor()

@app.route('/book', methods=['POST'])
def book():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    source = request.form['from']
    destination = request.form['to']
    date = request.form['date']
    seats = request.form['seats']
    gender = request.form['gender']
    bus_type = request.form['bus_type']
    boarding = request.form['boarding']

    query = """
    INSERT INTO bookings 
    (name, email, phone, source, destination, travel_date, seats, gender, bus_type, boarding)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (name, email, phone, source, destination, date, seats, gender, bus_type, boarding)

    cursor.execute(query, values)
    db.commit()

    return "<h2>🎉 Ticket Booked Successfully & Saved in Database!</h2>"

if __name__ == '__main__':
    app.run(debug=True)
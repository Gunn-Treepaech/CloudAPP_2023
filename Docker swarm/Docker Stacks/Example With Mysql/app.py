from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return 'Example Docker Stack With Mysql'

@app.route('/db', methods=['GET'])
def showdatadb():
    return jsonify(getdatadb())

def getdatadb():
    config = {
        'user': 'user',
        'password': 'user',
        'host': 'db',
        'port': '3306',
        'database': 'example'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM example_data;')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

if __name__ == '__main__':
    # -----------------------------------------------------------------------------------------------
    config = {
    "start_month": 11,
    "start_year": 2024,
    "initial_loan": 100000000,
    "fixed_interest": 2.95,
    "fixed_year": 3,
    "MRR": 8.8,
    "monthly_payment": 15000,
    "chang_interest": [2.95, 1.95],
    "bank": "UOB"
}
    # ------------------------------------------------------------------------------------------------
    #calculate_loan_schedule(**config)
    app.run(host='0.0.0.0', port=12345)

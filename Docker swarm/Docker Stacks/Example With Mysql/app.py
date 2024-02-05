from flask import Flask, request, jsonify
import mysql.connector
import json

app = Flask(__name__)

config = {
    'user': 'user',
    'password': 'user',
    'host': 'db',
    'port': '3306',
    'database': 'example'
}

@app.route('/', methods=['GET'])
def home():
    return 'Example Docker Stack With Mysql'

@app.route('/db', methods=['GET'])
def showdb():
    return jsonify(getdb())

@app.route('/adddata', methods=['POST'])
def adddata():
    datas = request.json
    insertdata(**datas)
    return jsonify(getdb())

@app.route('/addcolumn', methods=['GET'])
def addcolumn():
    insertcolumn()
    return jsonify(getdb())

@app.route('/addtable', methods=['GET'])
def addtable():
    inserttable()
    return

def getdb():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    cursor.execute('SELECT * FROM example_data;')
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results

def insertdata(**datas):
    data_to_insert = datas
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    insert_query = "INSERT INTO example_data (test1, test2, test3) VALUES (%s, %s, %s)"
    for entry in data_to_insert:
        cursor.execute(insert_query, (json.dumps(entry['test1']), entry['test2'], entry['test3']))
    connection.commit()
    cursor.close()
    connection.close()
    return

def insertcolumn():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    alter_table_query = "ALTER TABLE example_data ADD COLUMN new_column VARCHAR(50)"
    cursor.execute(alter_table_query)
    connection.commit()
    cursor.close()
    connection.close()
    return

def inserttable():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor(dictionary=True)
    create_table_query = """
    CREATE TABLE IF NOT EXISTS new_table (
    id INT AUTO_INCREMENT PRIMARY KEY,
    column1 VARCHAR(50),
    column2 DECIMAL(4, 2),
    column3 DECIMAL(5, 2)
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()
    return

if __name__ == '__main__':
    # -----------------------------------------------------------------------------------------------
    config = {
    "test1": 'gun',
    "test2": 2024,
    "test3": 100,
}
    # ------------------------------------------------------------------------------------------------
    app.run(host='0.0.0.0', port=12345)

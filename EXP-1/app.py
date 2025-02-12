from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Date@2004",
    database="Bank_Loan_DW"
)
cursor = db.cursor()

# API to insert a new customer
@app.route('/add_customer', methods=['POST'])
def add_customer():
    data = request.json
    sql = "INSERT INTO Customer_Dimension (Name, Age, Gender, Income, Credit_Score) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (data["name"], data["age"], data["gender"], data["income"], data["credit_score"]))
    db.commit()
    return jsonify({"message": "Customer added successfully!"})

# API to fetch loan disbursement details
@app.route('/get_loans', methods=['GET'])
def get_loans():
    cursor.execute("SELECT * FROM Loan_Disbursement_Fact")
    result = cursor.fetchall()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    return "Dashboard API Running"


@app.route("/dashboard")
def dashboard():

    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transactions")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions WHERE prediction='Mule'")
    mule = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions WHERE prediction='Suspicious'")
    suspicious = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM transactions WHERE prediction='Legit'")
    legit = cursor.fetchone()[0]

    cursor.execute("""
    SELECT acct_age,txn_count,txn_amount,prediction,probability
    FROM transactions
    ORDER BY id DESC
    LIMIT 10
    """)

    rows = cursor.fetchall()

    conn.close()

    return jsonify({

        "total":total,
        "mule":mule,
        "suspicious":suspicious,
        "legit":legit,
        "rows":rows

    })


app.run(debug=True)
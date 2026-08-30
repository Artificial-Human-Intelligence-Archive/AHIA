from flask import Flask
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('logs.db', timeout=30)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS log(
id INTEGER PRIMARY KEY AUTOINCREMENT,
nume TEXT NOT NULL,
email TEXT UNIQUE NOT NULL,
parola TEXT NOT NULL,
aid INTEGER);''')

conn = sqlite3.connect('fis.db', timeout=30)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS fis(
id INTEGER PRIMARY KEY AUTOINCREMENT,
uid INTEGER NOT NULL,
nume TEXT NOT NULL,
ext TEXT NOT NULL,
loc TEXT NOT NULL,
dim INTEGER NOT NULL,
FOREIGN KEY (uid) REFERENCES log (id));''')

@app.route("/")
def index():
    return "Hello, from Flask in Wasmer Edge 🚀"

@app.route("/Diana")
def treburi():
    return "Diano, daca nu mai lucrezi, macar spune-mi. Si daca totusi vrei sa mai continui sa ma ajuti, eu cred co o voi lasa-o mai usor cu celallt proiect si voi face mai multe la asta. Pur si simplu, fara tine pare plictisitor."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

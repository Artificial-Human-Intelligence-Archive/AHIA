from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, from Flask in Wasmer Edge 🚀"
@app.route("/Diana")
def treburi():
    return "Diano, daca nu mai lucrezi, macar spune-mi. Si daca totusi vrei sa mai continui sa ma ajuti, eu cred co o voi lasa-o mai usor cu celallt proiect si voi face mai multe la asta. Pur si simplu, fara tine pare plictisitor."
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

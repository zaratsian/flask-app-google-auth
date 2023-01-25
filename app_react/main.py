from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/data")
def get_data():
    data = {
        "message": "Hello from the backend!"
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run()

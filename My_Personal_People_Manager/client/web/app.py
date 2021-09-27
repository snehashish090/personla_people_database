from flask import *

app = Flask(__name__)

@app.route('/main', methods=["GET", "POST"])
def main():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port="8000")


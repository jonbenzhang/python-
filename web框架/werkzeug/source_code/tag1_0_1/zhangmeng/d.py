from flask_old import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def m():
    return "hello"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=15478)

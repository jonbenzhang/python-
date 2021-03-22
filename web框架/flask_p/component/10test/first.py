from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods={"POST"})
def b():
    print(request.form)
    return "dd"


app.run(host="0.0.0.0")

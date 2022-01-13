# from ..flask import Flask,request,g
from .app import Flask
app = Flask(__name__)
@app.route("/",methods=["GET"])
def main():
    return {}

app.__call__
app.run()
# request.get_data()
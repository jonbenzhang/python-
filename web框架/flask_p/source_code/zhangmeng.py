from flask_ import Flask,g
# from .app import Flask
app = Flask(__name__)
@app.route("/",methods=["GET"])
def main():
    # print(g.__dict__)
    return [1,2]
# app.__call__
app.run()
# request.get_data()

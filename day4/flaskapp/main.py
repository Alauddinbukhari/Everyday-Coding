from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/bye")
def bye():
    return "Bye"


@app.route("/hello/<int:var>")
def example_var(var):
    return f"hello {var}"
if __name__ =="__main__":
    app.run(debug=True)
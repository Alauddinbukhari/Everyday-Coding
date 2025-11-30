from flask import Flask

app = Flask(__name__)

def make_bold(function):
        
        def wrapper_function():
            text=function()
            return f'<b>{text}</b>'

        return  wrapper_function

def make_empahsis(function):
     def wrapper_function():
            text=function()
            return f'<em>{text}</em>'

     return  wrapper_function

def make_underlined(function):
     def wrapper_function():
          text=function()
          return f'<u>{text}</u>'
     return wrapper_function


@app.route("/")
def hello_world():
    return '<h1 style ="text-align: center"> Hello World! </h1>'\
            '<p> This is a paragraph</p>'


@app.route("/bye")
@make_bold
@make_empahsis
@make_underlined
def bye():
    return "Bye"


@app.route("/hello/<int:var>")
def example_var(var):
    return f"hello {var}"





if __name__ =="__main__":
    app.run(debug=True)



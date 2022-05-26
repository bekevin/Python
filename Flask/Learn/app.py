from flask import Flask, render_template

app = Flask(__name__)

def hello():
    return "Hello World!"

@app.route("/")
def hello():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/<my_name>")
def greetings(my_name):
    if my_name == "kevin":
        my_name = "Dummy"
    return f"welcome {my_name}"

@app.route("/render")
def render():
    return render_template("test.html")

@app.route("/index")
def index():
    Users = {
                "Archie":"Amsterdam",
                "Veronica":"London",
                "Betty":"San Francisco",
                "Jughead":"Los Angeles"
            }
    return render_template("index.html", users=Users)

@app.route('/square/<int:number>')
def show_square(number):

    return "Square of "+ str(number) +" is: "+ str(number * number) 

@app.route("/educated")
def learn():
    return "Happy Learning!"

if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)




from flask import Flask
from run import hello_world, hello_name_number, greet
app = Flask(__name__)

app.config.from_pyfile("config.py")

app.add_url_rule("/", view_func=hello_world)
app.add_url_rule("/hello/<string:name>/<int:number>", view_func=hello_name_number)
app.add_url_rule("/greet", view_func=greet)

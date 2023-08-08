from flask import Flask, request

app = Flask(__name__)

# Привет мир
@app.route('/')
def hello_world():
    return 'Hello, world!'

# Приветствие с динамическим маршрутом
@app.route('/hello/<string:name>/<int:number>')
def hello_name_number(name, number):
    return f'Hello {name}! Your number is {number}.'

# Приветствие с query в URL
@app.route('/greet')
def greet():
    name = request.args.get('name', 'Guest')
    number = request.args.get('number', 0, type=int)
    return f'Hello {name}! Your number is {number}.'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=45000)

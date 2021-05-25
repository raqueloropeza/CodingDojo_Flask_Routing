from flask import Flask 

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def success ():
    return 'Dojo!'

@app.route('/say/<name>')
def say(name):
    print(name)
    return "Hi, " + name + "!"

@app.route('/repeat/<int:num>/<word>')
def repeat(word, num):
    print(word)
    return word * num

@app.route('/user/<int:id>')
def checkinteger(id):
    return f"The answer to life, the universe, and everything is {id}"

if __name__=="__main__":
    app.run(debug=True)
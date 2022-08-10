from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/second')
def second():
    return 'Bize Her Yer Kayseri!!!!'

@app.route('/third/subthird')
def third():
    return 'This is the'

@app.route('/forth/<string:id>')
def forth(id):
    return f'Id number of this page is {id}'
    
if __name__ == "__main__":
    app.run(debug=True,)
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    posts = [
            {
            'title' : "Poem",
            'content' : "Nothing",
            'gender' : 1,
            'author' : 'Soái ca'
            },
            {'title' : "Thơ",
            'content' : "Ko có gì",
            'gender' : 1,
            'author' : 'boy'
            },
            {
            'title' : 'No',
            'content' : 'shut',
            'gender' : 0,
            'author' : 'up'
            }


    ]
    return render_template('index.html', posts=posts)

@app.route('/Hello')
def hello():
    return "Hello c4E16"


@app.route('/SayHi/<name>/<age>') #tren duoi nhu nhau
def sayhi(name, age):
    return "Hi " + name + ".You're" + age + "years old"

@app.route('/sum/<int:num01>/<int:num02>')
def sum(num01, num02):
    return str(num01 + num02)

if __name__ == '__main__':
  app.run(debug=True)

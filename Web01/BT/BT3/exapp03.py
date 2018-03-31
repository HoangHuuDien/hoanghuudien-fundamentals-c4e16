from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def exapp03():

    Users = {
    	“quy” :         {
    			“name” : “Dinh Cong Quy”,
    			“age” : 20
           },
    “tuananh” : {
    			“name” : “Huynh Tuan Anh”,
    			“age” : 22
           }
}
        return render_template('exapp03.html', Users=Users)

if __name__ == '__main__':
  app.run( debug=True)

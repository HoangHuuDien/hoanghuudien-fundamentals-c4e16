from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/about-me')
def aboutme():
    return render_template('exapp01.html')

@app.route('/school')
def school():
    return redirect('http://techkids.vn' )

if __name__ == '__main__':
  app.run(debug=True)

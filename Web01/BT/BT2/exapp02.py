from flask import Flask
app = Flask(__name__)


#with

@app.route('/bmi/weight/<height')
def calc(weight,height):
    bmi = weight/((height*0.01)**2)
    h = h / 100
    return render_template('exapp02.html', BMI=BMI)

if __name__ == '__main__':
  app.run( debug=True)

#without

@app.route('/bmi/<weight>/<height>')
def calc(weight, height):
    height = height / 100
    BMI = weight / (height * height)
    if BMI < 16 :
    return("Severely underweight")
elif BMI > 16 and BMI < 18.5:
    return("Underweight")
elif BMI > 18.5 and BMI  < 25:
    return('Normal')
elif BMI > 25 and BMI < 30:
    return('Overweight')
else: print('Obese')

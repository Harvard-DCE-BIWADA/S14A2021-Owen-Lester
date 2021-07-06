from flask import Flask, render_template, request
import joblib
from forms.forms import Form
#import sklearn

# Initialize
app = Flask(__name__)
app.secret_key = 'super_duper_secret' # where else can we put this??

#Load ML model
model = joblib.load('./notebooks/regr.pkl')
@app.route('/')
def index():
    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = str(model.predict([[4, 2.5, 3005, 15, 17903.0, 1]])[0][0].round(1))
    # Return Template
    return render_template('index.html', prediction = prediction)

@app.route('/form')
def form():

    # Instantiate form
    form = Form()

    return render_template('form.html', form=form)

@app.route('/predict', methods=['post'])
def predict():

    # Form vars - cast strings to float
    beds = float(request.form['beds'])
    baths = float(request.form['baths'])
    sqft = float(request.form['sqft'])
    age = float(request.form['age'])
    lotsize = float(request.form['lotsize'])
    garage = float(request.form['garage'])

    #next line is for grad student homework
    #l = ???

    # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
    prediction = str(model.predict([[beds, baths, sqft, age, lotsize, garage]])[0][0].round(1))

    return render_template('index.html', prediction=prediction)
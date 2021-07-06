##Lab 3

1. (HW) Strategies for improving your linear model:

    + Understand data better with visualizations from  [Seaborn](https://seaborn.pydata.org/): `pip install seaborn` *- nb[1, 10, 11]*.
    + Take a look at the [coeffecients](https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html) *- nb[21, 16*]*.
    + Make use of categorical variables with [Pandas'](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html) `get_dummies` (or, with [SKLearn's]([`https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html`) `OneHotEncoder`) *- nb[13, 14, 15]*.
    + Running [Decision Tree](https://scikit-learn.org/stable/modules/tree.html) and [Random Forest](https://scikit-learn.org/stable/modules/ensemble.html) (paying attention to parameters).
    + Not covered, but important - [preprocessing](https://scikit-learn.org/stable/modules/preprocessing.html).

2. Pickle (pipeline) your file using [joblib](https://joblib.readthedocs.io/en/latest/).
	+ Copy the output .pkl files from your lab2 homework to the lab3/notebook/ directory.
	+ Example pkl files can also be found in the notebook/ directory.

3. Move the model into Flask:

    + Set up your flask app with an `app.py`:
        ```
        from flask import Flask, render_template, request
        import joblib

        # Initialize
        app = Flask(__name__)
        app.secret_key = 'super_duper_secret' # where else can we put this??

        @app.route('/')
        def index():

            # Return Template
            return render_template('index.html')
        ```

    + After your app is initialized, load your model:
        ```
        # Load ML model
        model = joblib.load('./notebooks/regr.pkl') ## or ../lab2/notebooks/regr.pkl
        ```
    + Make a prediction in '/' (index route):
        ```
        # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
        prediction = str(model.predict([[4, 2.5, 3005, 15, 17903.0, 1]])[0][0].round(1))
        ```
    + Show the output predictions in the browser (for each model) - see example image 'output_eg.png'.

4. Connect to a user with forms
    + Install [Flask WTF](https://flask-wtf.readthedocs.io/en/stable/): `pip install flask-wtf`.
    + Create a directory `forms` with a file `form.py` with:
        ```
        from flask_wtf import FlaskForm
        from wtforms import StringField, IntegerField, DecimalField, SubmitField
        from wtforms.validators import DataRequired


        class Form(FlaskForm):
            beds = DecimalField('Beds', default=4, validators=[DataRequired()])
            baths = DecimalField('Baths', default=2.5, validators=[DataRequired()])
            sqft = DecimalField('Sq. feet', default=3005, validators=[DataRequired()])
            age = DecimalField('Age', default=15, validators=[DataRequired()])
            lotsize = DecimalField('Lot size', default=1793, validators=[DataRequired()])
            garage = DecimalField('Garage', default=1, validators=[DataRequired()])
            # proptype = StringField('proptype', validators=[DataRequired()])
			# Uncomment the next line for Grad student homework
			# model = ???
            submit = SubmitField('Predict')
        ```

    + Create a new template called `form.html`:
        ```
        {% extends "layout.html" %}

        {% block styles %}
        <link href="{{ url_for('static', filename='./css/form.css') }}" rel="stylesheet">
        {% endblock %}

        {% block scripts %}
        {% endblock %}

        {% block content %}
        <h1>Housing price prediction form</h1>

        <form class="form" method="POST" action="/predict">
            {{ form.hidden_tag() }}

            {% for field in form %}
                {% if field.id != 'submit' and field.id != 'csrf_token' %}
                    <div class="form-group">
                        {{ field.label }}:
                        {{ field }}
                        {% if field.errors %}
                            {% for error in field.errors %}
                                <p class="form-error-message">{{ error }}</p>
                            {% endfor %}
                        {% endif %}
                    </div>
                {% endif %}
            {% endfor %}

            <div class="form-submit">
                {{ form.submit }}
            </div>
        </form>

        {% endblock %}

        ```
    + In app.py:
        + Add import: `from forms.form import Form`
        + Add form route:
            ```
            @app.route('/form')
            def form():

                # Instantiate form
                form = Form()

                return render_template('form.html', form=form)
            ```
        + Add predict route:
            ```
            @app.route('/predict', methods=['post'])
            def predict():

                # Form vars - cast strings to float
                beds = float(request.form['beds'])
                baths = float(request.form['baths'])
                sqft = float(request.form['sqft'])
                age = float(request.form['age'])
                lotsize = float(request.form['lotsize'])
                garage = float(request.form['garage'])

				# The next line is for grad student homework
				# model = ???

                # Make prediction - features = ['BEDS', 'BATHS', 'SQFT', 'AGE', 'LOTSIZE', 'GARAGE']
                prediction = str(model.predict([[beds, baths, sqft, age, lotsize, garage]])[0][0].round(1))

                return render_template('index.html', prediction=prediction)
            ```
	5. Test your application using `flask run`

	6. Publish your new app to heroku
		+ Commit and push your code to github first,
		+ Create a *new* heroku app using the steps we used previously.
			+ Remember to create/copy your Procfile to the main repo directory.
			+ Remember to create/copy your requirements.txt file to the main repo directory.
			+ This will **overwrite** the old files!

	7. HW: Using the resources/bootstrap.md file as a guide, modify your templates to use bootstrap for styling your new web application.
		+ Rerun steps 5 & 6 with your newly styled app.

	8. EXTRA: Add a drop-down menu that will allow you to choose which of the three regression models you chose to use when making predictions.

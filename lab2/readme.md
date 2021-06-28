## Lab 2

Welcome! This week we will be learning to work with Python notebooks

1. Install [Jupyter](https://jupyter.org/)

    + `pip install jupyter`

2. Open Jupyter in the browser:

    + Serve: `jupyter notebook`
    + Click on the generated link to access in browser
    + A lot of help in "Help"
    + Some keyboard shortcuts:
        + Run cell: `shift enter`
        + Run cell, move down: `control enter`
        + New cell: `alt enter`
        + Save and checkpoint with: `command s`

3. Get started with [Numpy](https://numpy.org/) - [docs](https://numpy.org/doc/stable/reference/index.html)

    + Numpy is useful for performing [linear algebra](https://en.wikipedia.org/wiki/Linear_algebra) operations on n
    -dimensional arrays!
    + Install: `pip install numpy`
    + Go through 'lab2_numpy.ipynb'

4. Get started with [Pandas](https://pandas.pydata.org/) - [docs](https://pandas.pydata.org/docs/user_guide/index.html#user-guide)

    + Pandas is useful for data analysis and manipulation.
    + Install: `pip install pandas`
    + Go through 'lab2_pandas.ipynb'

5. Move into an example, 'lab2_pricing_houses.ipynb'

    + Import and explore the data with Numpy and Pandas
    + Leverage [Scikit-learn](https://scikit-learn.org/stable/) - [user guide](https://scikit-learn.org/stable/user_guide.html)
        + SKlearn is our first tool for machine learning
        + Install: `pip install sklearn`
    + Visualize with [Matplotlib](https://matplotlib.org/) - [docs](https://matplotlib.org/contents.html)
        + Install: `pip install matplotlib`
    + Export with [Joblib](https://joblib.readthedocs.io/en/latest/)
        + Install `pip install joblib`

6. HW:

    1. Run a model using SKlearn's [Train-Test-Split](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html), including an r2 score, pkl file and plots.
    2. Run another model using a [Decision Tree Regressor](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeRegressor.html), including an r2 score, pkl file and plot.

7. EXTRA (Required for Grad Students)
    3. Run one of the ensemble methods presented in class and perform parameter tuning via CV GridSearch.

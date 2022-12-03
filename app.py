import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
filename= "model.pkl"

with open(filename, 'rb') as file:
    model = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    X_test_new = [x for x in request.form.values()]

    #print(sgd_clf.predict(X_test_new_count))

    prediction = model.predict(X_test_new)

    output = prediction[0]

    return render_template('index.html', prediction_text='This text belongs to {} '.format(output))


if __name__ == "__main__":
    app.run(debug=True)

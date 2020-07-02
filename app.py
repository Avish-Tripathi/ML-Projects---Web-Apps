from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('template/index.html')

@app.route('/predict',methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]
    final = [np.array(features)]
    Predict = model.predict(final)

    output = round(Predict[0], 4)
#     if(float(output)<100):
    return render_template('template/index.html', prediction_text='Predicted Percentile is {}'.format(output))
#     else:
#          return render_template('Home.html', prediction_text='Predicted Percentile is {}'.format('100'))

if __name__ == "__main__":
    app.run()

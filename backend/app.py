from flask import Flask, request, jsonify
import pickle
import pandas as pd
# -- module pipelining
from sklearn.base import BaseEstimator, TransformerMixin
# dataset
# Create a class to select numerical or categorical columns 
class OldDataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names
    def fit(self, X, y=None):
        return self
    def transform(self, X):
        return X[self.attribute_names].values

# -- APP
app = Flask(__name__)

# import model
with open ('pipeline_feature.pkl','rb') as pipe:
    pipeline_feature = pickle.load(pipe)

with open ('pipeline_model.pkl','rb') as pipe1:
    pipeline_model = pickle.load(pipe1)
@app.route("/predict", methods=['POST'])
def model_prediction():
    cl = eval(request.args.get('cl'))
    cw = eval(request.args.get('cw'))
    cb = eval(request.args.get('cb'))
    en = eval(request.args.get('en'))
    hp = eval(request.args.get('hp'))
    ct = eval(request.args.get('ct'))
    hh = eval(request.args.get('hh'))
    ft = request.args.get('ft')
    dw = request.args.get('dw')
    new_data = pd.DataFrame([cl, cw, cb, en, hp, ct, hh, ft, dw]).T
    new_data.columns = ['carlength', 'carwidth', 'curbweight', 'enginesize', 'horsepower', 'citympg','highwaympg','fueltype', 'drivewheel'] 
    scale = pipeline_feature.transform(new_data)
    res = pipeline_model.predict(scale)
    response = {'status':'success',
            'code':200,
            'data':{'result':str(round(res[0],2))}
            }
    return jsonify(response)
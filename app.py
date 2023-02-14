# Import libraries
#import numpy as np
import pandas as pd
from flask import Flask, request
import pickle
import shap
#import json
import unittest

app = Flask(__name__)

#Définition chemin d'accès aux fichiers
#PATH='C:/Users/valev/Projet-7/repo_git_api/'

#Test unitaire qui vérifie si la prédiction renvoyée par la fonction est bien une valeur entre 0 et 1
#def value_predict(self):
#    if self.assertTrue(self,0<=y<=1): #doit être entre 0 et 1
#        return True
#    return False

# Load data
read_csv = pd.read_csv('sampled.csv',delimiter= ',')
#read_csv=read_csv.drop(columns='index')
read_csv.set_index("SK_ID_CURR", drop=False, inplace=True)
print (read_csv)

# Load the model
model = pickle.load(open('model.pkl','rb'))

#return probability
@app.route('/predict',methods=['GET'])
def predict():
    #Get the data from the POST request.
    numID = request.args
    numeroClient = int(numID['numeroClient'])
    print("numeroClient ", numeroClient)
    # Make prediction using model loaded from disk as per the data.
    X_id = read_csv.loc[numeroClient:numeroClient]
    print("test id " , X_id)
    prediction = model.predict_proba(X_id)[:,1]
    print(prediction)
    #value_predict(float(prediction))
    # SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(read_csv)

    explanation_val = explainer.shap_values(X_id)
    sv=pd.DataFrame(shap_values[0].values[:,0])
    ev=explainer.expected_value[0]
    return  '[{},{},{},{}]'.format(float(prediction), 
                                        sv.to_json(), 
                                        ev, 
                                        pd.Series(explanation_val).to_json()) 

def getScoreUtilisateur(numeroUtilisateur):
    # Make prediction using model loaded from disk as per the data.
    X_id = read_csv.loc[numeroUtilisateur:numeroUtilisateur]
    prediction = model.predict_proba(X_id)[:,1]
    return prediction

   
if __name__ == '__main__':
    app.run(port=5000, debug=True)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#class TestStringMethods(unittest.TestCase):
#
#    def testavecUtilisateur100002(self): 
#        scoreUtilisateur = getScoreUtilisateur(100002)
#        self.assertGreaterEqual(scoreUtilisateur, 0)
#        self.assertLessEqual(scoreUtilisateur, 1)
        

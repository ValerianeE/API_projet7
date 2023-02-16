# Import libraries
import pandas as pd
from flask import Flask, request
import pickle
import shap

app = Flask(__name__)

#Définition chemin d'accès aux fichiers
#PATH='C:/Users/valev/Projet-7/repo_git_api/'

# Load data
read_csv = pd.read_csv('sampled.csv',delimiter= ',')
read_csv.set_index("SK_ID_CURR", drop=False, inplace=True)

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
    # SHAP values
    explainer = shap.TreeExplainer(model)
    shap_values = explainer(read_csv)

    sv=pd.DataFrame(shap_values[0].values[:,0])
    ev=explainer.expected_value[0]
    return  '[{},{},{}]'.format(float(prediction), 
                                        sv.to_json(), 
                                        ev,) 

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


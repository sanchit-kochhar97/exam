from flask import Flask, request, Response 
import jsonpickle
import pickle
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load the pickled data and store it in a global variable
with open('finalized_model.sav', 'rb') as f:
    model = pickle.load(f)
   


@app.route('/api/test', methods=['GET'])
def test():
    # Model code
    response = {'message': 'API hit iimv'}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")





@app.route('/api/testmodel', methods=['POST'])
def process_form():
    data = request.form
    data = model.predict([[float(data['testdata'])]])  
    data_str = ", ".join(str(x) for x in data)
    return data_str


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
from flask import Flask, request, Response 
import jsonpickle

app = Flask(__name__)



@app.route('/api/test', methods=['GET'])
def test():
    response = {'message': 'API hit iimv'}
    # encode response using jsonpickle
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype="application/json")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
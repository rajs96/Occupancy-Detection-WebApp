# import necessary modules
from flask import Flask, render_template, request, Response,json,jsonify
import numpy as np

# initialize application
app = Flask(__name__,static_folder='js')

# load keras model
from keras.models import load_model
model = load_model('model.h5')

# define the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    jsonData = request.get_json()
    X = np.array(
      [[float(jsonData['temperature']),
      float(jsonData['humidity']),
      float(jsonData['C02']),
      float(jsonData['light']),
      float(jsonData['humidity_ratio'])]])
    print(X)
    print(X.shape)
    return custom_response(jsonData,201)


def custom_response(res, status_code):
  """
  Custom Response Function
  @res: the response to be sent (i.e. a JSON object)
  @status_code: the status code to be sent in the response
  """

  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )

# run the app
if __name__ == '__main__':
    app.run(debug=True)

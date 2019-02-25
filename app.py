# import necessary modules
from flask import Flask, render_template, request, Response,json,jsonify,redirect,url_for
import numpy as np

# initialize application
app = Flask(__name__,static_folder='js')

# load keras model
from keras.models import load_model
model = load_model('model.h5')
model._make_predict_function()


# import scaler for particular training data
from scaleData import scale_data


@app.route('/predict',methods=['GET','POST'])
def predict():
    # get the data from the fields on the front end
    # as json
    jsonData = request.get_json()

    # turn it in to a numpy array so
    # we can feed it into our model
    X = np.array(
      [[float(jsonData['temperature']),
      float(jsonData['humidity']),
      float(jsonData['light']),
      float(jsonData['C02']),
      float(jsonData['humidity_ratio'])]])
    
    # get the particular scaler for the dataset
    scaler = scale_data()

    # scale the data
    X = scaler.transform(X)
    
    # make the prediction based on our loaded model
    prediction = model.predict(X)

    print(prediction)

    # return redirect
    return Response(str(prediction[0,1]),201)

@app.route('/displayPrediction/<prob_occupied>',methods=['GET'])
def displayPrediction(prob_occupied):
  print("got here")
  return render_template('prediction.html',prediction=prob_occupied)

# define the route for the index page
@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(debug=True,host='0.0.0.0')

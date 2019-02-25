This is a very simple machine learning model web application. The app takes in 5 features about a room and outputs whether or not the room is occupied. The application has an included Dockerfile to containerize the application and it has also been deployed using AWS's Elastic Beanstalk


# How to run locally on your machine
## Run the server
1. Create a virtual environment using venv or conda.
2. Install the necessary dependencies.
`pip install -r requirements.txt`
3. Run the application
`python app.py`

Note: There is not extensive error checking on REST calls and inputs (make sure you enter in all floats!): this is simply to be used as a starting point for creating a full stack machine learning model web application. 
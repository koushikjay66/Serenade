#This is a simple Hallo World Application for recruitment states of Ki Reply

import os
import sys


# Bug with Flask and Python on Dockerized Import ?????
sys.path.append(os.getcwd())

from flask import Flask

from web.rest_controllers.hello_world import HelloWorldRestController






#Initialize the Flask Application
app = Flask(__name__)



# Initialize Rest Endpoints
hello_world_controller:HelloWorldRestController=HelloWorldRestController(flask_app=app)
hello_world_controller.register_routes()




# Or we can also do in this way .... 
@app.route("/v2/sayhello", methods = ['GET'])
def v2_say_hello():
    
    return {"message": "Hello and Welcome"}


    
    if __name__ == "__main__":
        app.run(debug=True)
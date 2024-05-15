
from flask import Flask, Blueprint
from web.blueprints import RestApiController


class HelloWorldRestController(RestApiController): 
    
    def __init__(self, flask_app: Flask) -> None:
        self.flask_app:Flask= flask_app
        self.hello_world_blueprint:Blueprint = Blueprint("hello_world_bp", __name__, url_prefix="/v1")
        
        super().__init__(flask_app)
        
    
    def register_routes(self) -> None:
        self.hello_world_blueprint.route("/sayhello", methods=['GET'])(self.say_hello)
        self.flask_app.register_blueprint(blueprint=self.hello_world_blueprint)
        return super().register_routes()
    
    
    
    def say_hello(self):
        return {"message": "Hello and Welcome"}
    

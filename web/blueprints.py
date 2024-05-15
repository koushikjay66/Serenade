from abc import ABC, abstractmethod

from flask import Flask

class RestApiController(ABC):
    
    def __init__(self, flask_app:Flask) -> None:
        self.flask_app:Flask=flask_app
        
    
    
    @abstractmethod
    def register_routes(self)->None:
        pass
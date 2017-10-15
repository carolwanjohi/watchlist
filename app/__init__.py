from flask import Flask
from .config import DevConfig

# Initialising application
''' 
    Pass instance_relative_config to connect to instace/
'''
app = Flask(__name__,instance_relative_config = True)

# Setting upconfiguration
app.config.from_object(DevConfig)

''' 
    Connect to config.py file
    All its contents are appended to app.config
'''
app.config.from_pyfile("config.py")

from app import views
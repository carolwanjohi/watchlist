from flask import Flask
from .config import DevConfig

# Initialising application
app = Flask(__name__)

# Setting upconfiguration
app.config.from_object(DevConfig)

from app import views
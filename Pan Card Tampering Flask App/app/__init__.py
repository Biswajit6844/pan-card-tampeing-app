from flask import Flask
from . import config  # Import config from the same directory
from .config import ProductionConfig, DevelopmentConfig, TestingConfig

app = Flask(__name__)

# Set the ENV configuration if not already set
app.config["ENV"] = app.config.get("ENV", "development")  # Default to "development" if ENV is not set

if app.config["ENV"] == "development":
    app.config.from_object("app.config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("app.config.TestingConfig")
else:
    app.config.from_object("app.config.ProductionConfig")

from app import views

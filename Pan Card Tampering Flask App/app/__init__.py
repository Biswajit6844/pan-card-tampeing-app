from flask import Flask

app = Flask(__name__)

# Set the ENV configuration if not already set
app.config["ENV"] = app.config.get("ENV", "development")  # Default to "development" if ENV is not set

if app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.ProductionConfig")

from app import views

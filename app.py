from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://patib91326:nPzT8U7FCKZaHYfH@cluster0.bd8lxx7.mongodb.net/employees?retryWrites=true&w=majority"

mongo = PyMongo(app)

@app.route("/")
def index():
    mongo.db.users.insert_one({"name": "John"})
    return "Document inserted"

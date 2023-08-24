from flask import Flask
from flask_pymongo import PyMongo
from pymongo import MongoClient
app= Flask(__name__)

app.config["SECRET_KEY"]="4e40b9696f065f0049d2dd6bfa4aeb2fae686965"
cluster  = "mongodb://localhost:27017"
client=MongoClient(cluster,connect=False)

db = client.seconddatabase
from application import routes
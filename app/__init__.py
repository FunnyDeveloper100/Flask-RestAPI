from flask import Flask, Blueprint
from flask_restful import Api, Resource
from .domains import domain

       
app = Flask(__name__)
api = Api(app)

api.add_resource(domain, '/domain')





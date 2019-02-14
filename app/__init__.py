from flask import Flask

app = Flask (__name__)

app.config['SECRET_KEY'] = 'theolemecpascoollevendredimatinsiilapaseusmashlaveille'

from app import routes


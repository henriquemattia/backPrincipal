import json


from flask import Flask, request
from database import cursor
from database import connection


from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/mascu')
def rota_masculino():
    cursor.execute()

from cgi import print_form
import json


from flask import Flask, Request, Response
from database import cursor
from database import connection


from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/mascu')
def rota_masculino():
    cursor.execute("SELECT * FROM public.produtos WHERE categoria = 'masculino'")
    retorno = cursor.fetchall()
    return {"masculinos": retorno}
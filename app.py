from cgi import print_form
import json


from flask import Flask, make_response, jsonify
from database import cursor
from database import connection


from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# ROTA DE TODOS OS PRODUTOS
@app.route('/produtos')
def all_prosucts():
    cursor.execute("SELECT * FROM public.produtos")
    res = cursor.fetchall()
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'price': item[3],
                'desc_price': item[4]
            }
        )
     
    return make_response(
        jsonify(
            dados=dest
        )
    )





    # ROTA DSE PRODUTOS QUE ESTAO EM DESTAQUE NA PAGINA INICIAL
@app.route('/destaque')
def destaques():
    cursor.execute("SELECT * FROM public.produtos WHERE destaque = 'TRUE'")
    res = cursor.fetchall()
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'price': item[3],
                'desc_price': item[4]
            }
        )
     
    return make_response(
        jsonify(
            dados=dest
        )
    )


#  ROTA DE PRODUTOS MASCULINO
@app.route('/mascu')
def rota_masculino():
    cursor.execute("SELECT * FROM public.produtos WHERE categoria = 'masculino'")
    res = cursor.fetchall()
    return {"Masculino": res}


#  ROTA DE PRODUTOS FEMININOS
@app.route('/feminino')
def rota_feminino():
    cursor.execute("SELECT * FROM public.produtos WHERE categoria = 'feminino'")
    res = cursor.fetchall()
    return {"Feminio": res}


#  ROTA DE PRODUTOS INFANTIS
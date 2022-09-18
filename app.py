
from flask import Flask, make_response, jsonify, Response
from database import cursor


from flask_cors import CORS

app = Flask(__name__)

CORS(app)

# ROTA DE TODOS OS PRODUTOS
@app.route('/produtos')
def all_prosucts():
    cursor.execute("SELECT * FROM produtos p FULL OUTER JOIN images i ON p.img_id = i.id WHERE is_available = 'TRUE'")
    res = cursor.fetchall()
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'preco': item[3],
                'desc_preco': item[4],
                'rota': item[5],
                'img_main': item[10],
                'img_front': item[11],
                'img_right': item[12],
                'img_left': item[13],
                'img_back': item[14]
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
    cursor.execute("SELECT * FROM produtos p FULL OUTER JOIN images i ON p.img_id = i.id WHERE destaque = 'TRUE' and is_available = 'TRUE'")
    res = cursor.fetchall()
    dest = list()
    for item in res:
        dest.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'preco': item[3],
                'desc_preco': item[4],
                'rota': item[5],
                'img_main': item[10],
                'img_front': item[11],
                'img_right': item[12],
                'img_left': item[13],
                'img_back': item[14]
            }
        )
    return make_response(
        jsonify(
            dados=dest
        )
    )


#  ROTA DE PRODUTOS MASCULINO
@app.route('/masculino')
def rota_masculino():
    cursor.execute("SELECT * FROM produtos p FULL OUTER JOIN images i ON p.img_id = i.id WHERE categoria = 'masculino' and is_available = 'TRUE'")
    res = cursor.fetchall()
    masc = list()
    for item in res:
        masc.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'preco': item[3],
                'desc_preco': item[4],
                'rota': item[5],
                'img_main': item[10],
                'img_front': item[11],
                'img_right': item[12],
                'img_left': item[13],
                'img_back': item[14]
            }
        )
    return make_response(
        jsonify(
            dados=masc
        )
    )


#  ROTA DE PRODUTOS FEMININOS
@app.route('/feminino')
def rota_feminino():
    cursor.execute("SELECT * FROM produtos p FULL OUTER JOIN images i ON p.img_id = i.id WHERE categoria = 'feminino' and is_available = 'TRUE'")
    res = cursor.fetchall()
    femin = list()
    for item in res:
        femin.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'preco': item[3],
                'desc_preco': item[4],
                'rota': item[5],
                'img_main': item[10],
                'img_front': item[11],
                'img_right': item[12],
                'img_left': item[13],
                'img_back': item[14]
            }
        )
    return make_response(
        jsonify(
            dados=femin
        )
    )


#  ROTA DE PRODUTOS INFANTIS

# ROTA DE TESTE MASCULINO
@app.route('/ams')
def rota_ams():
    cursor.execute("SELECT * FROM produtos p FULL OUTER JOIN images i ON p.img_id = i.id WHERE categoria = 'masculino' and is_available = 'TRUE' ")
    res = cursor.fetchall()
    print(res)
    ams = list()
    for item in res:
        ams.append(
            {
                'id': item[0],
                'categoria': item[1],
                'nome': item[2],
                'preco': item[3],
                'desc_preco': item[4],
                'rota': item[5],
                'img_main': item[10],
                'img_front': item[11],
                'img_right': item[12],
                'img_left': item[13],
                'img_back': item[14]
            }
        )
    return  make_response(
        jsonify(
            dados=ams
        )
    )
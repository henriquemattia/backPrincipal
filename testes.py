# import json


# from flask import Flask, request
# from database import cursor
# from database import connection


# from flask_cors import CORS

# app = Flask(__name__)

# CORS(app)



#            ROTA DE TODOS OS PRODUTOS 
# @app.route('/produtos')
# def all_products():
    
#     list = [{"masculino": [{
#                         "image": "camisa",
#                         "valor": "R$ 344",
#                         "valorDesc": "R$ 500",
#                         "name": "camisa Masculina",
#                         "rota": "camisa1"
#                         },
#                         {"image": "moleton",
#                         "valor": "R$ 555",
#                         "valorDesc": "R$ 222",
#                         "name": "moleton Masculina",
#                         "rota": "moleton"
#                     }]},
#             {"feminino": [{
#                         "image": "camisa inverno",
#                         "valor": "R$ 50",
#                         "valorDesc": "R$ 100",
#                         "name": "camisa Feminina",
#                         "rota": "camisa2"
#                         },
#                         {
#                         "image": "camisa verao",
#                         "valor": "R$ 300",
#                         "valorDesc": "R$ 200",
#                         "name": "camisa Feminina",
#                         "rota": "camisa2"
#                     }]}
#             ]
                
#     return json.dumps(list)

    # TEMPORARIO! // TESTE 

# @app.route('/produtos')
# def all_products():
    
#     list =  [{ "masculino": {
#                     "image": "camisa",
#                     "valor": "R$ 344",
#                     "valorDesc": "R$ 500",
#                     "name": "CAMISA MASCULINA",
#                     "rota": "camisa1"
#                     },
#                     "feminino": {
#                     "image": "camisa",
#                     "valor": "R$ 50",
#                     "valorDesc": "R$ 100",
#                     "name": "CAMISA FEMININA",
#                     "rota": "camisa2"
#                     }
#                 }
#              ]
#     return json.dumps(list)


    # ROTAS DAS SESSOES INDIVIUDAIS
        
    #   fazer um select somente na tabela de produtos mascuolino 
# @app.route('/masculino')
# def prod_masculino():

#     masc_prods = [{
#                     "image": "camisa",
#                     "valor": "R$ 344",
#                     "valorDesc": "R$ 500",
#                     "name": "CAMISA VERMELHA",
#                     "rota": "camisa-vermelha"
#                     },
#                     {
#                     "image": "camisa",
#                     "valor": "R$ 50",
#                     "valorDesc": "R$ 200",
#                     "name": "CAMISA LARANJA",
#                     "rota": "camisa-laranja"
#                     }
#                    ]
#     return json.dumps(masc_prods)
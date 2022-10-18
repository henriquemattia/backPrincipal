from flask import Flask, request
from database import cursor
from database import connection


from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/register", methods=["POST"])
def create_user():
    body = request.json
    username = body["name"]
    email = body["email"]
    password =body["password"]
    
    cursor.execute(f"INSERT INTO users (name, email, password) VALUES ('{username}', '{email}', '{password}');")
    connection.commit()

    return {"ola": "tudo certo?"}


# Rota de verificaçaode usuario no banco de dados
@app.route("/login", methods=["GET"])
def verfiy_users():
    body = request.json
    email = body["email"]
    password =body["password"]
    
    print(email)
    print(password)
    
    # emailVerify = cursor.execute(f"SELECT email FROM users WHERE email = '{email}'"), cursor.fetchall()
    # passverify = cursor.execute(f"SELECT password FROM users WHERE password = '{password}'"), cursor.fetchall()
    cursor.execute(f"SELECT * FROM users WHERE email ={email} AND password ={password}")
    cursor.fetchall()    
    
        

        
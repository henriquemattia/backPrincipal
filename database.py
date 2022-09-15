from flask import Flask
import psycopg2
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()
connection = psycopg2.connect(host=os.environ["DB_HOST"],
                              dbname=os.environ["DB_NAME"],
                              user=os.environ["DB_USER"],
                              password=os.environ["DB_PASS"])
cursor = connection.cursor()

# username = 'body["username"]'
# email = 'opse'
# password ='poze'
    
#     # print(username)
#     # print(email)
#     # print(password)
#     # print(confirmPassword)
    
# cursor.execute(f"INSERT INTO users (name, email, password) VALUES ('{username}', '{email}', '{password}');")
# connection.commit()

# cursor.execute("INSERT INTO users (name, email, password) VALUES ('henrique', 'askjdn@emial.com', 'sneha123');")
# connection.commit()


# CREATE TABLE users (id bigserial primary key, name VARCHAR, email VARCHAR, password VARCHAR)
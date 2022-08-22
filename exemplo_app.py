from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>hello pessaol!!</h1>"
 
# insegur0!! pode ser rodado javaScrip dentro dele por iss oa estençao makup safe
@app.route("/inseguro/<path:subpath>")
def inseguro(subpath):             #para teste) http://localhost:5000/inseguro/<script>alert('oi')</script>
    return f"{subpath}"

# seguro pois está usando a ferramenta qeu limita o uso de escrips dentro da rota!
@app.route("/seguro/<path:subpath>")
def seguro(subpath):
    return f"{escape(subpath)}"

# usando  o INT poara definir o tipo de dado que vai ficar dentro do <> diamante
@app.route("/conversor/<int:numero>")
def conversor_numero(numero):
    return f" O numero é: {numero}"


@app.route("/template")
def template_fixo():
    return render_template("index.html")


@app.route("/template-dinamico/<name>")
def template_dinamico(name):
    return render_template("dinamico.html", name=name, name_2=19834712983)
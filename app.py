from flask import Flask, jsonify, request, render_template 
from flask_cors import CORS, cross_origin #conda install flask-cors

app =   Flask(__name__)
# cors = CORS(app, resources={r"/filmes": {"origins": "*"}})
# app.config['CORS_HEADERS'] = 'Content-Type'
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# CORS(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/grafico")
def grafico():
    return render_template("grafico.html")
    
@app.route('/filmes', methods = ['GET'])
def ReturnJSON():
    if(request.method == 'GET'):
        data = [
                {"label": "Ação", "value" : 15},
                {"label": "Terror", "value" : 23},
                {"label": "Comedia", "value" : 5},
                {"label": "Guerra", "value" : 3},
                {"label": "Ficção", "value" : 50}
        ]

        return jsonify(data)
  
if __name__=='__main__':
    app.run(debug=True, host="localhost", port=3000)
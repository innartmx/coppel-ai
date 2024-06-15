from flask import Flask,jsonify,request
from flask_cors import CORS, cross_origin
import rag_chat as rag_chat
from flask import send_file
from flask import render_template 

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/") 
def hello(): 
    return render_template('index.html') 

# Endpoint para verificar que el api esté funcionando
@app.route("/health")
@cross_origin()
def healthcheck():
    return "Hi, I'm Coppel AI and I'm working properly"

# Endpoint para enviar una pregunta al modelo de AI
@app.route("/rag/chat", methods=['POST'])
@cross_origin()
def sendQuestion():
    data = request.json
    respuesta = rag_chat.query_rag(data.get('question'))
    res = {
        "result": respuesta["respuesta"],
        "source": respuesta["fuentes"]
    }
    return jsonify(res)

# Endpoint para descargar un documento
@app.route("/download", methods=['GET'])
@cross_origin()
def downloadDocument():
    docName = request.args.get("filename")
    path = "docs/" + docName
    return send_file(path, as_attachment=True)
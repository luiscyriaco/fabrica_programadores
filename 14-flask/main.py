from flask import Flask #Importa somente o módulo Flask

app = Flask(__name__) #app é uma variável que inicia nossa aplicação

from routes import *

if __name__ == '__main__':
    app.run(debug=True)

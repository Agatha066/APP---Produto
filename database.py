from pymongo import MongoClient
import certifi

MONGO_URI = 'mongodb+srv://agathacristinaf2014:Agathacristina12@cluster0.ews7bp6.mongodb.net/?retryWrites=true&w=majority'

ca = certifi.where()

def dbConnect():
    try:
        cliente = MongoClient(MONGO_URI, tlsCAFile=ca)
        db = cliente['dbb_produtos_app']
    except ConnectionError:
        print("Error de conexão com o BD!")
    return db
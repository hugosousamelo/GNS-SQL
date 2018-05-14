#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import *
from modeles import modeleGNS

app = Flask(__name__)
app.secret_key

@app.route( "/parties" , methods = ['GET'] )
def getLesParties():
	lesParties = modeleGNS.getPartie()
	corpsReponse = json.dumps( lesParties )
	reponse = make_response( corpsReponse )
	reponse.mimetype = "application/json"
	reponse.status_code = 200
	return reponse

@app.route( '/parties/<numeroPartie>' , methods = ['GET'])
def consulterPartie(numeroPartie):
	laPartie = modeleGNS.getPartie(numeroPartie)
	corpsReponse = json.dumps( laPartie )
	reponse = make_response( corpsReponse )
	reponse.mimetype = "application/json"
	reponse.status_code = 200
	return reponse
	
@app.route( '/parties/<numeroPartie>' , methods = ['DELETE'])
def supprimerPartie(numeroPartie):
	laPartie = modeleGNS.annulerPartie(numeroPartie)
	corpsReponse = json.dumps( laPartie )
	reponse = make_response( corpsReponse )
	reponse.mimetype = "application/json"
	reponse.status_code = 200
	return reponse
	
if __name__ == "__main__":
	app.run( debug = True , host = '0.0.0.0' , port = 5000 )


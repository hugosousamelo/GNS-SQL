#!/usr/bin/python
# -*- coding: utf-8 -*-


import mysql.connector

connexionBD = None

def getConnexionBD() :
	global connexionBD
	try :
		if connexionBD == None :
			connexionBD = mysql.connector.connect(
					host = 'localhost' ,
					user = 'root' ,
					password = 'azerty' ,
					database = 'gns'
				)
		return connexionBD
	except :
		return None

def getPartie() :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select * from Partie;
				'''
		curseur.execute(requete, () )
		enregistrement = curseur.fetchall()
		parties = []
		for unEnregistrement in enregistrement:
			unePartie = {}
			unePartie[ 'numeroPartie' ] = unEnregistrement[ 0 ]
			unePartie[ 'dateCreation' ] = str(unEnregistrement[ 1 ])
			unePartie[ 'initiatiateur' ] = unEnregistrement[ 2 ]
			unePartie[ 'adversaire' ] = unEnregistrement[ 3 ]
			unePartie[ 'vainqueur' ] = unEnregistrement[ 4 ]
			unePartie[ 'suivant' ] = unEnregistrement[ 5 ]
			unePartie[ 'couleurInitiateur' ] = unEnregistrement[ 6 ]
			unePartie[ 'couleurAdversaire' ] = unEnregistrement[ 7 ]
			
			lesJoueurs = getJoueur()
			
			for unJoueur in lesJoueurs:
				if unePartie['initiatiateur'] == unJoueur['numeroJoueur']:
					unePartie['initiatiateur'] = unJoueur['numeroJoueur']
					
			for unJoueur in lesJoueurs:
				if unePartie['adversaire'] == unJoueur['numeroJoueur']:
					unePartie['adversaire'] = unJoueur['numeroJoueur']
			
			lesCouleurs = getCouleur()		
			
			for uneCouleur in lesCouleurs:
				if unePartie['couleurAdversaire'] == uneCouleur['numeroCouleur']:
					unePartie['couleurAdversaire'] = uneCouleur['numeroCouleur']
			
			for uneCouleur in lesCouleurs:
				if unePartie['couleurInitiateur'] == uneCouleur['numeroCouleur']:
					unePartie['couleurInitiateur'] = uneCouleur['numeroCouleur']
					
			parties.append(unePartie)
		curseur.close()
		return parties
	except :
		return None



def getJoueur():
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select * from Joueur;
				'''

		curseur.execute(requete, )

		enregistrement = curseur.fetchall()

		joueurs = []
		
		for unEnregistrement in enregistrement:
			unJoueur = {}
			unJoueur[ 'numeroJoueur' ] = unEnregistrement[ 0 ]
			unJoueur[ 'nomJoueur' ] = unEnregistrement[ 1 ]
			unJoueur[ 'mdpJoueur' ] = unEnregistrement[ 2 ]
			joueurs.append(unJoueur)
		curseur.close()
		return joueurs
	except :
		return None


	
def getCouleur():
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select * from Couleur;
				'''

		curseur.execute(requete, )
		enregistrement = curseur.fetchall()

		couleur = []
			
		for unEnregistrement in enregistrement:
			uneCouleur = {}
			uneCouleur[ 'numeroCouleur' ] = unEnregistrement[ 0 ]
			uneCouleur[ 'nomCouleur' ] = unEnregistrement[ 1 ]
			couleur.append(uneCouleur)
		curseur.close()
		return couleur
	except :
		return None

def getPartie(numeroPartie) :
	try :
		curseur = getConnexionBD().cursor()
		requete = '''
					select * from Partie where numeroPartie = %s;
				'''
		curseur.execute(requete, (numeroPartie) )
		enregistrement = curseur.fetchone()
		numPartie = {}
		if enregistrement != None:
			numPartie[ 'numeroPartie' ] = enregistrement[0]
			numPartie[ 'dateCreation' ] = str(enregistrement[1])
			numPartie[ 'initiatiateur' ] = enregistrement[2]
			numPartie[ 'adversaire' ] = enregistrement[3]
			numPartie[ 'vainqueur' ] = enregistrement[4]
			numPartie[ 'suivant' ] = enregistrement[5]
			numPartie[ 'couleurInitiateur' ] = enregistrement[6]
			numPartie[ 'couleurAdversaire' ] = enregistrement[7]
		curseur.close()
		return numPartie
	except :
		return None
	
def annulerPartie(numeroPartie) :
	try :
		if getPartie(numeroPartie) == {}:
			return False
		curseur = getConnexionBD().cursor()
		requete = '''
					DELETE FROM Partie where numeroPartie = %s;
				'''
		curseur.execute(requete, (numeroPartie, ) )
		getConnexionBD().commit()
		curseur.close()	
		
		return True
	except :
		
		return None


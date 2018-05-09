Select * from Partie where vainqueur != null;
Select * from Partie where vainqueur = null;
Select * from Partie where adversaire = null;
Select * from Partie where initiateur = 5 or adversaire = 5 and vainquer != null;
Select * from Partie where vainquer = 5;
Select * from Partie where initiateur = 5 or adversaire = null;
Select * from Partie where suivant = 5;
Select * from Partie where initiateur != 5 and adversaire = null;
Select * from Partie ;


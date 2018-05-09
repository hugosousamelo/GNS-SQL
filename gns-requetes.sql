Select numero from Partie where vainqueur != null;
Select dateCreation from Partie where vainqueur = null;
Select * from Partie where adversaire = null;
Select * from Partie where initiateur = 5 or adversaire = 5 and vainquer != null;
Select * from Partie where vainquer = 5;
Select * from Partie where initiateur = 5 or adversaire = null;
Select * from Partie where suivant = 5;
Select * from Partie where initiateur != 5 and adversaire = null;
Select * from Partie ;

Select numeroPartie from Partie where vainqueur is not null;
Select dateCreation from Partie where vainqueur is null;
Select nomJoueur from Joueur inner join Partie where Joueur.numeroJoueur = Partie.initiateur and adversaire is null;
Select couleurInitiateur from Partie where initiateur = 5 and vainqueur is not null;
Select nomJoueur from Joueur inner join Partie where Joueur.numeroJoueur = Partie.adversaire and vainqueur = 5;
Select couleurAdversaire from Partie where initiateur = 5 and vainqueur is null;
Select nomJoueur from Joueur inner join Partie where Joueur.numeroJoueur = Partie.suivant and suivant = 5;
Select nomJoueur from Joueur inner join Partie where Joueur.numeroJoueur = Partie.vainqueur;

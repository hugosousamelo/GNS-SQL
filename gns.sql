#------------------------------------------------------------
#        Script MySQL.
#------------------------------------------------------------
drop database if exists gns;
create database gns default character set utf8 default collate utf8_general_ci ;
use gns;

#------------------------------------------------------------
# Table: Joueur
#------------------------------------------------------------

CREATE TABLE Joueur(
        numeroJoueur Int NOT NULL ,
        nomJoueur    Varchar (25) ,
        mdpJoueur    Varchar (25) ,
        PRIMARY KEY (numeroJoueur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Couleur
#------------------------------------------------------------

CREATE TABLE Couleur(
        numeroCouleur Int NOT NULL ,
        nomCouleur    Varchar (25) ,
        PRIMARY KEY (numeroCouleur )
)ENGINE=InnoDB;


#------------------------------------------------------------
# Table: Partie
#------------------------------------------------------------

CREATE TABLE Partie(
        numeroPartie    Int NOT NULL ,
        dateCreation    Date ,
        initiateur   Int ,
        adversaire  Int ,
        vainqueur  Int ,
        suivant  Int ,
        couleurInitiateur   Int ,
        couleurAdversaire Int ,
        PRIMARY KEY (numeroPartie )
)ENGINE=InnoDB;

ALTER TABLE Partie ADD CONSTRAINT FK_Partie_initiateur FOREIGN KEY (initiateur) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_adversaire FOREIGN KEY (adversaire) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_vainqueur FOREIGN KEY (vainqueur) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_suivant FOREIGN KEY (suivant) REFERENCES Joueur(numeroJoueur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_couleurInitiateur FOREIGN KEY (couleurInitiateur) REFERENCES Couleur(numeroCouleur);
ALTER TABLE Partie ADD CONSTRAINT FK_Partie_couleurAdversaire FOREIGN KEY (couleurAdversaire) REFERENCES Couleur(numeroCouleur);

INSERT INTO Joueur VALUES (1,"Nicolas","azerty");
INSERT INTO Joueur VALUES (2,"Ilona","azerty");
INSERT INTO Joueur VALUES (3,"Georges","azerty");
INSERT INTO Joueur VALUES (4,"Aïcha","azerty");
INSERT INTO Joueur VALUES (5,"Cody","azerty");

INSERT INTO Couleur VALUES (1,"Blanc");
INSERT INTO Couleur VALUES (2,"Noir");

INSERT INTO Partie VALUES (1,"18/05/01",5,2,2,null,1,2);
INSERT INTO Partie VALUES (2,"18/05/01",5,2,5,null,2,1);
INSERT INTO Partie VALUES (3,"18/05/01",5,null,null,5,1,null);
INSERT INTO Partie VALUES (4,"18/05/01",2,null,null,null,2,1);
INSERT INTO Partie VALUES (5,"18/05/02",5,1,null,1,1,2);
INSERT INTO Partie VALUES (6,"18/05/02",5,1,null,5,1,2);
INSERT INTO Partie VALUES (7,"18/05/02",1,null,null,null,null,2);
INSERT INTO Partie VALUES (8,"18/05/02",1,null,null,null,null,2);
INSERT INTO Partie VALUES (9,"18/05/03",5,2,null,2,1,2);
INSERT INTO Partie VALUES (10,"18/05/03",2,1,2,null,2,1);


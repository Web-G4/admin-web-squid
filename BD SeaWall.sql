#CREA BASE DE DATOS
DROP DATABASE IF EXISTS SEAWALL;
CREATE DATABASE IF NOT EXISTS SEAWALL;

#ABRE BASE DE DATOS
USE SEAWALL;

DROP TABLE IF EXISTS Surfer;	#Surfer('username', pass, namePrivilege)--namePrivilege -> Privilege(name)
DROP TABLE IF EXISTS Rule;	#Rule(nameURL, 'idRule', isContent, nameSurfer, description, allow, rFrom, rTo)--nameSurfer -> Surfer(username)
DROP TABLE IF EXISTS Privilege;	#Privilege('name', isBlock)
DROP TABLE IF EXISTS Content;	#Content('nameContent', urlList)
DROP TABLE IF EXISTS ActiveUser;#ActiveUser('idActiveUser', ipSurfer, nameSurfer)--nameSurfer -> Surfer(username)
DROP TABLE IF EXISTS RuleList;	#RuleList(surferAsigned, ruleAsigned)--surferAsigned -> Surfer(username), ruleAsigned -> Rule(idRule)

#CREANDO TABLAS

CREATE TABLE IF NOT EXISTS Privilege(
name VARCHAR(20),
isBlock BOOLEAN,
CONSTRAINT PK_Privilege PRIMARY KEY (name));

CREATE TABLE IF NOT EXISTS Surfer(
username VARCHAR(20),
pass VARCHAR(20),
namePrivilege VARCHAR(20),
CONSTRAINT PK_Surfer PRIMARY KEY (username),
CONSTRAINT FK_Surfer_Privilege FOREIGN KEY (namePrivilege) REFERENCES Privilege(name));

CREATE TABLE IF NOT EXISTS Rule(
nameURL VARCHAR(50),
idRule INT AUTO_INCREMENT UNSIGNED,
isContent BOOLEAN,
nameSurfer VARCHAR(30),
description TEXT,
allow BOOLEAN,
rFrom TIME,
rTo TIME,
CONSTRAINT PK_Rule PRIMARY KEY (idRule),
CONSTRAINT FK_Rule_Surfer FOREIGN KEY (nameSurfer) REFERENCES Surfer(username));

CREATE TABLE IF NOT EXISTS ActiveUser(
idActiveUser INT AUTO_INCREMENT UNSIGNED,
ipSurfer INT UNSIGNED,
nameSurfer VARCHAR(30),
CONSTRAINT PK_ActiveUser PRIMARY KEY (idActiveUser),
CONSTRAINT FK_ActiveUser_Surfer FOREIGN KEY (nameSurfer) REFERENCES Surfer(username));

CREATE TABLE IF NOT EXISTS RuleList(
surferAsigned VARCHAR(20),
ruleAsigned INT,
FOREIGN KEY (surferAsigned) REFERENCES Surfer(username),
FOREIGN KEY (ruleAsigned) REFERENCES Rule(idRule));

CREATE TABLE IF NOT EXISTS Content(
nameContent VARCHAR(30),
urlList TEXT,
CONSTRAINT PK_Content PRIMARY KEY (nameContent));

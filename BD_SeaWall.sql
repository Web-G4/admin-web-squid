#CREA BASE DE DATOS
DROP DATABASE IF EXISTS SEAWALL;
CREATE DATABASE IF NOT EXISTS SEAWALL;

#ABRE BASE DE DATOS
USE SEAWALL;

DROP TABLE IF EXISTS Surfer;
DROP TABLE IF EXISTS Rule;
DROP TABLE IF EXISTS Privilege;
DROP TABLE IF EXISTS Content;
DROP TABLE IF EXISTS ActiveUser;
DROP TABLE IF EXISTS RuleList;
#CREANDO TABLAS

CREATE TABLE IF NOT EXISTS Privilege(
namePrivilege VARCHAR(20),
isBlock BOOLEAN,
CONSTRAINT PK_Privilege PRIMARY KEY (namePrivilege));

CREATE TABLE IF NOT EXISTS Surfer(
username VARCHAR(20),
pass VARCHAR(20),
namePrivilege VARCHAR(20) NOT NULL,
CONSTRAINT PK_Surfer PRIMARY KEY (username),
CONSTRAINT FK_Surfer_Privilege FOREIGN KEY (namePrivilege) REFERENCES Privilege(namePrivilege));

CREATE TABLE IF NOT EXISTS Rule(
nameURL VARCHAR(50),
idRule INT UNSIGNED AUTO_INCREMENT,
isContent BOOLEAN,
description TEXT,
allow BOOLEAN,
rFrom TIME,
rTo TIME,
CONSTRAINT PK_Rule PRIMARY KEY (idRule));

CREATE TABLE IF NOT EXISTS ActiveUser(
idActiveUser INT UNSIGNED AUTO_INCREMENT,
ipSurfer INT UNSIGNED,
nameSurfer VARCHAR(20),
CONSTRAINT PK_ActiveUser PRIMARY KEY (idActiveUser),
CONSTRAINT FK_ActiveUser_Surfer FOREIGN KEY (nameSurfer) REFERENCES Surfer(username));

CREATE TABLE IF NOT EXISTS RuleList(
privilegeAsigned VARCHAR(20),
ruleAsigned INT UNSIGNED AUTO_INCREMENT,
FOREIGN KEY (privilegeAsigned) REFERENCES Privilege(namePrivilege),
FOREIGN KEY (ruleAsigned) REFERENCES Rule(idRule));

CREATE TABLE IF NOT EXISTS Content(
nameContent VARCHAR(30),
urlList TEXT,
CONSTRAINT PK_Content PRIMARY KEY (nameContent));

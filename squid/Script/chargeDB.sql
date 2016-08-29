use SEAWALL;

delete from RuleList;
delete from ActiveUser;
delete from Surfer;
delete from Privilege;
delete from Content;
delete from Rule;

insert into Privilege values
("Administrador", 0);
insert into Privilege values
("OperarioPrensa", 0);
insert into Privilege values
("OperarioMantenimiento", 1);
insert into Privilege values
("Invitado", 1);


insert into Rule values
("games", 1, 1, "Te bloqueamos todo el lyg off leyens", 0, "14:20", "21:20");
insert into Rule values
("facebook.com", 2, 0, "Te vlokeamoh el livro de kras", 0, "13:20", "21:20");
insert into Rule values
("media", 3, 1, "Te permitimoh ve el iutuv", 1, "8:00", "21:00");

insert into Content values
("games","leagueoflegends.com
minijuegos.com
games");
insert into Content values
("media","youtube.com
kat.cr
video");

insert into RuleList values
(1, "OperarioPrensa", 1);
insert into RuleList values
(2, "OperarioPrensa", 2);
insert into RuleList values
(3, "OperarioPrensa", 3);
insert into RuleList values
(4, "OperarioMantenimiento", 3);


insert into Surfer values
("admin","admin","Administrador");
insert into Surfer values
("OperarioPrensa1","OperarioPrensa1","OperarioPrensa");
insert into Surfer values
("OperarioPrensa2","OperarioPrensa2","OperarioPrensa");
insert into Surfer values
("OperarioPrensa3","OperarioPrensa3","OperarioPrensa");
insert into Surfer values
("OperarioMant1","OperarioMant1","OperarioMantenimiento");
insert into Surfer values
("OperarioMant2","OperarioMant2","OperarioMantenimiento");
insert into Surfer values
("Invitado1","Invitado1","Invitado");


insert into ActiveUser values
(1, "192.168.20.174", "admin");
insert into ActiveUser values
(2,"192.168.20.203","OperarioPrensa1");
insert into ActiveUser values
(3,"192.168.20.218","OperarioPrensa3");
insert into ActiveUser values
(4,"192.168.20.219","OperarioMant2");
insert into ActiveUser values
(5,"192.168.20.220","Invitado1");


Nuestro proyecto administra el servidor proxy (squid), desarrollado por el grupo 3, a través de una interfaz gráfica. El proyecto debe correrse como superusuario

# Dependencias
Trabajar como superusuario

    sudo su

Podría requerir instalar la siguiente dependencia (en ubuntu):

    sudo apt install libmysqlclient-dev

Instalar dependencias de python con superusuario:

    source /usr/local/bin/virtualenvwrapper_lazy.sh #Podria ser necesario
    sudo pip install -r requeriments.txt

Instalar squid y crear carpetas de seawall

    sudo apt install squid3
    sudo mkdir -p /etc/squid/seawall/content/
    sudo mkdir -p /etc/squid/seawall/users/

Instalar mysql server y cargar archivo squid/Script/DB_SeaWall.sql:

    mysql -u root -p < squid/Script/DB_SeaWall.sql

Y si queres agrega dummy data:

    mysql -u root -p < squid/Script/chargeDB.sql

Estas obligado a correr el manage.py sobre el directorio del proyecto ya que si no el squidconf no funcionara (programacion de alta calidad)

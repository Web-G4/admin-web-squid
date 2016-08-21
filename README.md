Nuestro proyecto administra el servidor proxy (squid), desarrollado por el grupo 3, a través de una interfaz gráfica. El proyecto debe correrse como superusuario

# Dependencias
Trabajar como superusuario

    sudo su

Podría requerir instalar la siguiente dependencia (en ubuntu):

    sudo apt install libmysqlclient-dev

Instalar dependencias de python con superusuario:

    sudo pip install -r requeriments.txt

Si aparece el error "ImportError: No module named 'pip'" ejecutar:

    source /usr/local/bin/virtualenvwrapper_lazy.sh

Instalar squid y crear carpetas de seawall

    sudo apt install squid3
    sudo mkdir -p /etc/squid/seawall/content/
    sudo mkdir -p /etc/squid/seawall/users/

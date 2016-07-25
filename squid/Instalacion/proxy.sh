echo "=====================INSERTE CONTRASEÑA===================="
sudo su

echo "=====================INSTALANDO SQUID======================"
apt-get install squid3

cd 
echo "=====================CONFIGURANDO PAGINA 403==============="
cp Candado.png home.png /usr/share/squid3/icons/
echo "IMAGENES [HECHO]"
cp mime.conf /usr/share/squid3/
echo "MIME.CONF [HECHO]"
cp ERR_ACCESS_DENIED /usr/share/squid-langpack/en/
echo "ACCESS_DENIED [HECHO]"
echo "###########################################################"

echo "======================CONFIGURANDO IPTABLES================"




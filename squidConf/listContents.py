import MySQLdb
import os

ROUTE = "/etc/squid/seawall/content/"
#ROUTE = "/home/pi/ftp/Script/content/"

db = MySQLdb.connect(host='localhost', user='root',passwd='grupo2',
 db='SEAWALL' )

cur = db.cursor()

var = cur.execute('SELECT * FROM Content')
Content =  cur.fetchall()

#print("Content")
#print(Content)

try:
    os.chdir(ROUTE)
    os.system("pwd")
    os.system("touch something")
    os.system("sudo rm *")
except Exception, e:
    print(e)
    exit()
for c in Content:
    content = open(ROUTE+c[0],"w")
    content.write(c[1])
    content.close()
print("Done.")

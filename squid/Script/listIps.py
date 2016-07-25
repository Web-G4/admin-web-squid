import MySQLdb
import os

ROUTE = "/etc/squid3/seawall/users/"
#ROUTE = "/home/pi/ftp/Script/users/"

db = MySQLdb.connect(host='localhost', user='root',passwd='squid',
 db='SEAWALL' )

cur = db.cursor()

var = cur.execute('SELECT * FROM ActiveUser')
ActiveUser =  cur.fetchall()
var = cur.execute('SELECT * FROM Surfer')
Surfer =  cur.fetchall()

#print("ActiveUser")
#print(ActiveUser)
#print("Surfer")
#print(Surfer)

try:
    os.chdir(ROUTE)
    os.system("pwd")
    os.system("touch something")
    os.system("sudo rm *")
except Exception, e:
    print(e)
    exit()
privileges = []
for u in ActiveUser:
    userPrivilege = None
    for s in Surfer:
        if u[2] == s[0]:
            userPrivilege = s[2]
    if userPrivilege not in privileges:
        privileges.append(userPrivilege)
        user = open(ROUTE+userPrivilege,"w")
    else:
        user = open(ROUTE+userPrivilege,"a")
    user.write(u[1]+"\n")
    user.close()
os.system("squid3 -k reconfigure")
print("Done.")

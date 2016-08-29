def formatTime(time):
    hours, remainder = divmod(time.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return zeroFill(hours)+":"+zeroFill(minutes)

def zeroFill(number):
    if number <= 9:
        return "0"+str(number)
    else:
        return str(number)

import MySQLdb

#ROUTE = "/home/pi/ftp/Script/"
ROUTE = "/etc/squid3/"
ROUTE_USER = ROUTE+"seawall/users/"
ROUTE_CONTENT = ROUTE+"seawall/content/"

db = MySQLdb.connect(host='localhost', user='root',passwd='squid',
 db='SEAWALL' )

cur = db.cursor()

#TODO sacar activeuser
var = cur.execute('SELECT * FROM ActiveUser')
ActiveUser =  cur.fetchall()

#TODO sacar content
var = cur.execute('SELECT * FROM Content')
Content =  cur.fetchall()

var = cur.execute('SELECT * FROM Privilege')
Privilege =  cur.fetchall()

var = cur.execute('SELECT * FROM Rule')
Rule =  cur.fetchall()

var = cur.execute('SELECT * FROM RuleList')
RuleList =  cur.fetchall()

var = cur.execute('SELECT * FROM Surfer')
Surfer =  cur.fetchall()

#print("ActiveUser")
#print(ActiveUser)
#print("Content")
#print(Content)
#print("Privilege")
#print(Privilege)
#print("Rule")
#print(Rule)
#print("RuleList")
#print(RuleList)
#print("Surfer")
#print(Surfer)

db.close()

# Write Section

squidconf = open(ROUTE+"squid.conf","w")

header = """
### HEADER SECTION ###


acl SSL_ports port 443
acl Safe_ports port 80		# http
# acl Safe_ports port 21		# ftp
# acl Safe_ports port 443		# https
# acl Safe_ports port 70		# gopher
# acl Safe_ports port 210		# wais
# acl Safe_ports port 1025-65535	# unregistered ports
# acl Safe_ports port 280		# http-mgmt
# acl Safe_ports port 488		# gss-http
# acl Safe_ports port 591		# filemaker
# acl Safe_ports port 777		# multiling http
acl CONNECT method CONNECT
"""

main = ""

footer = """




### FOOTER SECTION ###


http_access deny !Safe_ports
http_access deny CONNECT !SSL_ports
http_access allow localhost manager
http_access deny manager
http_access allow localhost
http_access deny all
http_port 3128

coredump_dir /var/spool/squid

refresh_pattern ^ftp:		1440	20%	10080
refresh_pattern ^gopher:	1440	0%	1440
refresh_pattern -i (/cgi-bin/|\?) 0	0%	0
refresh_pattern .		0	20%	4320
"""

#ACL - Section
main += "\n\n\n\n### ACL SECTION ###\n\n"
for p in Privilege:
    main += "\n\n#ACL - " + p[0]
    main += "\nacl "+p[0]+"Ip src \""+ROUTE_USER+p[0]+"\"\n"
    ruleCounter = 1
    for acl in RuleList:
        if acl[1] == p[0]:
            for rule in Rule:
                if acl[2] == rule[1]:
                    main += "\nacl "+p[0]+"Rule"+str(ruleCounter)+"Time time MTWHF "+formatTime(rule[5])+"-"+formatTime(rule[6])
                    if rule[2] == 1:
                        main += "\nacl "+p[0]+"Rule"+str(ruleCounter)+"NameURL url_regex -i \""+ROUTE_CONTENT+rule[0]+"\"\n"
                    else:
                        main += "\nacl "+p[0]+"Rule"+str(ruleCounter)+"NameURL dstdomain "+rule[0]+"\n"
                    ruleCounter+=1


#ACCESS - Section
main += "\n\n\n\n### ACCESS SECTION ###\n\n"
main += """
acl djangoServer dst 192.168.1.103
http_access allow djangoServer
"""
for p in Privilege:
    main += "\n\n#ACCESS - " + p[0]
    ruleCounter = 1
    for acl in RuleList:
        print(acl, p)
        if acl[1] == p[0]:
            for rule in Rule:
                print("RULE",acl,rule)
                if acl[2] == rule[1]:
                    if rule[4] == 1:
                        allow = "allow"
                    else:
                        allow = "deny"
                    main += "\nhttp_access "+allow+ " " +p[0]+"Rule"+str(ruleCounter)+"Time "+p[0]+"Rule"+str(ruleCounter)+"NameURL "+p[0]+"Ip"
                    ruleCounter+=1
    if p[1] == 1:
        main += "\nhttp_access deny all "+p[0]+"Ip"
    else:
        main += "\nhttp_access allow all "+p[0]+"Ip"


squidconf.write(header+main+footer)
squidconf.close()
print("Done.")

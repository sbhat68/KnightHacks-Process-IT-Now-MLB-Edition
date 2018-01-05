import MySQLdb

db = MySQLdb.connect(host="zcoursey22.mysql.pythonanywhere-services.com", user="zcoursey22", passwd="ilRnR_22", db="zcoursey22$lahman")

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like

#cur.execute(SQLCommand)
cur.execute("SELECT playerID FROM Batting where yearID = '2005' AND HR= '51'")

tempSet=set()

# print all the first cell of all the rows
'''for row in cur.fetchall():
    b=row[0].split()
    if len(b)>=2:
        tempSet.add((b[0].lower(),b[1].lower()))
'''
#cmd = "select CONCAT(yearID" + ",' ', max("+ behaviors[behavior] + ")) FROM Batting WHERE playerID =" + " '" + playerId + "'"
#cur.execute(cmd)
for row in cur.fetchall():
	playerId=str(row[0])
	print(playerId)

db.close()


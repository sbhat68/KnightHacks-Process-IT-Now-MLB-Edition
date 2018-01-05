import MySQLdb

def parse(Sentence):
	db = MySQLdb.connect(host="zcoursey22.mysql.pythonanywhere-services.com", user="zcoursey22", passwd="ilRnR_22", db="zcoursey22$lahman")
	cur = db.cursor()
	words = Sentence.split()
	"""what, who, how"""
	whatStatus=False
	"""behavior: homeruns"""
	behaviorStatus=False
	"""adverb: most, least"""
	adverbStatus=False
	"""name"""
	nameStatus=False
	"""team name"""
	tNeamStatus=False
	"""year"""
	yearStatus=False

	nameSet=set()
	wWords={'what','who','how'}
	behaviors={'homeruns':'HR', 'runs':'R', 'hits':'H', 'games':'G', 'doubles':'2B', 'triples':'3B','team':'teamID', 'bats':'AB', 'strikeouts':'SO', 'intentional':'IBB', 'sacrifice':'SF', 'grounded':'GIDP', 'batted':'RBI'}
	adverbs={'most', 'least'}

	cur.execute("SELECT CONCAT (nameFirst, ' ', nameLast) FROM Master")

	for row in cur.fetchall():
	    temp=row[0].split()
	    if len(temp)>=2:
	        nameSet.add((temp[0].lower(), temp[1].lower()))




	for i in range(len(words)):
		w=words[i].lower()
		if w in wWords:
			whatStatus=True
			wWord=w
		elif w in behaviors:
			behaviorStatus=True
			behavior=w
		elif w in adverbs:
			adverbStatus=True
			adverb=w
		elif "1800"<w<"2100":
			yearStatus=True
			year=(w)

		elif i<len(words)-1 and (words[i].lower(),words[i+1].lower()) in nameSet:
			nameStatus=True
			name=words[i].lower()+" "+words[i+1].lower()

	if nameStatus:
		cmd = "select playerID FROM Master where CONCAT(nameFirst,' ',nameLast)='"+name+"'"
		cur.execute(cmd)
		for row in cur.fetchall():
			playerId=str(row[0])

	if not whatStatus:
		result="Invalid"
		"""how many"""
	elif whatStatus and behaviorStatus and nameStatus and yearStatus and not adverbStatus:
	    cmd = "SELECT" + " " + behaviors[behavior] + " " + "FROM Batting WHERE playerID =" + " '" + playerId + "' " + "AND yearID =" + " " + str(year)
	    cur.execute(cmd)
	    for row in cur.fetchall():
	        result=str(row[0])
	    """what year"""
	elif whatStatus and behaviorStatus and nameStatus and adverbStatus and not yearStatus:
		if adverb == 'most':
		    cmd = "select max("+ behaviors[behavior] + ") FROM Batting WHERE playerID =" + " '" + playerId + "'"
		else:
		    cmd = "select min("+ behaviors[behavior] + ") FROM Batting WHERE playerID =" + " '" + playerId + "'"
		cur.execute(cmd)
		for row in cur.fetchall():
			result=str(row[0])

		cmd = "select yearID FROM Batting WHERE playerID =" + " '" + playerId + "' AND "+ behaviors[behavior] +" = '" + result+"'"

		cur.execute(cmd)
		for row in cur.fetchall():
		    temp=row[0]
		    result = temp

		"""who"""
	elif whatStatus and behaviorStatus and not nameStatus and adverbStatus and yearStatus:

	    if adverb == 'most':
	        cmd = "select max("+ behaviors[behavior] + ") FROM Batting WHERE yearID ='" + year+"'"
	    else:
	        cmd = "select min("+ behaviors[behavior] + ") FROM Batting WHERE yearID =" + year
	    cur.execute(cmd)

	    for row in cur.fetchall():
	        result=(row[0])

	    cmd = "SELECT playerID FROM Batting where yearID = '"+ year +"' AND " +behaviors[behavior]+ "='"+str(result)+"'"

	    cur.execute(cmd)
	    for row in cur.fetchall():
	        result=(row[0])
	    cmd = "select CONCAT(nameFirst,' ',nameLast) FROM Master where playerID='"+str(result)+"'"
	    cur.execute(cmd)
	    for row in cur.fetchall():
	        result=str(row[0])


	else:
	    result = "Please choose another question"
	db.close()
	return result

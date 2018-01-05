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
	
	nameSet={}
	tNameSet={}
	wWords={'what','who','how'}
	behaviors={'homeruns':'HR', 'runs':'R', 'hits':'H'}
	adverbs={'most', 'least'}

	cur.execute("SELECT CONCAT (nameFirst, " ", nameLast) FROM Master")
	for row in cur.fetchall():
		temp=row[0].split()
		nameSet.add((temp[0].lower(), temp[1].lower()))

	cur.execute("SELECT CONCAT (nameFirst, " ", nameLast) FROM Master")
	for row in cur.fetchall():
		tNameSet.add(row)

	for i in range(words.size()):
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
			year=int(w)
		elif i<words.size()-1 and (words[i].lower(),words[i+1].lower()) in nameSet:
			nameStatus=True
			name=words[i].lower()+" "+words[i+1].lower()

	if nameStatus:
		cmd = "select playerID FROM Master where CONCAT(nameFirst," ",nameLast)="+name
		cur.execute(cmd)
		for row in cur.fetchall():
			playerId=str(row[0])

	if not whatStatus:
		result="Invalid"
		"""how many"""
	elif whatStatus and behaviorStatus and nameStatus and yearStatus and not adverbStatus:
		cmd = "select"+" "+behaviors[behavior]+" "+"FROM BATTING WHERE playerID ="+" "+playerId+" "+"and yearID ="+" "+str(year)
		cur.execute(cmd)
		for row in cur.fetchall():
			result=str(row[0])
		return result
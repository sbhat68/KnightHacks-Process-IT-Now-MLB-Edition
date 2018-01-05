import nltk
nltk.download()
from nltk.corpus import stopwords
stopWords = set(stopwords.words('english'))
stopWords
#sentence = "How many home runs did Barry Bonds hit in 2007?"
print("Sentence: ")
sentence = input()
from nltk.tokenize import word_tokenize
#nltk.download()
words = word_tokenize(sentence)
words
wordsFiltered = []
for w in words:
	w = w.lower()
	if w not in stopWords or w == "who" or w == "how" or w == "what" or w == "which" or w == "when" or w == "did" or w == "not" or w == "where":
		wordsFiltered.append(w)
print(wordsFiltered)

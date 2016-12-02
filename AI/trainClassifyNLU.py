from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import numpy
from sklearn.externals import joblib


dictWords = {}
dictLabels = {}
wordList = []
labelList = []
lines = []
wordCount = 0
labelCount = 0
file = "input.csv"
f = open(file, "r")
for line in f:
    line = line.lower()
    val = line.split(",")
    lines.append(val)
    if val[1].strip() not in labelList:
        labelList.append(val[1].strip())
        dictLabels[val[1].strip()] = labelCount
        labelCount+=1
    for word in val[0].split():
        if word not in wordList:
            wordList.append(word)
            dictWords[word] = wordCount
            wordCount+=1

print(len(wordList))
X_list = numpy.zeros(shape=(len(lines),len(wordList)))
Y_list = numpy.zeros(shape=(len(lines)))
for i in range(len(lines)):
    sent = lines[i][0].split()
    label = lines[i][1].strip()
    if label == 'food':
        Y_list[i] = 1
    elif label == 'price':
        Y_list[i] = 2
    else:
        Y_list[i] = 3
    for j in range(len(sent)):
        if sent[j] in wordList:
            X_list[i][dictWords[sent[j]]] = 1
classif = MultinomialNB()
cls = LogisticRegression()
randcls = RandomForestClassifier()
dtcls = DecisionTreeClassifier()
dtcls.fit(X_list,Y_list)
cls.fit(X_list,Y_list)
classif.fit(X_list, Y_list)
randcls.fit(X_list, Y_list)
joblib.dump(randcls, 'model.pkl')

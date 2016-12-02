from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.externals import joblib
import numpy

## the model does not hold total wordcount so you need to pass that in the testNLU module

foodList = ['mexican', 'chinese', 'indian', 'italian']
priceList = ['cheap', 'expensive', 'inexpensive', 'costly','moderate','medium']
locList = ['downtown', 'koreatown', 'bakersfield']

def nluClassifier(input):
    dictWords = {}
    dictLabels = {}
    wordList = []
    labelList = []
    lines = []
    wordCount = 55
    labelCount = 0

    # classif = MultinomialNB()
    # cls = LogisticRegression()
    dtcls = RandomForestClassifier()
    # dtcls = DecisionTreeClassifier()
    dtcls = joblib.load('model.pkl')
    #testing starts here

    test = input.lower()
    testarray = test.split()
    X = numpy.zeros(shape=(1,wordCount))
    for word in testarray:
        if word in wordList:
            X[0][dictWords[word]] = 1
    # print(classif.predict(X))
    # print(cls.predict(X))
    # print(randcls.predict(X))
    print(dtcls.predict(X))
    tArr = input.split()
    if dtcls.predict(X)[0] == 1:
        for word in foodList:
            if word in tArr:
                return {'food': word}
    if dtcls.predict(X)[0] == 2:
        for word in priceList:
            if word in tArr:
                return {'price': word}
    if dtcls.predict(X)[0] == 3:
        for word in locList:
            if word in tArr:
                return {'location': word}

print(nluClassifier("moderate priced"))
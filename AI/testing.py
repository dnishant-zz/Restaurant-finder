from nltk import  word_tokenize
import nltk
from nltk.tokenize import word_tokenize

dict = {
    "bakersfield":"location",
    "downtown":"location",
    "koreatown":"location",
    "university":"location",
    "cheap":"price",
    "medium":"price",
    "costly":"price",
    "expensive":"price",
    "inexpensive":"price",
    "moderate":"price",
    "indian":"food",
    "italian":"food",
    "mexican":"food",
    "chinese":"food"
}

def nluPOS(input):
    ans = {}
    a = nltk.pos_tag(input)
    for x in a:
        if(x[1] == 'NNP' or x[1] == "NN" or x[1] == "JJ" or x[1] == "NNS" or x[1] == "DT"):
            if(x[0] in dict):
                ans[dict[x[0]]] = x[0]
    return input

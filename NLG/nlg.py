# from database import search_restaurant_by_cuisine
# from database import search_restaurant
# from database import search_restaurant_by_price
# from database import search_restaurant_by_price_cuisine
# from database import search_restaurant_by_address
from Text-to-speech-api import speak
import database
from tabulate import tabulate
import subprocess
from prettytable import PrettyTable
from tempfile import TemporaryFile
from gtts import gTTS


flag = 1
input_dictionary = {"price": "medium", "location": "downtown", "cuisine": "chinese"}

cuisine_list = ["italian", "mexican", "indian", "chinese"]
price_list = ["cheap", "costly", "medium"]
location_list = ["downtown", "koreatown", "bakersfield", "university"]


def requestInfoPOS(flag):
    if flag == 1:
        return "Hi I am your food assistant"
    else:
        return "Tell me what you want!"


# a = requestInfoPOS(flag)


def requestInfoClassify(input_dictionary):
    if input_dictionary["price"] is None \
            and input_dictionary["cuisine"] is None \
            and input_dictionary["location"] in location_list:
        return "Which cuisine would you like to eat at " + input_dictionary["location"] + \
               "?\nAlso tell me the price range of the restaurant you would like to visit."

    '''if input_dictionary["price"] is None \
            and input_dictionary["cuisine"] is None \
                and input_dictionary[location] is None:
        return "Which cuisine would you like to eat?"+ \
               "? Also tell me the price range of the restaurant you would like to visit."'''

    if input_dictionary["price"] is None \
            and input_dictionary["location"] is None \
            and input_dictionary["cuisine"] in cuisine_list:
        return "At which location would you like to visit the " + input_dictionary["cuisine"] + \
               " Restaurant?\nWhat is the price range of the restaurant you would like to visit"

    '''if input_dictionary["price"] not in price \
            and input_dictionary["location"] not in location \
                and input_dictionary["cuisine"] is None:
        return "At which location would you like to visit the" \
               " Restaurant? What is the price range of the restaurant you would like to visit"'''

    if input_dictionary["cuisine"] not in price_list \
            and input_dictionary["location"] not in location_list \
            and input_dictionary["price"] in price_list:
        return "Where would you like to visit the " + input_dictionary["cheap"] + \
               "priced Restaurant?\nAlso what cuisine would you like to try?"
    '''
    if input_dictionary["cuisine"] not in price \
            and input_dictionary["location"] not in location \
                and input_dictionary["price"] is None:
        return "Where would you like to visit the "+ input_dictionary["cheap"] + \
                " Restaurant? What cuisine would you like to try?"'''

    if input_dictionary["price"] in price_list \
            and input_dictionary["cuisine"] in cuisine_list \
            and input_dictionary["location"] is None:
        return "At which place would you like to visit the " + \
               input_dictionary["price"] + " priced " + input_dictionary["cuisine"] + "Restaurant?"

    if input_dictionary["price"] in price_list \
            and input_dictionary["cuisine"] is None \
            and input_dictionary["location"] in location_list:
        return "What kind of cuisine would you like at the " + input_dictionary["price"] + "priced" + \
               " Restaurant at " + input_dictionary["location"] + "Restaurant?"

    if input_dictionary["price"] is None \
            and input_dictionary["cuisine"] in cuisine_list \
            and input_dictionary["location"] in location_list:
        return "What priced range " + input_dictionary["cuisine"] + " Restaurant would you like to visit" + \
               " in " + input_dictionary["location"] + "?"


#b = requestInfoClassify(input_dictionary)
#print(b)

def confirmInfo(input_dictionary):

    if input_dictionary["location"] in location_list \
            and input_dictionary["price"] in price_list \
            and input_dictionary["cuisine"] in cuisine_list:
        return "Would you like me to search for " + input_dictionary["price"] + " " + input_dictionary[
            "cuisine"] + " Restaurant in " + input_dictionary["location"] + "?"


'''c = confirmInfo(input_dictionary)
tts = gTTS(text=c, lang='en')
print(c)
tts.save("hello.mp3")
subprocess.call(["afplay", "hello.mp3"])'''


def getInfo(input_dictionary):
    global engine
    d, count = database.search_restaurant(input_dictionary["location"], input_dictionary["cuisine"],
                                          input_dictionary["price"])
    length = len(d)
    if count == 0:
        d = database.call_trade_off(input_dictionary["location"], input_dictionary["cuisine"],
                                    input_dictionary["price"])
        ans = "Sorry I could not find restaurants matching your interests. But here is a list of suggestions.\n"
        Text-to-speech-api.speak(ans)
        t = PrettyTable(['Name', 'Location', 'Cuisine', 'Price', 'Rating'])

        for k, v in d.items():
            t.add_row(v)
        ans += t.get_string()
        print(ans)
        #subprocess.call(["afplay", "hello.mp3"])
        return ans

    ans = "I have found " + str(length) + " Restaurants matching your interest.\n"
    ans += "Here is the list of Restaurants along with their name, rating and average price.+\n"
    Text-to-speech-api.speak(ans)
    #tts = gTTS(text=ans, lang='en')
    #tts.save("hello.mp3")

    t = PrettyTable(['Name', 'Location', 'Cuisine', 'Price', 'Rating'])
    for k, v in d.items():
        t.add_row(v)

    ans += t.get_string()
    # print(ans)
    print(ans)
    #subprocess.call(["afplay", "hello.mp3"])
    return ans

d = getInfo(input_dictionary)




from nlg import *


#input1={"price":"costly","location":"South Figueroa","cuisine":"Indian"}
handler={"price":"null","location":"null","cuisine":"null","price_status":"null","location_status":"null","cuisine_status":"null"}
handlerfornlg={"price":"null","location":"null","cuisine":"null"}
finalhandler={"price":"null","location":"null","cuisine":"null"}
def dm(input):
    if "price" in input:
        handler["price_status"]="filled"
        handlerfornlg["price"]=input["price"]

    if "location" in input:
        handler["location_status"]="filled"
        handlerfornlg["location"]=input["location"]

    if "cuisine" in input:
        handler["cuisine_status"]="filled"
        handlerfornlg["cuisine"]=input["cuisine"]

    if "price" not in input or "location" not in input or "cuisine" not in input:
        nlg.requestInfoClassify(handlerfornlg)
    else:
        nlg.confirmInfo(handlerfornlg)
        finalhandler["location"]=input["confirmed_location"]
        finalhandler["price"]=input["confirmed_price"]
        finalhandler["cuisine"]=input["confirmed_cuisine"]



    if "confirmed_price" in input:
        handler["price_status"]="confirmed"
        finalhandler["price"]=input["confirmed_price"]


    if "confirmed_location" in input:
        handler["location_status"]="confirmed"
        finalhandler["location"]=input["confirmed_location"]


    if "confirmed_cuisine" in input:
        handler["cuisine_status"]="confirmed"
        finalhandler["cuisine"]=input["confirmed_cuisine"]


    return finalhandler



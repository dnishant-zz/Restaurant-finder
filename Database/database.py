# import mysql.connector

import pymysql

cnx = pymysql.connect(user='root', password='fgjf,jgb', #used dummy password
                      host='127.0.0.1',
                      database='Saif_Test')

# print("connected")
# define insert function to insert restaurant details from excel to database
# address = 'koreatown'
# cuisine = 'italian'
# price = 'costly'
lb, ub = 0, 0

cuisine_list = []
price_list = []
location_list = []


def search_restaurant(address, cuisine, price):
    #print("in search restaurant")
    global lb
    global ub
    if price == "cheap":
        lb = 0
        ub = 13
    if price == "medium":
        lb = 14
        ub = 22
    if price == "costly":
        lb = 23
        ub = 50
    cur = cnx.cursor()
    count = 0
    query = "SELECT Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price, Restaurant_rating FROM Restaurant WHERE Restaurant_cuisine ='" + cuisine + "' " + \
            "AND Restaurant_address = '" + address + "' " + "AND Restaurant_price between " + str(lb) + " and " + str(
            ub) + " ORDER BY RAND() Limit 4"
    #print(query)
    cur.execute(query)
    restaurant_dict = {}
    for (Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price,
         Restaurant_rating) in cur:
        count += 1

        restaurant_dict[int(Restaurant_id)] = [str(Restaurant_name), str(Restaurant_address), str(Restaurant_cuisine),str(Restaurant_price),
                                               str(Restaurant_rating)]
    # print(Restaurant_name+","+Restaurant_address+","+Restaurant_cuisine)

    cnx.close()
    return restaurant_dict, count



def search_restaurant_by_cuisine(cuisine, cnx1,global_dict):

    query = "select * from Restaurant where Restaurant_cuisine ='" + cuisine + "' ORDER BY RAND() Limit 100;"

    cursor1 = cnx1.cursor()
    cursor1.execute(query)
    restaurant_dict = {}

    #print("cuisine query = "+query)
    count = 0
    for (Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price,
         Restaurant_rating) in cursor1:
        #print("in cuisine for loop")
        count += 1
        if len(global_dict) > 3:
            break
        if Restaurant_id not in global_dict:
            global_dict[int(Restaurant_id)] = [str(Restaurant_name), str(Restaurant_address),
                                               str(Restaurant_cuisine), str(Restaurant_price), str(Restaurant_rating)]

        # print(Restaurant_name+","+Restaurant_address+","+Restaurant_cuisine)
    '''if count == 0:
        restaurant_dict = no_result_query(cursor1)'''
    # cnx.close()
    #print("in cuisine")
    return global_dict


def search_restaurant_by_price(price, cnx1,global_dict):
    global ub
    global lb

    if price == "cheap":
        lb = 0
        ub = 13
    if price == "medium":
        lb = 14
        ub = 22
    if price == "costly":
        lb = 23
        ub = 50
    query = "select * from Restaurant where Restaurant_price between " + str(lb) + " and " + str(
            ub) + " ORDER BY RAND() Limit 100"
    #print("price query = "+ query)
    cursor1 = cnx1.cursor()
    cursor1.execute(query)
    restaurant_dict = {}
    # print(cursor1.rowcount)

    for (Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price,
         Restaurant_rating) in cursor1:
        #print("in price for loop")
        if len(global_dict) > 1:
            break
        if Restaurant_id not in global_dict:
            global_dict[int(Restaurant_id)] = [str(Restaurant_name), str(Restaurant_address),
                                               str(Restaurant_cuisine), str(Restaurant_price), str(Restaurant_rating)]
        # print(Restaurant_name+","+Restaurant_address+","+Restaurant_cuisine)
    '''if count == 0:
        restaurant_dict = no_result_query(cursor1)'''
    # cnx.close()
    #print("in price")
    return global_dict

'''
def search_restaurant_by_price_cuisine(price, cuisine):
    global ub
    global lb
    if price == "cheap":
        lb = 0
        ub = 13
    if price == "medium":
        lb = 14
        ub = 22
    if price == "costly":
        lb = 23
        ub = 50
    query = "select * from Restaurant where Restaurant_cuisine =" + "'" + cuisine + "'" + " and Restaurant_price between " + str(
            lb) + " and " + str(ub) + " Limit 4"

    cursor1 = cnx.cursor()
    cursor1.execute(query)
    restaurant_dict = {}
    # print(cursor1.rowcount)

    for (Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price,
         Restaurant_rating) in cursor1:
        restaurant_dict[1, int(Restaurant_id)] = [str(Restaurant_name), str(Restaurant_address),
                                                  str(Restaurant_cuisine), str(Restaurant_price),
                                                  str(Restaurant_rating)]

        print(Restaurant_name + "," + Restaurant_address + "," + Restaurant_cuisine)
    if count == 0:
        restaurant_dict = no_result_query(cursor1)
    cnx.close()
    return restaurant_dict'''


def search_restaurant_by_address(address, cnx1, global_dict):

    query = "select * from Restaurant where Restaurant_address = '" + address + "' ORDER BY RAND() Limit 100;"
    cursor1 = cnx1.cursor()
    cursor1.execute(query)
    restaurant_dict = {}
    #print("address query = "+query)
    # print(cursor1.rowcount)
    count = 0
    for (Restaurant_id, Restaurant_name, Restaurant_address, Restaurant_cuisine, Restaurant_price,
         Restaurant_rating) in cursor1:

        count += 1
        if len(global_dict) > 5:
            break
        #print("in location for loop")
        if Restaurant_id not in global_dict:
            global_dict[int(Restaurant_id)] = [str(Restaurant_name), str(Restaurant_address), str(Restaurant_cuisine),
                                               str(Restaurant_price), str(Restaurant_rating)]
        # print(Restaurant_name+","+Restaurant_address+","+Restaurant_cuisine)
    '''if count == 0:
        restaurant_dict = no_result_query(cursor1)'''
    # cnx.close()
    #print("in address")
    return global_dict


# result = search_restaurant_by_cuisine(cuisine)
# result = search_restaurant(address,cuisine,price)
# result = search_restaurant_by_price(price)
# result = search_restaurant_by_price_cuisine(price,cuisine)
# result = search_restaurant_by_address(address)
# print(result)
def call_trade_off(address, cuisine, price):
    global ub
    global lb
    global_dict = {}
    if price == "cheap":
        lb = 0
        ub = 13
    if price == "medium":
        lb = 14
        ub = 22
    if price == "costly":
        lb = 23
        ub = 50

    cnx1 = pymysql.connect(user='root', password='fdsfjhgj', #dummy password
                           host='127.0.0.1',
                           database='Saif_Test')
    global_dict = search_restaurant_by_price(price, cnx1,global_dict)
    global_dict = search_restaurant_by_cuisine(cuisine, cnx1,global_dict)
    global_dict = search_restaurant_by_address(address, cnx1,global_dict)

    return global_dict

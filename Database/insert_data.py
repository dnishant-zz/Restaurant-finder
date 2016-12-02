import pymysql
import csv

cnx = pymysql.connect(user='root', password='hidden', #used dummy password
                              host='127.0.0.1',
                              database='Saif_Test')


def insert_data_to_database():
    cur = cnx.cursor()
    with open("Restaurants.csv", 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            name = "'"+row[0]+"'"
            address = "'"+row[1]+"'"
            cuisine = "'"+row[2]+"'"
            price = "'"+row[3]+"'"
            rating = "'"+row[4]+"'"
            query = "insert into Restaurant(Restaurant_name,Restaurant_address,Restaurant_cuisine,Restaurant_price,Restaurant_rating) values("+name+","+address+","+cuisine+","+price+","+rating+")"
            cur.execute(query)

    cur.close()
    cnx.close()

insert_data_to_database()



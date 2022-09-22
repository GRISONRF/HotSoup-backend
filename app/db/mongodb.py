from pymongo import MongoClient
# import pandas as pd
# import numpy as np
import logging

logging.basicConfig(level=logging.DEBUG)

# Is this the file where we create the endpoint implementation?

def init_mongo():
    """
    #Creates a connection to our local mongoDB and returns the following:

    Returns: 
        client: A Pymongo client (lowest level object of MongoDB connection)
        hot_soup_table: MongoDB Table
        kitchen_collection: MongoDB collection inside hot_soup_table.
        user_collection: MongoDB collection inside hot_soup_table

    """
    try:
        client = MongoClient('mongodb://admin:HotSoup4321!@database:27017/hot_soup_local_db?authSource=admin')
        hot_soup_table = client['hot_soup_table']   #creates a db table called hot_soup_table
        kitchen_collection = hot_soup_table['kitchens'] #references to the table - creating a collection called 'kitchens'
        user_collection = hot_soup_table['user'] #references to the table - creating a collection called 'user'
        return client, hot_soup_table, kitchen_collection, user_collection
    except:
        logging.error("Client to MongoDB unavailable.  Please check your environment variables.")
    
#Client for connection to MongoDB
mongo_client, mongo_table, kitchen_collection, user_collectior = init_mongo()


#Sample Kitchen example /// 
sample_kitchen = {"Name":"Scott's Kitchen",
 "Address": {
     "street_name":"Fake Street",
     "street_number": "123",
     "city":"Chicago",
     "state":"Illinois",
     "zip_code":"60127"
 },
 "Comment":"Friendly Staff and Great Food",
 "Phone":"1-123-555-4321",
 "Hours":
 {"Monday": {"start": 700, "end": 1500},
  "Tuesday":{"start": 900, "end": 1200},
  "Wednesday":{"start": 600, "end":1500}
 }
}


#inserting above sample_kitchen into the kitchen_collection /// That's what is going to create the tables!!
kitchen_collection.insert_one(sample_kitchen)


#This is printing out all the values inside the kitchen_collection // passing an empty document, so there is "no filter" which means everything is printed since everything is a doc.
print(list(kitchen_collection.find({})))

class MongoDBController:
    def get_kitchens(self):
        return list(kitchen_collection.find({}))

# to print this as a 'readable' list and not as an object, we need to iterate through the kitchen_collection and print each of the values 

#How to delete via the name key and outputs the deleted value.
#NOTE:  Since it is .delete_one it should always be one!
# kitchen_collection.delete_one({'Name':"Scott's Kitchen"}).deleted_count 


# create functions to add / modify / do things with our database
'''
function to define what we have to pass to kitchen to add it into the database // when we are dealing with real data
eg: 

def add_kitchen(name, address, comment, phone, hours):
    document = {
        'name': name
        'address': address,
        'comment': comment,
        'phone': phone,
        'hours': hours,
        'date added' : datetime.datetime.now()  -> to add what time we added this entry to the db #DO WE NEED THIS?!
    }
    return cars.insert_one(document)   #what collection do we want to add this into // will return an object that tells us about the status of what we just inserted


# kitchen = add_kitchen(...)
# kitchen.inserted_id 
# ---> this will return the id of that document



def add_user(value):
    same thing...
    document = {
        'Key': value
    }
    return user.insert_one(document)


if I want to create a relationship bewtween the 2 functions:

def add_user_fav_kitchen(kitchen_id, user_id):
    document = {
        'car id': car_id,
        'user_id': user_id
    }
    return user_fav_kitchen.insert_one(document)


--> to add a kitchen and a user to make sure everything is working:
kitchen = add_kitchen('Scott's Kitchen', 'Fake Street', 'Friendly Staff and Great Food', 1-555-222-3333)
user = add_user('value')
user_fav = add_user_fav(kitchen.inserted_id, user.inserted_id)

---> to filter information:
about the kitchen: 
kitchen.find({'address': '123 street'}) -> will get all the kitchens at this address

---> to delete information:
result = kitchen.delete_one({'address': 456 street}) -> will delete the first one its find. .delete_many to delete everything that fits the values.-returns an object
retult.deleted_count -> tells you how many things were remove

---> to update information:
result = kitchen.update_many({'address': 456 street}, {'$set': {'address': '000 street}}) -> change the address to 000 street

'''




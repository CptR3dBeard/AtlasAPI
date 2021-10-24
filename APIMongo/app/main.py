#Author CptR3dBeard
"""Description:
These are the main functions that interact with MongoDB's Atlas.
These will be called from within the API.py file and used to submit/delete/return entries"""
#Imported Libraries
import os
import pymongo
import pandas as pd
from dotenv import load_dotenv

load_dotenv()                     # loading the local enviroment variables
client = pymongo.MongoClient(f"yourclusteraddress{os.getenv('user')}:{os.getenv('pass')}@yourclusteraddress", ssl=True)
db = client[os.getenv('db')]
col = db[os.getenv('collection')]


def upload_dict(value1, value2):  # defining the upload entry function
    d = {'Name':value1, 
    'Age': value2}                # d value to store Name/Age Data
    col.insert_one(d)             # insert values into mongoDB Collection
    return {'Upload Successful'}


def finding_value(value1):        # define a function to find entry within MongoDB
    return col.find_one({'Name': value1}, {'_id': 0})

def delete_entry(value1,value2):
    for x in col.find({'Name': value1,'Age': value2}, {'_id': 0}):  # for value1 in collection
        if True:                  # if true do this
            col.delete_one(x)     # delete that entry and call the menu function
        return {'Entry Deleted'}

def write_csv():                  # function to create local csv file
    x =col.find({}, {'_id': 0})   # variable containing pymongo find command aswell as removing the _id 
    for i in x:                   # iterating over x variable
        df = pd.DataFrame(x)      # setting dataframe variable for x
        df.reset_index(drop=True, inplace=True)     #resettinig the index and dropping it for smooth csv transition
        df.to_csv('out.csv')      # create csv file and save contents of x to it
        return {'CSV Download Successful'}  # return CSV download successful prompt
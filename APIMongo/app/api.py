#Author CptR3dBeard
#Description
"""This is a basic API to interact with my pymongo functions seen in "main.py"
the end goal is to allow the user to; Find an entry and return it, upload new entries, aswell as remove them.
"""
from main import *
from fastapi import FastAPI

app = FastAPI()             # define app for FastAPI


@app.get('/')               # get request of '/'
def index():
    return ['Connection Successful']    # return connection successful


@app.get('/find/{data}')    # find this entry
def find_an_entry(data):    # defining function to find entry
    return finding_value(data)    # calling finding value function from Core Functions with the entry var


@app.get('/add/{data}/{data2}')
def add_new_entry(data,data2):
    name = data             #set data to name variable
    age = data2             # set data2 to age variable
    return upload_dict(name,age) #call imported function to upload name and age var to Atlas

@app.get('/delete/{data}/{data2}')  # delete function
def delete_from_mongo(data,data2):
    return delete_entry(data,data2) # call and reutrn delete_entry function from main

@app.get('/download_csv')
def download_to_csv():      # function to call our other function
    return write_csv()      # calls the create csv function from main
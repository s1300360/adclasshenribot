# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 00:11:54 2018

@author: linzino
"""

from pymongo import MongoClient
import pymongo
import urllib.parse
from datetime import datetime 



# db setting
host = 'ds133252.mlab.com'
port = '33252'
username = urllib.parse.quote_plus('henri')
password = urllib.parse.quote_plus('Stock345')
# Authentication Database
Authdb='henribotdb'

def init_db():
    client = MongoClient('mongodb://%s:%s@%s:%s/%s?authMechanism=SCRAM-SHA-1'
                      % (username, password, host, port, Authdb))
    dbname='henribotdb'
    db = client[dbname]
    return db


def insert_one(dic,collection):
    #collection_name = 'users'
    db = init_db()
    coll = db[collection]
    coll.insert_one(dic)


def get_all(collection):
    db = init_db()
    coll = db[collection]
    return list(coll.find())

def find_user(userid,collection):
    '''
    確認這個使用者是不是加入了
    '''
    db = init_db()
    coll = db[collection]
    return len(list(coll.find({"userid":userid})))




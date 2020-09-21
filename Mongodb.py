# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 21:47:37 2020

@author: VK
"""

import pymongo

#Run below in cmd to get local ip and port and add protocol
## "C:\Program Files\MongoDB\Server\4.4\bin\mongo.exe" 
client = pymongo.MongoClient('mongodb://127.0.0.1:27017/')

mydb = client['Employee']

information = mydb.employeeinformation

record = [{
        'firtname':'John',
        'lastname':'Reed',
        'department':'Analytics'},{'firtname':'John1',
        'lastname':'Reed1',
        'department':'Analytics1'},{'firtname':'John2',
        'lastname':'Reed2',
        'department':'Analytics2'}]

information.insert_many(record)
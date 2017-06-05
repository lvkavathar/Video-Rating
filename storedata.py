#!/usr/bin/python

import mysql.connector 
import sys 
import json 
import os
import argparse

arg_parser = argparse.ArgumentParser("Store data in database")
arg_parser.add_argument("-f", "--filename", required=True, help="Filename to internalize")
args = arg_parser.parse_args()
data = open(args.filename, "rb")
csv_data = data.read()
csv_data = csv_data.strip()
words=csv_data.split(',')
print words
con = mysql.connector.connect(user='root',password='toor',host='127.0.0.1',database='hackYoutube')
cur = con.cursor() 
for word in words:
     word = word.replace(' ','')
     #try : 
     # word = unicode(word, "utf-8")
     #except Exception:
     # pass
     #print word
     arg = (word,)
     query = "INSERT INTO badWords VALUES (%s)"
     cur.execute(query,arg)
     con.commit()
cur.close()
con.close()


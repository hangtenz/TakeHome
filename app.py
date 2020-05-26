import json
from flask import Flask,jsonify
from flask_restful import reqparse
from flask import request
import sqlite3


PORT = "5565"
HOST = "0.0.0.0"

app = Flask(__name__)
conn = sqlite3.connect('data.db')

c = conn.cursor()

#c.execute('''CREATE TABLE cards(name text, content text, status text, catagory text, author text)''')

#Add
@app.route("/cards",methods=['POST'])
def add():
    d = request.json
    name = d['name']
    content = d['content']
    status = d['status']
    catagory = d['catagory']
    author = d['author']
    print(name,content,status,catagory,author)
    query = "INSERT INTO cards VALUES ('"+name+"','"+content+"','"+status+"','"+catagory+"','"+author+"')"
    print(query)
    with sqlite3.connect("data.db") as conn:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    return jsonify({"message":"OK"}) ,200
        
#Edit
@app.route("/cards",methods=['PUT'])
def update():
    d = request.json
    name = d['name']
    content = d['content']
    status = d['status']
    catagory = d['catagory']
    author = d['author']
    print(name,content,status,catagory,author)
    query = "UPDATE cards SET name='"+name+"',content='"+content+"',status='"+status+"',catagory='"+catagory+"' WHERE author = '"+author+"'"
    with sqlite3.connect("data.db") as conn:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    return jsonify({"author":author}) ,201
        

#Delete
@app.route("/cards",methods=['DELETE'])
def delete():
    d = request.json
    author = d['author']
    query = "DELETE FROM cards WHERE author='"+author+"'"
    print(query)
    with sqlite3.connect("data.db") as conn:
        c = conn.cursor()
        c.execute(query)
        conn.commit()
    return jsonify({"author":author}) ,202


#Get
@app.route("/cards",methods=['GET'])
def getAll():
    cards = []
    query = "SELECT * from cards"
    with sqlite3.connect("data.db") as conn:
        c = conn.cursor()
        for card in c.execute(query):
            cards.append(card)
        conn.commit()
    return jsonify({"allCards":cards}) ,200

app.run(host=HOST,port=PORT)
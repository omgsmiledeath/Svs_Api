#!flask/bin/python
import sqlite3
import json
from flask import Flask, abort,jsonify,make_response,request  #Импорт методов из библиотеки Flask


app = Flask(__name__)  #Создаем само приложение


@app.route('/api/v1/login',methods=['POST'])
def login():
    token = request.get_json()
    print(token)
    return jsonify({"token":'1'})


@app.route('/api/v1/entries',methods=['GET']) #Ставим Endpoint для GET
def get_entries():
    try:
        cur = sqlite3.connect("./app/app.db").cursor()

        resSql = cur.execute("SELECT * FROM ENTRY")
        res = resSql.fetchall()
        print(res)
        response = make_response(
            jsonify(
                res),
                200,
                )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        return ex.__str__()

@app.route('/api/v1/newentry',methods=['POST'])
def add_entries():
    if not request.json:
        abort(400)
    try:
        temp = request.get_json()
        print(temp['date'])
        date = temp['date']
        status = temp['status']
        owner = temp['owner']
        desc = temp['desc']
        con = sqlite3.connect("./app/app.db")
        cur = con.cursor()
        con.execute("""INSERT INTO entry (date,status,owner,desc) 
                    VALUES (?,?,?,?)""",(date,status,owner,desc))
        con.commit()
        resSql = cur.execute("SELECT * FROM ENTRY")
        res = resSql.fetchall()
        print(res)
        response = make_response(
            jsonify(
                res),
                201,
                )
        return response
    except Exception as ex:
        return ex.__str__()
    

if __name__== '__main__':
    app.run(debug=True,port=3000)


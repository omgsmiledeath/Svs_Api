#!flask/bin/python
import sqlite3
import json
from flask import Flask,jsonify,make_response,request  #Импорт методов из библиотеки Flask


app = Flask(__name__)  #Создаем само приложение


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
        temp = json.loads(request.json)
        print(temp) 
        con = sqlite3.connect("./app/app.db")
        cur = con.cursor()
        resSql = cur.execute("SELECT * FROM ENTRY")
        res = resSql.fetchall()
        print(res)
        response = make_response(
            jsonify(
                res),
                201,
                )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        return ex.__str__()
if __name__== '__main__':
    app.run()


#!flask/bin/python
import sqlite3
from flask import Flask,jsonify,make_response  #Импорт методов из библиотеки Flask


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

if __name__== '__main__':
    app.run()


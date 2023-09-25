#!flask/bin/python
import sqlite3
import json
from flask_cors import CORS,cross_origin
from flask import Flask,redirect,url_for,abort,jsonify,make_response,request  #Импорт методов из библиотеки Flask

dbpath = "./app/app.db"
app = Flask(__name__)  #Создаем само приложение
cors = CORS(app)
app.config['CORS_HEADERS']='Content-Type'


#POST на получение токена , доделать!!!!!!!!!!!!!
@app.route('/api/v1/login',methods=['POST'])
@cross_origin()
def login():
    token = request.get_json()
    print(token)
    cur = sqlite3.connect("./app/app.db").cursor()
    resSql = cur.execute("SELECT * FROM ENTRY")
    res = resSql.fetchall()
    return jsonify(res),201

@app.route('/api/v1/posts',methods=['GET']) #Ставим Endpoint для GET
def get_posts():
    try:
        cur = sqlite3.connect("./app/app.db").cursor()

        resSql = cur.execute("SELECT * FROM POST")
        res = resSql.fetchall()
        listToJson = []
        for el in res:
            listToJson.append({"id":el[0],"titul":el[1],"postText":el[2],"videoUrl":el[3],
                               "createData":el[4],"updateData":el[5],"user":el[6]})
        print(listToJson)
        response = make_response(
            jsonify(
                listToJson),
                200,
                )
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response
    except Exception as ex:
        return ex.__str__()
    
#GET на плучение всех записей
@app.route('/api/v1/entries',methods=['GET']) #Ставим Endpoint для GET
def get_entries():
    try:
        day = request.args.get('day')
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
#POST запрос с добавлеием новой записи
@app.route('/api/v1/newentry',methods=['POST'])
def add_entries():
    if not request.json:
        abort(400)
    try:
        temp = request.get_json()
        isExist = False
        print('ENTRIES ________________')
        print(temp['entries'])  
        if not temp['entries']:
            abort(400)
        con = sqlite3.connect("./app/app.db")
        cur = con.cursor()
        for el in temp['entries'] :
            date = el["date"]
            exist = cur.execute("""SELECT * FROM entry WHERE date = (?)
                                """,(date,)).fetchone()
            if (exist is None) or (len(exist)==0):
                status = el["status"]
                owner = el["owner"]
                desc = el["desc"]
                con.execute("""INSERT INTO entry (date,status,owner,desc) 
                        VALUES (?,?,?,?)""",(date,status,owner,desc))
            else :
                isExist==True
        resCode = 201        
        if isExist==False :
            con.commit()
        else:
            resCode = 409    
        resSql = cur.execute("SELECT * FROM ENTRY")
        res = resSql.fetchall()
        return jsonify(res),resCode
    except Exception as ex:
        return ex.__str__()
#PUT запрос на обновление    
@app.route('/api/v1/entries/<int:id>',methods=['PUT'])
def update_entry(id):
    json_req = request.get_json()
    con = sqlite3.connect(dbpath)
    cur = con.cursor()
    print(json_req)
    for el in json_req['entry']:
        cur.execute("UPDATE entry SET date=?,status=?,owner=?,desc=? WHERE id=?",
                      (el["date"],el["status"],el["owner"],el["desc"],id))
    con.commit()
    return jsonify()

if __name__== '__main__':
    app.run(debug=True)



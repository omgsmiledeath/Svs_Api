#!flask/bin/python

from flask import Flask,jsonify,make_response  #Импорт методов из библиотеки Flask


app = Flask(__name__)  #Создаем само приложение



@app.route('/api/v1/entries',methods=['GET']) #Ставим Endpoint для GET
def get_entries():
    response = make_response(
        jsonify(
            {"id":1,"name":"name1"}),
            200,
            )
    return response

if __name__== '__main__':
    app.run()


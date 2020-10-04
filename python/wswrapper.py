from flask import Flask, jsonify, request
import similaritysearch
import json

app = Flask(__name__)

@app.route("/")
def default():
    return "Hello world>>!!"

@app.route('/userquery',methods=['GET'])
def userquery():
    query = request.args.get('query', None) #user query
    categoriesjson = request.args.get('categoriesjson', None) #query categories as json for getting multiple categories
    print ("User Query :" + query)
   # print(categoriesjson)
    categorieslist = json.loads(categoriesjson)
    print ("categorieslist :" , categorieslist[0]['Custom User Query'])
    categories = list()
    for category in categorieslist:
        categories.append(category['Custom User Query'])

    response = similaritysearch.queryresponse(query, categories)
    return jsonify(response)

if __name__ == "__main__":
    app.run()

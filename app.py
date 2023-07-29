from flask import Flask,request,jsonify
import json


app=Flask(__name__) #name of module is main

#create url
@app.route('/')
def welcome():
    return "welocme to flask"  #we can html 

@app.route('/calculator',methods=["GET"])
def math_operation():
    # we are getting this njmber in the post man or html
    operation=request.json["operation"]  #postman #html ---->flask (app-server)
    number1=request.json["number1"]
    number2= request.json["number2"]

    if operation=="add":
        result=int(number1)+int(number2)
    elif operation =="mul":
        result=int(number1)*int(number2)
    elif operation =="div":
        result=int(number1)/int(number2)
    else:
        result=int(number1)-int(number2)

    return "the operation is {} and the result is {}".format(operation,result)     

print(__name__)
if __name__=='__main__':
    app.run()    # when we use this then only show sthe server number pupyth
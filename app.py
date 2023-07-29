from flask import Flask,request,render_template

app=Flask(__name__) #name of module is main

#create url
@app.route('/')
def welcome():
    return "welocme to flask"  #we can html 

@app.route('/calculator',method=['GET'])
def math_operation():
    # we are getting this njmber in the post man or html
    operation=request.json["operation"]  #postman #html ---->flask (app-server)
    number1=request.json["number1"]
    number2= request.json["number2"]

    if operation=="add":
        result=number1+number2
    elif operation =="mul":
        result=number1*number2
    elif operation =="div":
        result=number1/number2
    else:
        result=number1-number2  

    return result      

print(__name__)
if __name__=='__main__':
    app.run()    # when we use this then only show sthe server number pupyth
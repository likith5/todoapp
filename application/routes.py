from application import app
from flask import render_template,flash,request,redirect,url_for
from application import db
from datetime import datetime

from bson import ObjectId




@app.route("/")
def index():
    todos=[]
    for todo in db.todos.find().sort("date_created",-1):
        todo["_id"] = str(todo["_id"])
        todo["date_created"] = todo["date_created"].strftime("%b %d %Y %H:%M%S")
        todos.append(todo)
    return render_template("view.html",todos=todos)

    

 

@app.route("/add_todo",methods=['POST','GET'])
def add_todo():
    if request.method == "POST":
        todo_item = request.form.get('add_todo')
        db.todos.insert_one({
            'text':todo_item,
            'complete':False,
            'date_created':datetime.utcnow()
        })
        return redirect("/")
    else:
        return render_template("added.html")

@app.route("/complete_todo/<id>")
def complete_todo(id):
    
    todo_item = db.todos.find_one({
        '_id':ObjectId(id)
        })
    db.todos.save( { complete: True } )
    return redirect("/")


@app.route("/delete_todo/<id>")
def delete_todo(id):
    db.todos.find_one_and_delete({"_id":ObjectId(id)})
    return redirect("/")

@app.route("/update_todo/<id>",methods = ["POST","GET"])

def update_todo(id):
    if request.method == "POST":
        todo_item = request.form.get('add_todo')
        

        db.todos.find_one_and_update({
            "_id":ObjectId(id)
            },{"$set":{
            "text":todo_item,
            'complete':False,
            'date_created':datetime.utcnow()
            }})
        
        
        return redirect("/")
        
    else:
        todo_item = request.form.get('add_todo')
        todo=db.todos.find_one({"_id":ObjectId(id)})

         
    return render_template("added.html",todo_item=todo_item)

@app.route("/deleteall_todo")
def deleteall_todo():
    db.todos.delete_many({})
    return redirect("/")
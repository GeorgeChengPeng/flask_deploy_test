from flask import render_template,redirect,request
from models import Dojo,Ninja
from config import db

def root():
    list_of_dojos = Dojo.query.all()
    # print(list_of_dojos)
    # print(len(list_of_dojos))
    list_of_student = Ninja.query.filter_by(student_id = 1).all()
    # print(list_of_student)

    return render_template("index.html",list_of_dojos = list_of_dojos)
def dojo():
    new_a_dojo = Dojo(name = request.form["dojo_name"],city = request.form["dojo_city"],state = request.form["dojo_state"])
    db.session.add(new_a_dojo)
    db.session.commit()
    return redirect("/")

def ninja():
    new_a_ninja = Ninja(first_name = request.form["first_name"],last_name = request.form["last_name"], student_id = request.form["dojo_option"])
    db.session.add(new_a_ninja)
    db.session.commit()
    return redirect("/")
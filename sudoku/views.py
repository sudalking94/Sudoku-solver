import os 
from flask import send_from_directory    
from flask import Blueprint, render_template


views = Blueprint("views", __name__)


@views.route("/")
@views.route("/index")
def index():
    array = []
    for x in range(3):
        row = [1,2,3,4,5,6,7,8,9]        
        if x == 0:
            array.append(row[:3])
        elif x == 1:
            array.append(row[3:6])
        elif x == 2:
            array.append(row[6:])             
    return render_template("index.html", array=array)

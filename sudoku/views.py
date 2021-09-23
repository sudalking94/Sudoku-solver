from flask import Blueprint, render_template, request,jsonify
from .solver import backtrackingAlgorithm

views = Blueprint("views", __name__)

def arrayGenerator():
    array = []
    for x in range(3):
        row = [1,2,3,4,5,6,7,8,9]        
        if x == 0:
            array.append(row[:3])
        elif x == 1:
            array.append(row[3:6])
        elif x == 2:
            array.append(row[6:])
    return array


@views.route("/")
def index():       
    return render_template("index.html", array=arrayGenerator())


@views.route("/result", methods=['POST'])
def result():
    if request.method == "POST":                
        jsonData = request.get_json()                   
        board = backtrackingAlgorithm(jsonData)
    return jsonify({"board":board})

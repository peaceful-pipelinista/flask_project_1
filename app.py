from flask import Flask, jsonify, render_template
import json
from flask import request
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

@app.route('/api')
def api():
    with open('data.json', 'r') as file:
        data = json.load(file)
    return jsonify(data)

MONGO_URI = os.getenv("MONGO_URI")
client = pymongo.MongoClient(MONGO_URI)
db = client["flask_project_1"]
collection = db["to_do_list"]

@app.route("/todo")
def todo_page():
    return render_template("todo.html")

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    collection.insert_one({
        "itemName": item_name,
        "itemDescription": item_description
    })

    return "Item stored successfully"


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Configure MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client.poke_db
counter_collection = db.counter

# Initialize the counter if it doesn't exist
if counter_collection.count_documents({}) == 0:
    counter_collection.insert_one({"count": 0})

@app.route('/poke', methods=['GET'])
def poke():
    # Increment the counter
    counter_collection.update_one({}, {'$inc': {'count': 1}})
    
    # Get the current count
    count_doc = counter_collection.find_one()
    count = count_doc['count']
    
    return f'The poke endpoint has been accessed {count} times.'

@app.route('/home', methods=['GET'])
def home():
    # Get the current count
    count_doc = counter_collection.find_one()
    count = count_doc['count']
    
    return render_template('home.html', count=count)

if __name__ == '__main__':
    app.run(debug=True, host="localhost", port=5000)
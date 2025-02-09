# Python script to extract specific key-value pairs from the configuration file 
# in a data structure save the output file data as JSON data in the database.
# Once Data is inserted run the endpoint which will display all inserted config data

import os
import configparser
from flask import Flask, jsonify
from pymongo import MongoClient

# Declaring Flask App
app = Flask(__name__)

'''Read .env file and get the mongo db cluster URL stored as follows:
PASSWORD=mongodb+srv://youmongodbidhere:yourmongodbpasswordhere@cluster0.aq7nu.mongodb.net/
in a .env file in the ASSIGNMENT_01_DEVOPS folder cloned using git'''
env_path = os.path.join(os.path.dirname(__file__), "../.env")

MONGO_URI = None
if os.path.exists(env_path):
    with open(env_path, "r") as file:
        for line in file:
            key, value = line.strip().split("=", 1)
            if key == "PASSWORD":
                MONGO_URI = value.strip('"')  # Strip quotes if present
                break

# MongoDB Connection Database Name
DATABASE_NAME = "devops"
# MongoDB Connection Collection Name
COLLECTION_NAME = "assignment_one"

# Check if Url obtained is not empty and assign them to variables
if MONGO_URI is not None:
    client = MongoClient(MONGO_URI)
    db = client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
 
# Read configuration file
config_file = "config_file.txt"
config_data = {}

# if the file and path exists proceed
if os.path.exists(config_file):
    config = configparser.ConfigParser()
    # reading the file
    config.read(config_file)

    # loop over each section and create json
    for section in config.sections():
        config_data[section] = dict(config.items(section))

    # Find highest existing id and increment by 1
    if collection is not None and collection.count_documents({}) > 0:
        highest_record = collection.find_one({}, sort=[("id", -1)])
        new_id = highest_record["id"] + 1 if highest_record and "id" in highest_record else 1
    else:
        new_id = 1
    # insert the configuration data once per run of this script
    collection.insert_one({"id": new_id, "config_data": config_data})
    print(f"Configuration data inserted into MongoDB with id {new_id}.")
else:
    print("Configuration file not found!")
    print("New Record Not Inserted!")

@app.route('/get_all_config_data', methods=['GET'])
def get_config():
    #Fetch the list of configuration data from MongoDB
    if collection is not None:
        # Get all records
        result = list(collection.find({}, {"_id": 0}))
        return jsonify(result if result else {"message": "No data found."})
    return jsonify({"error": "Database connection failed!"})
    
if __name__ == '__main__':
    # debug = False to avoid reload of the script and single insertion of configuration data
    app.run(debug=False)
from flask import Flask
from flask_cors import CORS
import re

import json
import ast
from swarms import Swarms

app = Flask(__name__)
CORS(app)

api_key = "your_api_key_here"  # Replace with your actual API key
swarm = Swarms(api_key=api_key)

db = json.load(open('db.json','r'))
print("INITIAL DB STATE")
print(db['todo_list']["state"])

@app.route('/<app_name>/<api_call>')
def api(app_name, api_call):
    db = json.load(open('db.json','r'))
    print("INPUT DB STATE")
    print(db[app_name]["state"])

    objective = f"""{db[app_name]["prompt"]}
    API Call (indexes are zero-indexed):
    {api_call}

    Database State:
    {db[app_name]["state"]}

    Output the API response as json prefixed with '!API response!:'. Then output the new database state as json, prefixed with '!New Database State!:'. If the API call is only requesting data, then don't change the database state, but base your 'API Response' off what's in the database.
    """

    response, new_state = swarm.run_swarms(objective)

    db[app_name]["state"] = new_state
    json.dump(db, open('db.json', 'w'), indent=4)
    return response

if __name__ == "__main__":
    app.run()

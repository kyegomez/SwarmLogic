from fastapi import FastAPI, HTTPException
from typing import Optional

import json
import logging
from pydantic import BaseModel
from swarms import Worker

class AppState(BaseModel):
    app_name: str
    api_call: str

# Set up logging
logging.basicConfig(filename="app.log", level=logging.INFO, format='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# Initialize workers with your API key
api_key = "your-api-key-here"
worker = worker_node(openai_api_key=api_key)

app = FastAPI()

@app.post("/{app_name}/{api_call}")
async def api(app_state: AppState):
    try:
        db = json.load(open('db.json', 'r'))
    except Exception as e:
        logging.error("Error loading database: %s", e)
        raise HTTPException(status_code=500, detail="Error loading database")

    prompt = f"""{db[app_state.app_name]["prompt"]}
    API Call (indexes are zero-indexed):
    {app_state.api_call}

    Database State:
    {db[app_state.app_name]["state"]}

    Output the API response as json prefixed with '!API response!:'. Then output the new database state as json, prefixed with '!New Database State!:'. If the API call is only requesting data, then don't change the database state, but base your 'API Response' off what's in the database.
    """

    try:
        # Update to call the worker model
        response = worker.run(prompt)
        new_state = response['new_database_state']
        
        if new_state:
            db[app_state.app_name]["state"] = new_state
            json.dump(db, open('db.json', 'w'), indent=4)
    except Exception as e:
        logging.error("Error running model or updating state: %s", e)
        raise HTTPException(status_code=500, detail="Error running model or updating state")
        
    return response

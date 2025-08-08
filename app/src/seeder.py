#!/usr/bin/python

import configparser
import os
import random
import time
import uuid
import requests


def should_execute():
    return random.choice([True, False])


config = configparser.ConfigParser()

# Build path relative to the script's directory
config_path = os.path.join(os.path.dirname(__file__), 'config/config.ini')
config.read(config_path)

print("Sections found:", config.sections())

flask_server_url = config['flask-server']['url']
max_executions = config.getint('flask-server', 'max_executions')
print(f"Flask App Server Url: {flask_server_url} Max Executions: {max_executions}")

for i in range(max_executions):
    create_person_response = requests.post(f"{flask_server_url}/people")
    print(f"Create person http status {create_person_response.status_code}")
    person_id = create_person_response.json().get('id')
    get_person_response = requests.get(f"{flask_server_url}/people/{person_id}")
    print(f"Get person http status {get_person_response.status_code}")
    print(f"Get person response body {get_person_response.json()}")

    if should_execute():
        id = str(uuid.uuid4())  # Generate a random UUID
        get_person_response = requests.get(f"{flask_server_url}/people/{id}")
        print(f"Get person http status {get_person_response.status_code}")
        print(f"Get person response body {get_person_response.json()}")

    time.sleep(random.random()) # sleep between 0 and 1 second


#!/usr/bin/python

from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import uuid

app = Flask(__name__)
metrics = PrometheusMetrics(app)

metrics.info('app_info', 'Application info', version='1.0.3')

datasource = {}


@app.route('/health', methods=['GET']) 
def get_health_check():
    health_check = {"status": "UP"}
    json_response = jsonify(health_check)
    return json_response


@app.route('/people/<id>', methods=['GET'])
def get_person(id):
    person = datasource.get(id)
    if not person:
        return jsonify({"error": "Person not found"}), 404
    return jsonify(person)


@app.route('/people', methods=['POST']) 
def create_person_api():
    person = create_person()
    datasource[str(person['id'])] = person
    json_response = jsonify(person)
    return json_response


def create_person():
    response = {
        "id": uuid.uuid4(),
        "name": "John Doe",
    }
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

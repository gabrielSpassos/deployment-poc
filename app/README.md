# Flask APP

* Install deps 
```bash
pip3 install -r requirements.txt
```

* Unit test
```bash
python3 -m unittest -v app/test/test_server.py
```

* It test + Unit tests
```bash
pytest app/test
```

* Run server
```bash
python3 -m flask --app src/server.py run
```

* Run seeder
```bash
python3 src/seeder.py
```

* Create person
```bash
curl --location --request POST 'http://localhost:5000/people'
```

* Get person by id
```bash
curl --location 'http://localhost:5000/people/{{id}}'
```

* Get prometheus metrics
```bash
curl --location 'http://localhost:5000/metrics'
```

* Build docker image
```bash
docker build -t person-app .
```

* Run container
```bash
docker run -d -p 5000:5000 --name person-app-container person-app
```

# DatAI

**Setting Up Locally**

1. Create a **.env** file in the project root directory with the following environment variables
```
OPENAI_API_KEY=openai_api_key_local
DATAI_API_KEY=datai_api_key_local
MYSQL_DATABASE=db
MYSQL_USER=user
MYSQL_PASSWORD=password
MYSQL_ROOT_PASSWORD=password
```

2. To launch the service and the local test database
```bash
$ docker-compose up
```

3. Ensure there is some data in the database before testing. If there is no, add it


**Making API Requests**

***Search Endpoint***: Use the following curl request example for the /search endpoint:
```bash
$ curl -X 'POST' \
  'http://0.0.0.0:8000/api/v1/search/' \
  -H 'accept: application/json' \
  -H 'Authorization: Basic datai_api_key' \
  -H 'Content-Type: application/json' \
  -d '{
  "db_config": {
    "user": "user",
    "password": "password",
    "host": "db",
    "port": 3306,
    "db": "db"
  },
  "db_query_tables": ["loans", "clients", "branches", "pledges"],
  "search_query": "Какой не закрытый большой займ есть"
}'
```

**Swagger API Documentation**

You can also explore the Swagger API documentation locally by visiting:
* http://0.0.0.0:8000/docs

Have fun! 🚀

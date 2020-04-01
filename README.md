# how to run
## create a .env file in root directory adding these values
```
REDIS_SERVER=redis-server
REDIS_PASS=pass123
DB_HOST=psql-db
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=pass123
DB_NAME=fadb
```
## Database initialization is pefrormed with the ``psql_dump`` file.

## run the docker compose
``docker-compose up --build``

# Run in http using 
```
nginx:
    image: nginx:latest
    volumes:
      - ./nginx.http.config:/etc/nginx/nginx.conf
```
or using https, but first you have to create or obtain your own certificates and put on the directory certs with names ``server.crt`` and ``server.key``

```
nginx:
    image: nginx:latest
    volumes:
      - ./nginx.https.config:/etc/nginx/nginx.conf
      - ./certs:/etc/nginx/certs
```
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

# K8S

## create a self signed certificate with your domain (e.g. tsadimas.eu)
```
openssl req -x509 -newkey rsa:4096 -keyout server.key -out server.crt -days 365 --nodes -subj '/C=GR/O=fidemporiki/OU=it/CN=tsadimas.eu'i
openssl x509 -in server.crt -out server-crt.pem -outform PEM
openssl rsa -in server.key -out server-key.pem -outform PEM
 ```
## create a tls secret
```
kubectl create secret tls tls-secret --cert server-crt.pem --key server-key.pem
```
### apply the specific ingress with tls
```
kubectl apply -f k8s/fastapi-ingress-ssl.yaml
```
NOTE: because it is self signed certificate add the following to /etc/hosts
```
127.0.0.1 tsadimas.eu
```

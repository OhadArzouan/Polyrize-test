#SERVERLESS

##Run serverless normalizer
###Prerequisites:
* npm install
* npm install --save-dev serverless-wsgi serverless-python-requirements

##Start the server:
In order to start the process locally please run:

`sls offline start`

#API requests examples:
####API route:
`http://localhost:3000/master/api/v1/`
####Supported methods:
POST
####Supported endpoint:
`norm`
####Supported params:
input json to normalize must be sent in the request body.

Request example:

```
curl -X POST -H "Content-Type: application/json" -d '[ { "name": "device", "strVal": "iPhone", "metadata": "not interesting" }, { "name": "isAuthorized", "boolVal": "false", "lastSeen": "not interesting" }, { "name": "isAuthorized", "boolVal": "true", "lastSeen": "not interesting" }]' http://localhost:3000/master/api/v1/norm
```

Example response:

```
{'device': 'iPhone', 'isAuthorized': 'true'}
```
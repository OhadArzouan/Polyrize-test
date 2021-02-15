# normalizer
A server that find normalizes a json input and returns a json with all the names from the input and their corresponding values.


###Prerequisites
Install:
Python 3.6 and up
Run:
`pip install requirements.txt` (or pip3 - depending on your configuration)
 
###How to run
1. Make sure that port 8000 is vacant
2. Run the following command in order to authenticate using the `auth` endpoint
`curl -X POST -H "Content-Type: application/json" -d '{"username": "admin", "password": "aa1234"}' http://localhost:8000/auth`
You can change the credentials by changing the value in my_auth.json

3. Use the token created in step 2 as the Bearer in the header and send a POST request to out endpoint (Our route is: `/api/v1`, endpoint: `/norm`)

##Supported endpoint and examples:
####norm
The `norm` endpoint allows you to send a json list and get its normalized json in the responce.

Parameters:
* the json to normalized is to be sent in the body of the POST request to the endpoint. 

Return:
* json with all the names from the input and their corresponding values

 
e.g.

`curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjpudWxsLCJleHAiOjE2MTMzNDIwMzB9.IFTOxoIv3U3MpaLwnMk38GPjBk8IloKzHYV5SdbjoPI" -d '[ { "name": "device", "strVal": "iPhone", "metadata": "not interesting" }, { "name": "isAuthorized", "boolVal": "false", "lastSeen": "not interesting" }, { "name": "isAuthorized", "boolVal": "true", "lastSeen": "not interesting" }]' http://localhost:8000/api/v1/norm`

```
{"device":"iPhone","isAuthorized":"true"}
``` 
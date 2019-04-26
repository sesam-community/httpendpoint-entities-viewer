# Http endpoint entities viewer
Microservice to expose the json output from an http endpoint pipe.

WARNING: BE SURE THAT YOU KNOW WHAT YOU ARE DOING IF USING THIS MICROSERVICE.

[![Build Status](https://travis-ci.org/sesam-community/httpendpoint-entities-viewer.svg?branch=master)](https://travis-ci.org/sesam-community/httpendpoint-entities-viewer)

system setup
```json
{
  "_id": "http-endpoint-output-viewer",
  "type": "system:microservice",
  "docker": {
    "environment": {
      "SESAM_API_URL": "$ENV(sesam-api-url)"
    },
    "image": "sesamcommunity/httpendpoint-entities-viewer:latest",
    "port": 5001
  }
}
```

environment variables
```
SESAM_API_URL: the url to the api endpoint of the node
SECRET_KEY: secret key to use as cryptographic key for flask (to prevent CSRF attacks)
```

node configuration
```
1. Configure the microservice system with the above config.
2. Create a role for the requirement.
3. Give the role 'Endpoint read data' permission for the http endpoint pipes needed.
4. Create one or more jwt accordingly and assign the role created above to the jwt.
5. Give the created jwt to the users of the service.
6. Allow anonymous access to the microservice.
```

url to the http endpoint entities viewer
```
<node_url>:5001/<http_endpoint_name>

Replace <node_url> with the url of the node.
Replace <http_endpoint_name> with the name of the http endpoint pipe. 

Example: https://mynode.sesam.cloud:5001/data-http-endpoint
```

how to use the http endpoint entities viewer
```
1. Open the http endpoint entities viewer in a web broweser using the url pattern described above.
2. Submit a valid jwt.
3. If valid jwt, the microservice will return a json stream of the entities for the http endpoint.
```

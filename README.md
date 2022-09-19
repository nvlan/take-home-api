# take-home-api
A cool API to show off some skills

## What's in the repository

We have an API that exposes four endpoints:
- /health: a simple endpoint that responds with a 200 OK response for health check.
- /apiref: the API reference that explains each endpoint with examples.
- /words: this endpoint receives a word (only a-z and A-Z characters) and responds with said word but scrambled.
- /audit: this endpoint shows the last 10 API calls with the payload received.

## How do I use it?

There is a convenient Makefile that allows you to perform the following:
- make build: builds the app. This should be your first command.
- make run: starts the app with a fresh MariaDB database in foreground.
- make test: starts the app and executes all tests on the endpoints.
- make deploy: will deploy the app on an existing minikube installation.
- make teardown: removes the app and all resources from minikube.

## Tell me more about the app

This app was built using flask and uses a MariaDB container as a persistent storage. Each endpoint is a view registered with blueprint, and they each call to a service that handles the actual work. We have two decorators, one that is called on every API call and writes to the database (after sanitizing the input, we don't want any SQL injection) and a second one that checks if the request came with a basic auth header. All API endpoints have tests that check for all their possible answers. The API gets its configuration parameters from a class in the `config.py` file, located in the `/takehomeapi` directory. Currently, the configured values to use for the Basic auth header are `root:password`

## What about the deploy?

There is a docker compose file that starts the MariaDB and the app container locally (with make run). When you deploy to minikube, the database remains in the host (using a separate docker-compose file) instead of being a part of the POD. The idea behind this design is to simulate an off-deploy persistent database that would survive a k8s node going down. Also, for redundancy's sake the deploy creates two pods  with a dreplicaset and exposes both through nodeport service.

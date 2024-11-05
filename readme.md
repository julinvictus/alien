# ALIEN API

API with info about all Alien movies


This API was built with Python Flask, Docker and Postgres

---
## Fields

movie name: Official movie name

year: Year when the movie is set

spaceship name: Name of the spaceship where the movie is set

hero name: Name of the main character in the movie

hero actor name: Name of the actor's main character in the movie

synthetic name: Name of the robot (a.k.a synthetic) in the movie

planet name: Name of the planet where the movie is set

xenomorph name: Name of the xenomorph's specie (a.k.a alien) in the movie

release year: Year when the movie was released

director name: Name of the movie's director

---

## Endpoints

✅ create a movie

✅ get all movies

✅ get a movie by id

✅ update a movie

✅ delete a movie

---
App instrumented with Datadog APM
https://docs.datadoghq.com/tracing/

## Get started

`docker compose up -d flask_db`

(When needed to create for the first time)

`docker ps -a`

(Use this to see all containers running - and if used the above, to see if container was created)

`docker compose build`

(Builds the container)

`docker compose up flask_app datadog` OR `docker compose up --build flask_app datadog` (to rebuild img, every time code changes)



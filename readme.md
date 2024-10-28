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

## Get started

`docker compose up -d flask_db`

`docker ps -a`

`docker compose build`

`docker compose up flask_app` OR `docker compose up –builldflask_app` (to rebuild img, every time code changes)



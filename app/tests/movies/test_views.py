import json

import pytest

from movies.models import Movie

@pytest.mark.django_db
def test_add_movie(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    resp = client.post(
        "/api/movies/",
        {
            "title": "The Big Lebowski",
            "genre": "comedy",
            "year": "1998",
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["title"] == "The Big Lebowski"

    movies = Movie.objects.all()
    assert len(movies) == 1


@pytest.mark.django_db
def test_add_movie_invalid_json(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    response = client.post(
        path="/api/movies/",
        data={},
        content_type="application/json"
    )
    assert response.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_add_movie_invalid_jsom_keys(client):
    movies = Movie.objects.all()
    assert len(movies) == 0

    response = client.post(
        path="/api/movies/",
        data={"title": "Name",
              "year": 2000},
        content_type="application/json"
    )
    assert response.status_code == 400

    movies = Movie.objects.all()
    assert len(movies) == 0


@pytest.mark.django_db
def test_get_single_movie(client, add_movie):
    movie = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    response = client.get(
        path=f"/api/movies/{movie.id}/"
    )
    assert response.status_code == 200
    assert response.data["title"] == movie.title


@pytest.mark.django_db
def test_get_single_movie_incorrect_id(client):
    response = client.get(
        path=f"/api/movies/foo/"
    )
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_all_movies(client, add_movie):
    movie_one = add_movie(title="The Big Lebowski", genre="comedy", year="1998")
    movie_two = add_movie("No Country for Old Men", "thriller", "2007")
    response = client.get(path=f"/api/movies/")
    assert response.status_code == 200
    assert response.data[0]["title"] == movie_one.title
    assert response.data[1]["title"] == movie_two.title

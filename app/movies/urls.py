from django.urls import path

from . import views

urlpatterns = [
    path("api/movies/", views.MovieList.as_view()),
    path("api/movies/<int:pk>/", views.MovieDetail.as_view()),
]

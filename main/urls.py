from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("contact/", views.contact, name="contact"),
    # Below is what's known as a path variable, this allows you to get an individual id for say the project
    path("project/<int:id>/", views.project, name="project")
]


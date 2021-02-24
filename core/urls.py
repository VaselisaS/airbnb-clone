from django.urls import path
from rooms import views as views_rooms

urlpatterns = [
    path("", views_rooms.all_rooms, name="home"),
]

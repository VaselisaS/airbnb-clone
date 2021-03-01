from django.urls import path
from rooms import views as views_rooms

app_name = "core"
urlpatterns = [
    path("", views_rooms.HomeView.as_view(), name="home"),
]

from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("sign_up/", views.SingUpView.as_view(), name="sign_up"),
    path(
        "verify/<str:key>",
        views.complete_verification,
        name="complete_verification",
    ),
]

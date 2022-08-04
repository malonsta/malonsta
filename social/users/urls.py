from django.urls import path, include
from users.views import login_dashboard

app_name = "users"

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("login_dashboard/", login_dashboard, name="login_dashboard"),
]

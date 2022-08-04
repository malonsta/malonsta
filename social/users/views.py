from django.shortcuts import render


def login_dashboard(request):
    return render(request, "users/login_dashboard.html")

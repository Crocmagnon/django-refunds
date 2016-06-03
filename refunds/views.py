from django.shortcuts import render


def home(request):
    return render(request, "refunds/home.html")


def about(request):
    return render(request, "refunds/about.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages


def password_change_done(request):
    messages.success(request, "Mot de passe modifié avec succès")
    return render(request, 'refunds/home.html')

import random

from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "generator/home.html")


def generator(request):
    return render(request, "generator/generator.html")


def password(request):

    characters = list("abcdefghijklmnopqrstuvwxyz")

    if request.GET.get("uppercase"):
        characters.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    if request.GET.get("special"):
        characters.extend(list("""!"#$%&'()*+,-./:<=>?@[\]^_'{|}~"""))

    if request.GET.get("numbers"):
        characters.extend(list("1234567890"))

    length = int(request.GET.get("length"), 12)

    the_password = "".join(random.choice(characters) for _ in range(length))
    return render(
        request, "generator/password.html", {"password": the_password})

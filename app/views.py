from django.shortcuts import render


def base(request, name):
    return render(request, 'menu/home.html', {'name': name})

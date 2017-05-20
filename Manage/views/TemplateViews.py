from django.shortcuts import render

# Create your views here.


def manage_lights(request):
    return render(request, "Manage/Lights.html")


def manage_state(request):
    return render(request, "Manage/State.html")
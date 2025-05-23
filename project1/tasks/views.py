from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
tasks = {
    "sunday": "Plan the week ahead.",
    "monday": "Prepare for meetings.",
    "tuesday": "Grocery shopping.",
    "wednesday": "Workout session.",
    "thursday": "Clean the house.",
    "friday": "Family movie night.",
    "saturday": "Gardening and relaxation.",
}

def index(request):
    return render(request, 'index.html', {'days': tasks.keys()})

# def index(request):
#     return HttpResponse("Hi")


def day_view(request, day):
    task = tasks.get(day.lower(), "No task found for this day.")
    return render(request, 'day.html', {'day': day.capitalize(), 'task': task})
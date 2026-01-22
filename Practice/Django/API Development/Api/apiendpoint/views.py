from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def studentviews(request):
    students = {
        "id": 1,
        "name": "John", 
        "age": 32
    }
    return JsonResponse(students)
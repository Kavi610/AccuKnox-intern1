from django.shortcuts import render
from django.http import HttpResponse
from .models import employee
# Create your views here.
def create_instance(request):
    obj = employee.objects.create(name="Test")
    return HttpResponse("Instance created.")

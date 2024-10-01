from django.shortcuts import render
from .models import Student
# Create your views here.
def index(request):
    return render(request, "index.html")

def insertData(request):
    if request.method == "POST":
        name = request.POST.get("Name")
        email = request.POST.get("Email")
        query = Student(name = name, email = email)
        query.save()
        print(name, email)
    return render(request, "index.html")    
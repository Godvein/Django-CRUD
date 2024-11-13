from django.shortcuts import render,redirect
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
    return render(request, "index.html")    

def viewData(request):
    
    studentdata = Student.objects.all()
    data = {
        "studentdata" : studentdata
    }
    return render(request, "viewdata.html", data)

def updateData(request, id):
    if request.method == "POST":
        name = request.POST["Name"]
        email = request.POST["Email"]
        edit = Student.objects.get(id = id)
        edit.name = name
        edit.email = email
        edit.save()
        return redirect("/viewdata/")

    d = Student.objects.get(id = id)
    data = {
        "d" : d
    }
    return render(request, "updatedata.html", data)

def deleteData(request, id):
    d = Student.objects.get(id = id)
    d.delete()
    return redirect("/viewdata/")

from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import StudentSerializer
#api view
class ApiListViewCreate(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #custom delete all function
    def delete(self, request, *args, **kwargs):
        Student.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ApiRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = "pk"
    
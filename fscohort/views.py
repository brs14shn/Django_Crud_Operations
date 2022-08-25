from django.shortcuts import render,redirect
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,"fscohort/index.html")

def student_list(request):
   students=Student.objects.all()
   context={
    "student":students
   }
   return render(request,"fscohort/student_list.html",context)
#    return render(request,"fscohort/studen_list",{"student":students})

def student_add(request):
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successful")
            return redirect("list")
    context={
        "form":form
    }
    return render(request,"fscohort/student_add.html",context)

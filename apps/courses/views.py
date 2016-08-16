from django.shortcuts import render, HttpResponse, redirect
from .models import Course

def index(request):
    context = {
        "courses":Course.objects.all()
    }
    return render(request, 'courses/index.html', context)

def add(request):
    print(request.POST)
    Course.objects.create(name=request.POST["name"], description=request.POST["description"])
    return redirect('/')

def delete(request, course_id):
    print(request.POST)
    course = Course.objects.get(id=course_id)
    context = {
        "course": Course.objects.get(id=course_id)
    }
    return render(request, 'courses/destroy.html', context)

def destroy(request, course_id):
	course = Course.objects.get(id=course_id)
	course.delete()
	return redirect("/")

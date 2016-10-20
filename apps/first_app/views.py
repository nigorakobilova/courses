from django.shortcuts import render, redirect
from .models import Course, Description

# Create your views here.
def index(request):
    context={
        'courses': Course.objects.all(),
    }
    return render(request, 'first_app/index.html', context)

def courses(request):

    course = Course.objects.create(name=request.POST['fname'])

    Description.objects.create(description=request.POST['description'], course_id=course)

    return redirect('/')

def delete(request, id):
    context={
        'id': Course.objects.filter(id=id)
    }
    return render(request, 'first_app/delete.html', context)

def deleteCourse(request, id):
    course=Course.objects.get(id=id)
    course.delete()
    return redirect('/')

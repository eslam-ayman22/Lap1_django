from django.http import HttpResponse
from django.shortcuts import render

courses = [
    [1, 'Python', '30h'],
    [2, 'JavaScript', '20h'],
    [3, 'Html', '10h'],
    [4, 'Css', '15h']
]
# Create your views here.
def ListOfCourse(req):
    return render(req , 'course/list.html',context={'courses':courses})

def AddCourse(req):
    return HttpResponse('<h1>Add Trainee</h1>')


def UpdateCourse(req , id):
    course = next((t for t in courses if t[0] == id), None)

    if not course:
        return render(req, 'course/not_found.html')

    return render(req, 'course/updatecourse.html', {'course': course})


def DeleteCourse(req , id):
    return HttpResponse(f'<h1>delete Trainee {id}</h1>')


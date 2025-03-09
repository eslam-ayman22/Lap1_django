from django.http import HttpResponse
from django.shortcuts import render

trainees = [
    [1, 'eslam', 'engeslamayman@gmail.com'],
    [2, 'ali', 'ali9878@gmail.com'],
    [3, 'mohamed', 'mohamed43@gmail.com'],
    [4, 'ibrahim', 'mohamed77@gmail.com']
]
# Create your views here.
def ListOfTrainee(req):

    return render(req , 'trainee/list.html',context={'trainees':trainees})

def AddTrainee(req):
    return HttpResponse('<h1>Add Trainee</h1>')


def UpdateTrainee(req , id):
    trainee = next((t for t in trainees if t[0] == id), None)

    if not trainee:
        return render(req, 'trainee/not_found.html')

    return render(req, 'trainee/updatetrainee.html', {'trainee': trainee})


def DeleteTrainee(req , id):
    return HttpResponse(f'<h1>delete Trainee {id}</h1>')


def login(req):
    return render(req , 'trainee/login.html' ,context={'login':login})



def register(req):
    return render(req , 'trainee/register.html' ,context={'register':register})
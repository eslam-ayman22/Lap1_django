from django.http import HttpResponse
from django.shortcuts import render ,redirect
from .models import Trainee



# Create your views here.
def ListOfTrainee(req):
    context = {
        'trainees': Trainee.objects.filter(isactive=True)
    }
    return render(req, 'trainee/list.html', context)



def AddTrainee(req):
    if req.method == 'POST':
        (Trainee.objects.create
         (name=req.POST['trname'],
          email=req.POST['tremail'],
          img=req.FILES['trimg']))
        return redirect('ListOfTrainee')
    return render(req, 'trainee/addtrainee.html')





def UpdateTrainee(req , id):
    context = {'old':
                   Trainee.objects.get(trainee_id=id)}
    if (req.method == 'POST'):
        Trainee.objects.filter(trainee_id=id).update(
            name=req.POST['trname'],
            email=req.POST['tremail'],
            img=req.FILES['trimg']
        )
        return redirect('ListOfTrainee')

    return render(req, 'trainee/updatetrainee.html', context)

def DeleteTrainee(req , id):
    Trainee.objects.filter(trainee_id=id).update(isactive=False)
    return redirect('ListOfTrainee')




def login(req):
    return render(req , 'trainee/login.html' ,context={'login':login})


def register(req):
    return render(req , 'trainee/register.html' ,context={'register':register})
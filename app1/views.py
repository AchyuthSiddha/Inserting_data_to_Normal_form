from django.shortcuts import render

# Create your views here.
from app1.forms import *
from django.http import HttpResponse
def Display_student(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        STD=StudentForm(request.POST)
        # d1={'STD':STD}
        if STD.is_valid():
            return HttpResponse(str(STD.cleaned_data))
        else:
            return HttpResponse("not valid Data")
    return render(request,'Display_student.html',d)
from django.shortcuts import render
from demoapp.forms import RegisterData

# Create your views here.
def register(request):
    data1=RegisterData()
    return render(request,'registernew.html',{'form':data1})
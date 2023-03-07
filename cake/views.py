from django.shortcuts import render
from .models import DataDiscription
# Create your views here.
def index(request):
   dests= DataDiscription.objects.all()
   
   return render(request,'index.html',{'d1':dests})
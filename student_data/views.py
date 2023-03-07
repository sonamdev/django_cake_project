from django.shortcuts import render
from .models import Studentdata,Coursedata
# Create your views here.
def studentinfo(request):
    course1= Coursedata(course_id='C002',course_name='django',duration='30')
    course1.save()
    course=Coursedata.objects.get(course_id='C001')
    student1=Studentdata(sid='S002',name='rose',course=course)
    student1.save()
    print("data added successfully.................")

############ delete the user 
    Studentdata.objects.filter(name='rose').delete()
# u delete a entry from ur course then what changes do u see in ur student table


    #fetch data
    fetch1= Studentdata.objects.get(name='john')
    fetch_name= fetch1.course.course_name
    #fetch2=Coursedata.objects.get(course_name=fetch1.course)
    print("course for user is ",fetch2)

    return render(request,"helllooooo we are working on models")
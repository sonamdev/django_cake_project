from django.urls import path
from . import views

urlpatterns = [
   path('student_info',views.studentinfo,name='student_info'),

]

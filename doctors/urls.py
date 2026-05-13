from django.urls import path
from doctors import views
urlpatterns=[
    path('all-doctors/',views.alldoctors, name="alldoctors"),
    path('treatment/', views.treatment, name="treatment"),
   
    path('doctorslist/<str:category>/', views.doctorslist, name="doctorslist"),
    path('appointment/<str:doc_name>/<str:cat_name>/', views.appointment, name="appointment")

]
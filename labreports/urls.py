from django.urls import path
from labreports import views
urlpatterns=[

    path('labtechreg',views.labtechreg, name="labtechreg"),
    path('alltests',views.alltests, name="alltests"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('discharge',views.discharge, name="discharge"),
    path('addlabtests',views.addlab_tests, name="addlabtests"),
    path('editlabtests/<int:id>/',views.addlab_tests, name="editlabtests"),
    

]
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
   # path('doctor_login', views.doctor_login, name='doctor_login'),
   path('doctor', views.doctor, name='doctor'),
    path('logout',views.logout,name='logout'),
   path('dabout1', views.dabout1, name='dabout1'),
    
   path('dservice', views.dservice, name='dservice'),
   path('dcontact1', views.dcontact1, name='dcontact1'),
   path('showAppointment', views.showAppointment, name='showAppointment'),
   path('drSchedule', views.drSchedule, name='drSchedule'),
   path('dongoing',views.dongoing,name='dongoing'),
   path('dupcoming',views.dupcoming,name='dupcoming'),
   path('dupcoming1',views.dupcoming1,name='dupcoming1'),
   path('doutgoing',views.doutgoing,name='doutgoing'),
   path('docprescription',views.docprescription,name='docprescription'),
   path('get_appointment_info',views.get_appointment_info, name='get_appointment_info'),
 
]
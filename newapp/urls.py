from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('',views.index,name='index'),
    path('contact1.html',views.contact1,name='contact1'),
    path('blog.html',views.blog,name='blog'),
    path('detail.html',views.detail,name='detail'),
    path('team.html',views.team,name='team'),
    path('testimonial.html',views.testimonial,name='testimonial'),
    path('appointment.html',views.appointment,name='appointment'),
    path('search.html',views.search,name='search'),
    path('about1.html',views.about1,name='about1'),
    path('price.html',views.price,name='price'),
    path('service.html',views.service,name='service'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name='logout'),
    path('p_view',views.p_view,name='p_view'),
    path('complain',views.complain,name='complain'),
    path('feedback',views.feedback,name='feedback'),
    path('update_user',views.update_user,name='update_user'),
    path('ongoing.html',views.ongoing,name='ongoing'),
    path('upcoming.html',views.upcoming,name='upcoming'),
    path('outgoing.html',views.outgoing,name='outgoing'),
    path('paymentinvoice.html',views.paymentinvoice,name='paymentinvoice'),
    path('get_doctors/', views.get_doctors, name='get_doctors'),
    path('get_slots/', views.get_slots, name='get_slots'),
    path('reset_password',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name="reset_password"),
    path('reset_password_sent',auth_views.PasswordResetDoneView.as_view(template_name="reset_password_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>',auth_views.PasswordResetConfirmView.as_view(template_name="reset.html"),name="password_reset_confirm"),
    path('reset_password_complete',auth_views.PasswordResetCompleteView.as_view(template_name="reset1.html"),name="password_reset_complete"),
    path('service_1.html',views.service_1,name='service_1'),
    path('service_2.html',views.service_2,name='service_2'),
    path('service_3.html',views.service_3,name='service_3'),
    path('service_4.html',views.service_4,name='service_4'),
    path('service_5.html',views.service_5,name='service_5'),
    path('service_6.html',views.service_6,name='service_6'),
    path('success',views.OrderSuccess,name='success'),
    path('updateAppointment',views.updateAppointment,name='updateAppointment'),
    path('prescription',views.prescription,name='prescription'),

    
   

]
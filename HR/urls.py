from django.conf.urls import url
from . import views

app_name = 'HR'
urlpatterns = [
    url(r'^login/', views.user_login, name='login'),
    url(r'^logout', views.user_logout, name='logout'),
    url(r'^employee_profile/', views.employee_profile, name='employee_profile'),
    url(r'^home/', views.home, name='home'),
    url(r'^dashboard/', views.dashboard, name='dashboard'),
    url(r'^employee_complaints/', views.employee_complaints, name='employee_complaints'),
    url(r'^employee_feedback/', views.employee_feedback, name='employee_feedback'),
    url(r'^complaints/', views.complaints, name='complaints'),
    url(r'^feedback/', views.feedback, name='feedback'),
    url(r'^about/', views.about, name='about'),

]
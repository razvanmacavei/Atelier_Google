from user_profile import views
from django.urls import path

app_name = 'userprofile'

urlpatterns = [

    path('start_timesheet/', views.new_timesheet, name = 'start_pontaj'),
    path('stop_timesheet/', views.stop_timesheet, name = 'stop_pontaj'),

]
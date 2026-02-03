from django.urls import path
from .views import JobListAPI, JobCreateAPI, ApplicationListAPI, ApplicationCreateAPI, home

urlpatterns = [
    path('', home, name='home'),                    
    path('api/jobs/', JobListAPI.as_view(),
         name='job-list'),          
    path('api/jobs/create/', JobCreateAPI.as_view(),
         name='job-create'),  
    path('api/applications/', ApplicationListAPI.as_view(),
         name='application-list'),  
    path('api/applications/create/', ApplicationCreateAPI.as_view(),
         name='application-create'), 
]

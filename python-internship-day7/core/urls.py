from django.contrib import admin
from django.urls import path
# import view from app folder
from apps.views import (
    home, JobListAPI, JobCreateAPI,
    ApplicationListAPI, ApplicationCreateAPI
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # Day 3 Task URL (Root URL)
    path('', home, name='home'),

    # Day 5/7 API URLs
    path('api/jobs/', JobListAPI.as_view(), name='job-list'),
    path('api/jobs/create/', JobCreateAPI.as_view(), name='job-create'),
    path('api/applications/', ApplicationListAPI.as_view(), name='application-list'),
    path('api/applications/create/',
         ApplicationCreateAPI.as_view(), name='application-create'),
]

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Job, Application
from .serializers import JobSerializer, ApplicationSerializer

# Existing home view


def home(request):
    return HttpResponse("Hello Zecpath Backend")

# Job APIs


class JobListAPI(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)


class JobCreateAPI(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Application APIs


class ApplicationListAPI(APIView):
    def get(self, request):
        apps = Application.objects.all()
        serializer = ApplicationSerializer(apps, many=True)
        return Response(serializer.data)


class ApplicationCreateAPI(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

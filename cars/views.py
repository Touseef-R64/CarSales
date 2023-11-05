from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
import environ
from django.urls import reverse
from rest_framework import status
env = environ.Env()
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken

class HomePageView(APIView):
    def get(self, request, *args, **kwargs):
        
        # context = {
    
        #     'form': form,  # Initialize an empty registration form
        # }
        return render(request, 'views/index.html')

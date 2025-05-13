from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from .utils.csv_util import create_csv

def index(request):
    return render(request, 'index.html')

class CourseView(APIView):
    def get(self, request):
        pl =  Courses.objects.all().order_by('-id')
        serializer = CourseSerializer(pl,many = True)
        return Response(serializer.data)

class PlacementView(APIView):
    def get(self, request):
        pl =  Placement.objects.all()
        serializer = PlacementSerializer(pl,many = True)
        return Response(serializer.data)

class HireView(APIView):
    def get(self, request):
        pl =  Hire.objects.all().order_by('-id')
        serializer = HireSerializer(pl,many = True)
        return Response(serializer.data)

class TeamView(APIView):
    def get(self, request):
        pl =  Team.objects.all()
        serializer = TeamSerializer(pl,many = True)
        return Response(serializer.data)

class NewsView(APIView):
    def get(self, request):
        pl =  News.objects.all().order_by('-id')[:2]
        serializer = NewsSerializer(pl,many = True)
        return Response(serializer.data)

class StoryView(APIView):
    def get(self, request):
        pl =  Stories.objects.all().order_by('-id')[:5]
        serializer = StorySerializer(pl,many = True)
        return Response(serializer.data)

class CareerView(APIView):
    def get(self, request):
        pl =  Career.objects.all().order_by('-id')
        serializer = CareerSerializer(pl,many = True)
        return Response(serializer.data)

class AppView(APIView):
    def get(self, request):
        pl =  Application.objects.all()
        serializer = AppSerializer(pl,many = True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            resume = request.FILES.get('resume')
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            position = request.POST.get('position')
            apps = Application.objects.filter(Q(phone=phone) | Q(email=email)).exists()
            if apps:
                return Response({'status':False,'message': 'Application exists already'})
            else:
                app = Application(
                    name=name,
                    phone=phone,
                    email=email,
                    position=position,
                    resume=resume,
                )
                app.save()
                return Response({'status':True,'message': 'Application submitted successfully'})

class GameView(APIView):
    def get(self, request):
        pl =  Games.objects.all().order_by('-id')
        serializer = GameSerializer(pl,many = True)
        return Response(serializer.data)
    
class ContactView(APIView):
    def get(self, request):
        pl =  Contact.objects.all()
        serializer = ContactSerializer(pl,many = True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            place = request.POST.get('place')
            message = request.POST.get('message')
            contact = Contact(name=name,phone=phone,email=email,place=place,message=message)
            contact.save()
            return Response({'status':True,'message': 'Your message has been submitted'})

class FormView(APIView):
    def get(self, request):
        pl =  Form.objects.all()
        serializer = FormSerializer(pl,many = True)
        return Response(serializer.data)
    @csrf_exempt
    def post(self,request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            email = request.POST.get('email')
            place = request.POST.get('place')
            print(name)
            contact = Form(name=name,phone=phone,email=email,place=place)
            contact.save()
            return Response({'status':True,'message': 'Your message has been submitted'})

class LeadView(APIView):

    @csrf_exempt
    def post(self, request):
        if request.method == 'POST':
            data = request.data
            csv = create_csv(data)
            return Response({'status':True,'message': 'Your message has been saved'})
        
class SignupView(APIView):
    @csrf_exempt 
    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': True, 'message': 'Signup successful'})
        return Response({'status': False, 'errors': serializer.errors}, status=400)

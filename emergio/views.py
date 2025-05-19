from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q, Count
from .utils.csv_util import create_csv

def index(request):
    return render(request, 'index.html')

class CourseView(APIView):
    def get(self, request):
        pl =  Courses.objects.all().order_by('-id')
        serializer = CourseSerializer(pl,many = True)
        return Response(serializer.data)

class CourseDetailView(APIView):
    def get(self, request, pk):
        try:
            course = Courses.objects.get(id=pk)
            serializer = CourseSerializer(course, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Courses.DoesNotExist:
            return Response({'error': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

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

# class CareerView(APIView):
#     def get(self, request):
#         pl =  Career.objects.all().order_by('-id')
#         serializer = CareerSerializer(pl,many = True)
#         return Response(serializer.data)

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

class JobListView(APIView):
    def get(self, request):
        category = request.GET.get('category')
        location = request.GET.get('location')

        if category and location:
            jobs = Career.objects.filter(
                Q(category__category__icontains=category) & Q(locations__contains=[location])
            )
        elif category:
            jobs = Career.objects.filter(category__category__icontains=category)
        elif location:
            jobs = Career.objects.filter(locations__contains=[location])
        else:
            jobs = Career.objects.all()

        serializer = CareerSerializer(jobs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobCategoryCountView(APIView):
    def get(self, request):
        formatted = []

        # Get all categories
        all_categories = Category.objects.all()

        for category in all_categories:
            job_count = Career.objects.filter(category=category).count()
            formatted.append({
                'category': category.category,
                'image': category.image.url if category.image else None,
                'count': job_count
            })

        return Response(formatted, status=status.HTTP_200_OK)



# class CurrentVacancyView(APIView):
#     def get(self, request):
#         jobs = Job.objects.all().order_by('-posted_on')[:10]  # Latest 10 jobs
#         data = []

#         for job in jobs:
#             data.append({
#                 "title": job.title,
#                 "location_count": len(job.locations),
#                 "locations": job.locations
#             })

#         return Response(data, status=status.HTTP_200_OK)

class CurrentVacancyView(APIView):
    def get(self, request):
        today = timezone.now().date()
        current_month_jobs = Career.objects.filter(
            posted_on__year=today.year,
            posted_on__month=today.month
        ).order_by('-posted_on')

        if current_month_jobs.exists():
            jobs = current_month_jobs
        else:
            jobs = Career.objects.all().order_by('-posted_on')[:10]

        data = []
        for job in jobs:
            data.append({
                "title": job.position,
                "location_count": len(job.locations),
                "locations": job.locations
            })

        return Response(data, status=status.HTTP_200_OK)
class CurrentVacancyView(APIView):
    def get(self, request):
        today = timezone.now().date()
        current_month_jobs = Career.objects.filter(
            posted_on__year=today.year,
            posted_on__month=today.month
        ).order_by('-posted_on')

        if current_month_jobs.exists():
            jobs = current_month_jobs
        else:
            jobs = Career.objects.all().order_by('-posted_on')[:10]

        data = []
        for job in jobs:
            locations = job.locations or []
            data.append({
                "title": job.position,
                "description": job.description,
                "posted_on": job.posted_on,
                "category": job.category.category if job.category else None,
                "location_count": len(locations),
                "locations": locations
            })

        return Response(data, status=status.HTTP_200_OK)

class TestimonialView(APIView):
    def get(self, request):
        pl =  Testimonial.objects.all().order_by('-id')
        serializer = TestimonialSerializer(pl,many = True)
        return Response(serializer.data)
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('emergio/units/course',CourseView.as_view()),
    path('emergio/units/placement',PlacementView.as_view()),
    path('emergio/units/team',TeamView.as_view()),
    path('emergio/units/news',NewsView.as_view()),
    path('emergio/units/story',StoryView.as_view()),
    path('emergio/units/career',CareerView.as_view()),
    path('emergio/units/application',AppView.as_view()),
    path('emergio/units/game',GameView.as_view()),
    path('emergio/units/contact',ContactView.as_view()),
    path('emergio/units/form',FormView.as_view()),
    path('emergio/units/lead',LeadView.as_view()),
]
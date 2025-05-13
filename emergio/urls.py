from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('emergio/course/', CourseView.as_view()),
    path('emergio/placement/', PlacementView.as_view()),
    path('emergio/team/', TeamView.as_view()),  # fixed typo
    path('emergio/news/', NewsView.as_view()),
    path('emergio/story/', StoryView.as_view()),
    # path('emergio/career/', CareerView.as_view()),
    path('emergio/application/', AppView.as_view()),
    path('emergio/game/', GameView.as_view()),
    path('emergio/contact/', ContactView.as_view()),
    path('emergio/form/', FormView.as_view()),
    path('emergio/lead/', LeadView.as_view()),
    path('emergio/signup/', SignupView.as_view()),
    path('emergio/jobs/', JobListView.as_view()),
    path('emergio/job-categories/', JobCategoryCountView.as_view()),
    path('emergio/current-vacancies/', CurrentVacancyView.as_view()),
]


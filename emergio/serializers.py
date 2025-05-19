from rest_framework import serializers
from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    team_members = TeamSerializer(many=True, read_only=True)
    class Meta:
        model = Courses
        fields = '__all__'

class PlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Placement
        fields = '__all__'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = '__all__'

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class HireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hire
        fields = '__all__'

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'
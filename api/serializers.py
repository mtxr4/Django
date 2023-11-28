from rest_framework import  *
from app.models import CustomUser,Student,Course,Session_Time

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email','user_type','id')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('address','gender','course_id', 'admin')

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name','created_ad','updated_ad')

class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session_Time
        fields = ('sesstion_start', 'sesstion_end')
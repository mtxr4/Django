from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from app.models import CustomUser,Student,Course,Session_Time
from .serializers import CustomUserSerializer,StudentSerializer,CourseSerializer,SessionSerializer

class CustomUserView(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewDetails(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class StudentView(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class CourseView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SessionView(ListAPIView):
    queryset = Session_Time.objects.all()
    serializer_class = SessionSerializer
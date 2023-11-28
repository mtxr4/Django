from django.urls import path
from .views import CustomUserView, StudentView,CourseView,SessionView,CustomUserViewDetails

urlpatterns = [
    path('', CustomUserView.as_view()),
    path('<int:pk>', CustomUserViewDetails.as_view()),
    path('student/', StudentView.as_view()),
    path('course/', CourseView.as_view()),
    path('session/', SessionView.as_view())
]
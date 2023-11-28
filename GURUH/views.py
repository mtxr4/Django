from django.shortcuts import redirect,render
from app.models import CustomUser, Session_Time,Course,Student


def BASE(request):
    return render(request,'base.html')

def HOME(request):
    course = Course.objects.all()
    context = {
        'course': course
    }
    return render(request, 'Main/home.html', context=context)
def ABOUT(request):
    return render(request, 'Main/about.html')


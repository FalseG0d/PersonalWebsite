from django.shortcuts import render,redirect
from Home.models import About

# Create your views here.
def date(request):
    if request.user.is_authenticated:
        about=About.objects.all()[0]

        context={
            'about':about
        }

        return render(request,"dates.html",context)
    else:
        return redirect('/')
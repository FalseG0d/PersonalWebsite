from django.shortcuts import render
from Home.models import About,Link

# Create your views here.
def blog(request):
    about=About.objects.all()[0]
    links=Link.objects.all()
    context={
        'about':about,
        'links':links,
    }
    return render(request,"blog.html",context)
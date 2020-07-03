from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    about=About.objects.all()[0]
    work=Work.objects.all()
    paper=Paper.objects.all()
    count=Count.objects.all()
    podcast=Podcast.objects.all()
    skill=Skill.objects.all()
    article=Article.objects.all()
    link=Link.objects.all()

    context={
        'about':about,
        'works':work,
        'papers':paper,
        'counter':count,
        'podcasts':podcast,
        'skills':skill,
        'articles':article,
        'links':link,
    }

    return render(request,"index.html",context)
from django.shortcuts import render,redirect
from .models import *
from .forms import MessageForm

# Create your views here.

def home(request):
    about=About.objects.all()[0]
    work=Work.objects.all()
    paper=Paper.objects.all()
    count=Count.objects.all()
    podcast=Media.objects.all()
    skill=Skill.objects.all()
    article=Article.objects.all()
    link=Link.objects.all()
    message_form=MessageForm()
    game=Game.objects.all()

    context={
        'about':about,
        'works':work,
        'papers':paper,
        'counter':count,
        'podcasts':podcast,
        'skills':skill,
        'articles':article,
        'links':link,
        'message_form':message_form,
        'games':game,
    }

    return render(request,"index.html",context)

def mail(request):
    if request.method=='POST':
        form=MessageForm(request.POST)
        if form.is_valid:
            form.save()
    
    return redirect('/')
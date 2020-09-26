from django.db import models

# Create your models here.

class Game(models.Model):
    name=models.CharField(max_length=20)
    play_link=models.CharField(max_length=200,default='#')
    itch_link=models.CharField(max_length=200,default='#')
    image=models.ImageField(upload_to="gameimages")
    description=models.TextField()
    genre=models.CharField(max_length=20)

    visible=models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
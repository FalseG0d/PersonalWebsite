from django.db import models

# Create your models here.

class UnityGame(models.Model):
    name=models.CharField(max_length=20)
    play_link=models.URLField(max_length=200,default='#')
    itch_link=models.URLField(max_length=200,default='#')
    image=models.ImageField(upload_to="gameimages")
    description=models.TextField()
    def __str__(self):
        return self.name
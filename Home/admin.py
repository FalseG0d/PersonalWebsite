from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header="Apoorv Garg"
admin.site.site_title="Apoorv Garg"

admin.site.register(About)
admin.site.register(Work)
admin.site.register(Paper)
admin.site.register(Count)
admin.site.register(Podcast)
admin.site.register(Skill)
admin.site.register(Article)
admin.site.register(Link)
admin.site.register(Message)
admin.site.register(Game)
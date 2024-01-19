from django.contrib import admin
from .models import *

class AdminArticle(admin.ModelAdmin):
	model=Article
	list_display=['title','date']

admin.site.register(Article,AdminArticle)

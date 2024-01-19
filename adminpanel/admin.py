from django.contrib import admin
from .models import Message

class AdminMessage(admin.ModelAdmin):
	model=Message
	list_display=['id','name','read','date']

admin.site.register(Message,AdminMessage)

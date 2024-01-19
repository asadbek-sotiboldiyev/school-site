from django.urls import path
from .views import *

urlpatterns=[
	path('messages/',MessagesView,name='MessagesPage'),
	path('message/<int:message_id>',MessageView,name='MessagePage'),
]
from django.db import models

class Message(models.Model):
	name=models.CharField(max_length=250)
	phone=models.CharField(max_length=150)
	body=models.TextField()
	read=models.BooleanField(default=False)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
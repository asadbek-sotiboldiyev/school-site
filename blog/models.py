from django.db import models
from datetime import datetime

class Article(models.Model):
	title=models.CharField(max_length=250)
	description=models.CharField(max_length=300,null=True,blank=True)
	body=models.TextField()
	image=models.ImageField(upload_to='article_images',blank=True,null=True)
	date=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title
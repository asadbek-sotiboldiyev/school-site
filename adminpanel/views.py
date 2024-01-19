from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from .models import Message
from django.contrib import messages

def LoginView(request):
	context={}
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		user=User.objects.filter(username=username)
		if user.exists():
			user=user.first()
			if user.check_password(password):
				login(request,user)
				return redirect('HomePage')
			else:
				context={
					'username':username,
					'error':"Ma'lumotlar xato!"
				}
		else:
			context={
				'username':username,
				'error':"Ma'lumotlar xato!"
			}
	return render(request,'control/LoginPage.html',context)

def Logout(request):
	logout(request)
	return redirect('HomePage')

def ContactView(request):
	if request.method=='POST':
		name=request.POST['name']
		email=request.POST['email']
		body=request.POST['body']
		new_message=Message.objects.create(name=name,phone=email,body=body)
		new_message.save()
		messages.success(request,1)
	return redirect('HomePage')
	

def MessagesView(request):
	if not request.user.is_superuser:
		return render(request,'404.html')		
	messages=Message.objects.all().order_by('read')
	return render(request,'control/AdminPage.html',{'messages':messages})

def MessageView(request,message_id):
	if not request.user.is_superuser:
		return render(request,'404.html')
	message=Message.objects.filter(id=message_id)
	if message.exists():
		message=message.first()		
	else:
		return render(request,'404.html')
	message.read=True
	message.save()
	if request.method=='POST':
		message.delete()
		return redirect('MessagesPage')
	return render(request,'control/MessagePage.html',{'message':message})
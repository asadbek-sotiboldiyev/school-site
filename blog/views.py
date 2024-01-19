from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import Article

def HomePageView(request):
	last_new=Article.objects.last()
	last_news=Article.objects.all()[::-1][0:3]
	print(last_news)
	context={
		'last_new':last_new,
		'last_news':last_news,
	}
	return render(request,'HomePage.html',context)

def ArticlesPageView(request):
	articles=Article.objects.all()[::-1]
	return render(request,'blog/ArticlesPage.html',{"articles":articles})

def ArticlePageView(request,article_id):
	article=get_object_or_404(Article, id=article_id)
	return render(request,'blog/ArticlePage.html',{'article':article})

def ArticleAddView(request):
	if request.method=='POST':
		title=request.POST['title']
		description=request.POST['description']
		body=request.POST['body']
		image=request.FILES.get('image',False)
		if image:
			new_article=Article.objects.create(title=title,body=body,image=image,description=description)
		else:
			new_article=Article.objects.create(title=title,body=body,description=description)
		new_article.save()
		return redirect('ArticlePage',article_id=new_article.id)
	return render(request,'blog/ArticleAdd.html')

def ArticleEditView(request,article_id):
	if not request.user.is_superuser:
		return render(request,'403.html')
	article=get_object_or_404(Article, id=article_id)

	if request.method=='POST':
		article.title=request.POST['title']
		article.description=request.POST['description']
		article.body=request.POST['body']
		article.image=request.FILES.get('image', False)
		article.save()
		return redirect('ArticlePage',article_id=article.id)
	return render(request,'blog/ArticleEdit.html',{'article':article})

def ArticleDeleteView(request,article_id):
	if not request.user.is_superuser:
		return render(request,'403.html')
	article=get_object_or_404(Article, id=article_id)

	if request.method=='POST':
		article.delete()
		return redirect('ArticlesPage')
	return render(request,'blog/ArticleDelete.html',{'article':article})
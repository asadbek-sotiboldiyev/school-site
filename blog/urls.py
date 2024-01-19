from django.urls import path
from .views import *

urlpatterns=[
	path('',HomePageView,name='HomePage'),
	path('articles/',ArticlesPageView,name='ArticlesPage'),
	path('article/add',ArticleAddView,name='ArticleAdd'),
	path('article/<int:article_id>',ArticlePageView,name='ArticlePage'),
	path('article/<int:article_id>/edit',ArticleEditView,name='ArticleEditPage'),
	path('article/<int:article_id>/del',ArticleDeleteView,name='ArticleDeletePage'),
]

from django.urls import path

from . import views


app_name = 'word_count'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('wordcount/', views.WordCountView.as_view(), name='api'),
    path('docs/', views.DocsView.as_view(), name='docs'),
]

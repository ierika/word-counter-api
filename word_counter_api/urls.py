from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('word_count.urls', namespace='wordcount')),
    path('admin/', admin.site.urls),
]

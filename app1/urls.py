from django.urls import path
from .import views
urlpatterns = [
path('', views.index, name ='index'),
path('register', views.register, name ='register'), 
path('videos', views.videos, name ='videos'), 
path('log', views.log, name ='log'), 
path('logouts', views.logouts, name ='logouts'), 
path('add_video', views.add_video, name ='add_video'), 
path('play/<int:id>', views.play, name ='play'), 
path('analysis', views.analysis, name ='analysis'), 
]
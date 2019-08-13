from django.urls import include,path
from .views import *



urlpatterns = [
    path('history/', history, name='history'),
    path('upload/', upload, name='upload'),
    path('history/<int:id>/', history_detail, name='history_detail'),
]
    

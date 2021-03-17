from .views import persons_list
from django.urls import path, include


urlpatterns = [
    path('list/', persons_list),
] 

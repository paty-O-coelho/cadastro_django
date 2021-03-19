from django.urls import path, include
from .views import persons_list
from .views import persons_new


urlpatterns = [
    path('list/', persons_list, name='person_list'),
    path('new/', persons_new, name='person_new'),
    path('update/', persons_new, name='person_new'),
] 

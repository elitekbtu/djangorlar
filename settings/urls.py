# Django modules
from django.contrib import admin
from django.urls import path

#Project modules 
from apps.tasks.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome_view), 
    path('users/', users_view), 
    path('city-time/', city_time_view), 
    path('count/', count_view)
]

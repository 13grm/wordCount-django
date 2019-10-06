from django.urls import path
from django.urls import include
from .views  import (home,
                    count,)



urlpatterns = [
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('count/', count, name='count'),


]

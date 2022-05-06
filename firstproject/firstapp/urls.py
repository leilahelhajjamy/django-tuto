
from django.urls import path

from . import views


urlpatterns = [
    path('home/', views.display),
    path('datetime/',views.displayDateTime),
    path('firstTemplate/' ,views.home)
]

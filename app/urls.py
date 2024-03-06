from django.urls import path
from . import views


urlpatterns = [
    path("",views.home,name="home"),
    path("book/",views.book,name="book"),
    path("about/",views.about,name="about"),
    path("products/bride",views.bride,name="bride"),
    path("products/portraits",views.portraits,name="portraits"),

    
]

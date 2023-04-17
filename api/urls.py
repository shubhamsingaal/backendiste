from django.urls import path
# from django.conf.urls import url 
from api import views

urlpatterns = [
    path('student/', views.StudentList.as_view()),
    path('alumni/', views.AlumniList.as_view()),
    path('events/', views.EventsList.as_view()),
    path('gallery/', views.galleryList.as_view()),
    path('blog/', views.blogList.as_view()),
    path('sponsers/', views.sponsersList.as_view()),
    path('contact/', views.messages),
]
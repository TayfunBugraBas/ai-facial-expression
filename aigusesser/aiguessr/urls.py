from django.urls import path

from . import views

urlpatterns = [
    path('upload_audio/', views.upload_audio, name='upload_audio'),
    path('uploadImage/', views.upload_image, name='upload_image'),
    path('getCalculatedResult/',views.getCalculatedResult,name="getCalculatedResult"),
    path("home",views.home, name="home")
]
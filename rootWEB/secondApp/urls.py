from django.urls import path

from secondApp import views

urlpatterns = [
    path("index/", views.index),
    path("test/", views.test),
    path("", views.chatbot),
    path('chattrain/', views.chattrain, name='chattrain'),
    path('chatanswer/', views.chatanswer, name='chatanswer'),
]

from django.urls import path

from . import views

app_name = 'map'

urlpatterns = [
    path("", views.map, name='map'),
    # path('index/', views.index),
    # path('index2/', views.index2),
    # path('index3/', views.index3),
    # path('index4/', views.index4),
    # path('index5/', views.index5),
    # path('index6/', views.index6),
    # path('index7/', views.index7),
    # path('index8/', views.index8),
    # path('index9/', views.index9),
    # path('fads/', views.fads),
     path('jongno/', views.jongno),
     path('seocho/', views.seocho),
     path('gwangjin/', views.gwangjin),
     path('seongdong/', views.seongdong),
     path('yongsan/', views.yongsan),
]
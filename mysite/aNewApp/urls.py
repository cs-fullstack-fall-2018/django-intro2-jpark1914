from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hello/<str:name>/', views.hello, name='hello'),
    path('times2/<int:number>/',views.times2, name='times2'),
    path('addition/<int:sum>/', views.addition, name='addition')
]
from django.urls import path
from . import views


urlpatterns = [
    path('main/<str:firstname>/<str:surname>/<str:code>/<int:id>/<int:user_id>', views.Question, name="main"),
    path('home/', views.Home, name="home"),
    path('', views.Index, name="index"),
    path('practice/', views.Practice, name="offline"),
]

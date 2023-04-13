from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.chat, name="chat"),
    path('createform/', views.createform, name='createform'),
    path("signup", views.signup, name="signup"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("home", views.home, name="home"),
]
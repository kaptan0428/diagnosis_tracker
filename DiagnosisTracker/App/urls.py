from django.urls import path
from App import views

urlpatterns = [
    # path("", views.hello_world),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    # path('services', views.services, name="services"),
    # path('contact', views.contact, name="contact"),
    # path('signin', views.signin, name="signin"),
    path('signup', views.signup, name="signup"),
    path('welcome', views.welcome, name="welcome"),
    path('main', views.main, name="main"),
    path('logout', views.logout, name="log"),
    path('data', views.data, name="data"),
    path('createpost', views.createpost, name="createpost"),

]

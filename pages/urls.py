from django.urls import path, include
from .views import homePageView, aboutPageView, sunwooPageView, results, homePost, todos, register, message, logoutView, secretArea

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('sunwoo/', sunwooPageView, name='sunwoo'),
    path('homePost/', homePost, name='homePost'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
    path('todos', todos, name='todos'),
    path("register/", register, name="register"),  # <-- added
    path('message/<str:msg>/<str:title>/', message, name="message"),  # <-- added
    path('', include("django.contrib.auth.urls")), # <-- added
    path("logout/", logoutView, name="logout"),
    path("secret/", secretArea, name="secret"),
]
from django.urls import path
from .views import LoginView, UserView
from knox.views import LogoutView, LogoutAllView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path("signup/", UserView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('logallout/', LogoutAllView.as_view()),
]
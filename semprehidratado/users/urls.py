from django.urls import path
from . import views
urlpatterns = [
    path('koala/', views.helloworld),
    path('register/', views.SignUp.as_view()),
]
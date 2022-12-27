from django.urls import path
from users import views

urlpatterns = [
  path('user/', views.UserInformation.as_view()),
  path('register/', views.RegisterAPI.as_view(), name='register'),
  path('user/edit/', views.UserInformation.as_view()),
]
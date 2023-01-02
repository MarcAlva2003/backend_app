from django.urls import path
from companies import views

urlpatterns = [
  path('list/', views.CompanyList.as_view()),
  path('<int:pk>', views.SingleCompanyPublic.as_view()),
  path('add/', views.SingleCompany.as_view()),
  path('delete/<int:pk>', views.SingleCompany.as_view()),
  path('edit/<int:pk>', views.SingleCompany.as_view())
]
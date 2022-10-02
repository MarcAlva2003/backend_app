from django.urls import path
from public_api import views

urlpatterns = [
  path('companies/', views.CompanyList.as_view()),
  path('companies/<int:pk>', views.SingleCompany.as_view()),
  path('companies/add/', views.SingleCompany.as_view()),
  path('companies/delete/<int:pk>', views.SingleCompany.as_view()),
  path('companies/edit/<int:pk>', views.SingleCompany.as_view())
]
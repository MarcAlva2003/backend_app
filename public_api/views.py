from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Company
from .serializers import CompanySerializer
from public_api import serializers

NOT_FOUND_MESSAGE_404 = "404 - Sorry. No company found."
COMPANT_CREATED_201 = "Company added successfuly."
NOT_CREATED_ERROR = "Error. Company could not be added."
COMPANY_DELETED = "Company deleted successfuly."
COMPANY_UPDATED = "Company updated successfuly."

# Create your views here.
class CompanyList(APIView):
  def get(self, request):
    companies = Company.objects.all().order_by('id')
    serializer = CompanySerializer(companies, many = True)
    if companies:
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"Fail": NOT_FOUND_MESSAGE_404}, status=status.HTTP_404_NOT_FOUND)


class SingleCompany(APIView):
  def get(self, request, pk):
    company = Company.objects.filter(pk = pk).first()
    serializer = CompanySerializer(company)
    if company:
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"Fail": NOT_FOUND_MESSAGE_404}, status=status.HTTP_404_NOT_FOUND)

  def post(self, request, format=None):
    serializer = CompanySerializer(data=request.data)
    if serializer.is_valid(): 
      serializer.save()
      return Response({"Success": COMPANT_CREATED_201}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  def delete(self, request, pk):
    company = Company.objects.filter(pk = pk).first()
    if company:
      company.delete()
      return Response({"Success": COMPANY_DELETED}, status=status.HTTP_200_OK)
    return Response({"Fail": NOT_FOUND_MESSAGE_404}, status=status.HTTP_404_NOT_FOUND)

  def put(selg, request, pk):
    company = Company.objects.filter(pk = pk).first()
    if company:
      data = request.data
      company.pk = company.pk
      company.name = data["name"]
      company.company_business = data["company_business"]
      company.foundation_date = data["foundation_date"]
      company.foundation_country = data["foundation_country"]
      company.save()
      serializer = CompanySerializer(company)
      return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"Fail": NOT_FOUND_MESSAGE_404}, status=status.HTTP_404_NOT_FOUND)
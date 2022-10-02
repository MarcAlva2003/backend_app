from dataclasses import field
from rest_framework import serializers
from .models import Company

class CompanySerializer(serializers.ModelSerializer):
  class Meta:
    model= Company
    fields=["id", "name", "company_business", "foundation_date", "foundation_country"]
    read_only_fields = [
      "id"
    ]
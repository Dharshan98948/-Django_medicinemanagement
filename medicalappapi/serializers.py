from medicalapp.models import Medicine
from rest_framework import serializers
from rest_framework. serializers import ModelSerializer

class medicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'